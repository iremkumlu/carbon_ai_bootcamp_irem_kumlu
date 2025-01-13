import streamlit as st
import requests

# Streamlit arka plan stilini ayarlama
st.markdown(
    """<style>.stApp {background-image: url('https://media.istockphoto.com/id/1074160890/photo/colorful-cotton-candy-soft-fog-and-clouds-with-a-pastel-colored-pink-to-skyblue-gradient-for.webp?a=1&b=1&s=612x612&w=0&k=20&c=FxU4J8vbFBAiPIuGUfjdFkiIhS286C3OFmaZ_B9HsYI=');background-size: cover;}</style>""",
    unsafe_allow_html=True
)

# Streamlit başlık
st.title("Soru Cevaplama Arayüzü")

# Kullanıcıdan soruyu al
query = st.text_input("Soru Sorun:")

if query:
    response = requests.post("http://127.0.0.1:8000/chat/", json={"query": query})
    data = response.json()
    
    # Cevapları göster
    st.write(data['answers'])
    
    # Dosya kaydetme ve indirme
    output_text = f"Soru: {query}\nCevap: {data['answers']}"
    with open("output_task2.txt", "w", encoding="utf-8") as file:
        file.write(output_text)
    
    # Dosyayı indirme butonu
    with open("output_task3.txt", "r", encoding="utf-8") as file:
        file_data = file.read()  # Dosya verisini oku
        st.download_button(
            label="output_task3 dosyasını indir",
            data=file_data,  # Dosya verisini butona aktar
            file_name="output_task3.txt",
            mime="text/plain"
        )

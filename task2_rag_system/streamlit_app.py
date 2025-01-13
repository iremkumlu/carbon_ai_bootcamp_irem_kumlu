import streamlit as st
import requests

# Streamlit arayüzüne arka plan resmi verelim
st.markdown(
    """<style>.stApp {background-image: url('https://media.istockphoto.com/id/1074160890/photo/colorful-cotton-candy-soft-fog-and-clouds-with-a-pastel-colored-pink-to-skyblue-gradient-for.webp?a=1&b=1&s=612x612&w=0&k=20&c=FxU4J8vbFBAiPIuGUfjdFkiIhS286C3OFmaZ_B9HsYI=');background-size: cover;}</style>""",
    unsafe_allow_html=True
)

# Streamlit başlığı
st.title("Soru Cevaplama Uygulaması")

# Kullanıcıdan soruyu alalım
query = st.text_input("Soru Sorun:")

if query:
    response = requests.post("http://127.0.0.1:8000/chat/", json={"query": query})
    data = response.json()
    
    # Cevapları gösterelim
    st.write(data['answers'])
    
    # Dosyayı kaydetme ve indirme işlemi burada gerçekleşir
    output_text = f"Soru: {query}\nCevap: {data['answers']}"
    with open("output_task2.txt", "w", encoding="utf-8") as file:
        file.write(output_text)
    
    # Dosyayı indirme butonu :
    with open("output_task2.txt", "r", encoding="utf-8") as file:
        file_data = file.read()  # Dosya verisini okunur
        st.download_button(
            label="output_task2 dosyasını indir",
            data=file_data,  # Dosya verisi butona aktarılır
            file_name="output_task2.txt",
            mime="text/plain"
        )

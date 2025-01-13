import os
import requests
import streamlit as st
from haystack.agents import Agent, Tool
from haystack.nodes import PromptNode
from haystack.agents.conversational import ConversationalAgent

# Streamlit arayüzüne arka plan resmi verelim
st.markdown(
    """<style>.stApp {background-image: url('https://media.istockphoto.com/id/1074160890/photo/colorful-cotton-candy-soft-fog-and-clouds-with-a-pastel-colored-pink-to-skyblue-gradient-for.webp?a=1&b=1&s=612x612&w=0&k=20&c=FxU4J8vbFBAiPIuGUfjdFkiIhS286C3OFmaZ_B9HsYI=');background-size: cover;}</style>""",
    unsafe_allow_html=True
)

# API anahtarı ve URL bilgileri : 
weather_api_key = "7000de40458363ace6929e6573bc87d8"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

# Haystack PromptNode
prompt_node = PromptNode("gpt2-medium", use_gpu=True)

#Veriyi özetleme işlemi :
class WeatherSummarizer(Tool):
    def __init__(self):
        super().__init__(
            name="WeatherSummarizer",
            description="Hava durumu verilerini özetler.",
            pipeline_or_node=prompt_node
        )

    def run(self, weather_data):  # Burada weather_data parametresini alacak şekilde düzenledik
        city_name = weather_data["city"]
        temperature = weather_data["temperature"]
        weather_description = weather_data["weather_description"]
        wind_speed = weather_data["wind_speed"]
        
        weather_summary = f"Şehir: {city_name}, Sıcaklık: {temperature}°C, Hava Durumu: {weather_description}, Rüzgar: {wind_speed} km/s."
        

        return weather_summary  # Özet döndürülüyor



# Tavsiye oluşturmak için araç oluşturalım
class WeatherAdvice(Tool):
    def __init__(self):
        super().__init__(
            name="WeatherAdvice",
            description="Hava durumu verilerine göre tavsiyeler üretir.",
            pipeline_or_node=None  
        )

    def run(self, query):
        city = query.get("city")
        temperature = query.get("temperature")
        rain_probability = query.get("rain_probability")
        wind_speed = query.get("wind_speed")

        if rain_probability > 50:
            return f"{city} için hava yağmurlu görünüyor. Şemsiyenizi yanınıza alın."
        elif temperature < 15:
            return f"{city} için hava soğuk, kalın giysiler ve ceket önerilir."
        elif wind_speed > 20:
            return f"{city} için rüzgar çok kuvvetli, dikkatli olun ve sağlam giyinin."
        else:
            return f"{city} için hava oldukça güzel, rahat kıyafetlerle dışarı çıkabilirsiniz."

# Araçlar
weather_summarizer = WeatherSummarizer()
weather_advice = WeatherAdvice()

tools=[weather_summarizer, weather_advice]

agent = ConversationalAgent(prompt_node, tools=tools)

# Streamlit arayüzü
st.title("Hava Durumu ve Tavsiye Agent")
st.markdown("**Şehrinizin hava durumunu öğrenebilir ve tavsiyelere ulaşabilirsiniz.**")

city = st.text_input("Lütfen bir şehir adı girin:", "")

if city:
    # Hava durumu verisi için API'ye istek yapma
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric",
        "lang": "tr"
    }

    response = requests.get(weather_api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        rain_probability = data.get("rain", {}).get("1h", 0)
        wind_speed = data["wind"]["speed"]

        # Özetleme aracıyla hava durumu özeti
        weather_data = {
                          "city": city_name,
                           "temperature": temperature,
                          "weather_description": weather_description,
                         "wind_speed": wind_speed
                       }

        summary = weather_summarizer.run(weather_data)  # Şimdi doğru şekilde çağırabilirsiniz

        

        # Tavsiye aracıyla öneri oluşturma
        advice = weather_advice.run({
            "city": city_name,
            "temperature": temperature,
            "rain_probability": rain_probability,
            "wind_speed": wind_speed
        })

        # Sonuçları gösterme
        st.subheader("Hava Durumu Özeti")
        st.write(summary)

        st.subheader("Tavsiye")
        st.write(advice)

    else:
        st.error("Hava durumu verisi alınamadı, şehir adı doğru mu?")

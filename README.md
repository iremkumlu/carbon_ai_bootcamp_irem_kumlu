# carbon_ai_bootcamp_irem_kumlu

carbon ai bootcamp soru ve cevapları

# Task1 :
## Metin Özetleme
Bir dil modeli (Hugging Face Transformers gibi) kullanarak aşağıdaki işlemleri gerçekleştiren bir Python kodu yazıldı.
Hugging Face'ten alınan çnceden eğitilmiş Pegasus modelini (google/pegasus-xsum) kullanıldı.


# Task2 :
Haystack ve bir açık kaynaklı model kullanarak bir RAG sistemi tasarlandı.
## Türkçe Soru-Cevaplama Uygulaması (FastAPI ve Haystack ile)
- Bu proje, FastAPI ve Haystack kütüphanelerini kullanarak Türkçe metinler üzerinde soru-cevaplama yapabilen bir uygulama oluşturur. Önceden eğitilmiş "savasy/bert-base-turkish-squad" modelini kullanarak, verilen metin belgelerinden sorulara en uygun cevapları çıkarır. Ayrıca, Streamlit ile basit bir web arayüzü sunar.
- `Data` klasörü oluşturun ve içine `doc1.txt`, `doc2.txt`, ve `doc3.txt` adlı metin dosyalarınızı ekleyin. Bu dosyalar, uygulamanın cevapları arayacağı belgeleri içerecektir.
## Kullanım
1.  Backend(fast api) tarafını 'uvicorn task2_script:app --reload' komutunu terminalde çalıştırın.
2.  Sonrasında Streamlit arayüzünü tarayıcınızda açmak için 'streamlit run streamlit_app.py' komutunu terminalde çalıştırın.
3.  "Soru Sorun:" metin kutusuna sorunuzu girin.
4.  Uygulama, FastAPI arka ucu aracılığıyla Haystack işlem hattına sorunuzu gönderir.
5.  Haystack, ilgili belgeleri arar ve en uygun cevabı çıkarır.
6.  Cevap ve ilgili bağlam Streamlit arayüzünde görüntülenir.
7.  "output_task2 dosyasını indir" butonu ile soru ve cevabı içeren bir metin dosyası indirebilirsiniz.
  

# Task3 :
## Hava Durumu Özetleme ve Tavsiye Uygulaması 
Bir AI ajanı (agent) tasarlandı.
`weather_api_key` değişkenini kendi OpenWeatherMap API anahtarınızla değiştirin.
`weather_api_key = "7000de40458363ace6929e6573bc87d8"` 
## Kullanım
1- Terminalde 'streamlit run task3_script.py' komutunu çalıştırın.
2- Hava durumu özeti ve Tavsiye almak istediğin şehri yazın.


# Task4:
## İstanbul Gezi Asistanı (RAG Destekli)
Yeni bir RAG tabanlı uygulama veya LLM projesi tasarlayın açıklandı.
Bu proje, kullanıcılara kişiselleştirilmiş ve güncel İstanbul gezi tavsiyeleri sunan akıllı bir sistemdir. Retrieval Augmented Generation (RAG) yaklaşımını kullanarak, çeşitli güvenilir kaynaklardan elde edilen bilgileri bir araya getirir ve kullanıcının ilgi alanlarına, zaman kısıtlamalarına ve bütçesine göre özelleştirilmiş öneriler sunmaktadır.
## Teknolojiler

*   Sentence Transformers (`thenlper/gte-large`)
*   MongoDB (Vektör Arama)
*   Google Gemma (örn. `google/gemma-2b-it`)
  

# Task5:
Task 2 Docker compose file çalışabilecek şekle getirildi.

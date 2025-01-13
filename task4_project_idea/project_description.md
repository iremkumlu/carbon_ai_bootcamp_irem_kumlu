Uygulama ismi : İstanbul Gezi Asistanı (RAG Destekli)

a- Projenin amacı nedir?

Bu projenin amacı, kullanıcılara kişiselleştirilmiş ve güncel İstanbul gezi tavsiyeleri sunan akıllı bir
sistem geliştirmektir. Uygulama, kullanıcıların ilgi alanlarına, zaman kısıtlamalarına, bütçelerine ve diğer
tercihlerine göre özelleştirilmiş öneriler sunacaktır. Bunu yaparken, çeşitli güvenilir kaynaklardan
(güvenilir gezi blogları, resmi turizm siteleri, kullanıcı yorumları vb.) elde ettiği bilgileri kullanacaktır.
Kapsamlı ve kişiselleştirilmiş İstanbul Gezi Asistanı uygulaması sayesinde kullanıcılar, sordukları sorulara hızlı ve güvenilir cevaplar (tavsiyeler) alabileceklerdir.

b- Veriyi nasıl işleyeceksiniz?

Veri işleme süreci aşağıdaki adımları içerecektir:

1- Veri Toplama: Çeşitli kaynaklardan veriler toplanır.Örneğin, Wikivoyage XML verileri(ücretsiz erişime açık
bir çevrimiçi seyahat rehberi), İstanbul Büyükşehir Belediyesi web sitesi, TripAdvisor, gezi blogları,
haber siteleri vb. Bu veriler şunları içerecektir:

- Turistik yerler (tarihi mekanlar, müzeler, parklar vb.)
- Yemek ve Restoranlar
- Etkinlikler (konserler, sergiler, festivaller vb.)
- Ulaşım bilgileri (otobüs, metro, tramvay hatları, taksi durakları vb.)
- Konaklama yerleri (tarihi konaklar, oteller, pansiyonlar vb.)
- Kullanıcı yorumları ve değerlendirmeleri
- Hava durumu bilgileri

2- Veri Temizleme ve Ön İşleme: Toplanan veriler temizlenir, düzenlenir ve ön işleme yapılır. Bu, gereksiz karakterlerin temizlenmesini, verilerin standart bir formata dönüştürülmesini, eksik verilerin tamamlanmasını veya filtrelenmesi olacaktır. Aynı zamanda özetler çıkarılarak ve özellikle İstanbul şehri filtrelenir. Verilerin daha doğru bir şekilde işlenebilmesi için veri setinin anlamlı bir şekilde bölünmesi, etiketlenmesi veya gruplandırılma da yapılabilir.

c- LLM ve retrieval bileşenleri nasıl entegre olacak?

Kullanıcı, İstanbul gezisiyle ilgili bir sorgu girer (örneğin, "Ailemle gidebileceğim tarihi yerler", "En iyi Boğaz manzaralı restoranlar", "Hafta sonu etkinlikleri").
Kullanıcı sorgusu, bir embedding modeli olan Sentence Transformers kütüphanesindeki thenlper/gte-large modeline gönderilerek bir vektöre (embedding) dönüştürülür. Embedding modeli, metinleri anlamlarını koruyarak sayısal vektörlere dönüştürücektir."thenlper/gte-large" gibi önceden eğitilmiş modeller, metinleri anlamlı vektörlere dönüştürmek için yaygın olarak kullanılmaktadır.
Oluşturulan vektör, bir vektör veritabanı olan MongoDB'nin vektör arama özelliği ile saklanan belgelerin vektörleriyle karşılaştırılır. Vektör araması (vector search) ile sorgu vektörüne en yakın (en benzer) vektörlere sahip belgeler bulunur. En yakın 5 belge alınabilir. Aggregation framework kullanılarak vektör araması yapılır, böylece vektör benzerliğine dayalı bir arama yapılmış olunacaktır.
Vektör aramasından elde edilen en benzer belgeler, bir bağlam (context) oluşturmak için birleştirilir. Bu bağlam, LLM'ye sunulacak ek bilgileri içerir.Seçilen 5 belgenin metinleri birleştirilerek bir bağlam oluşturulur. Bu bağlam, kullanıcının sorgusuna doğrudan bir yanıt vermek için yetersiz olabilir, ancak LLM ile birleştiğinde anlamlı bir yanıt üretecektir.
Orijinal kullanıcı sorgusu ve oluşturulan bağlam, bir LLM olan Google Gemma'ya girdi olarak verilir. Özellikle google/gemma-2b-it gibi modeller, bağlama dayalı yanıtlar üretmek için uygun olduğu için seçilmiştir.
LLM, hem sorguyu hem de bağlamı analiz ederek kullanıcının sorgusuna uygun, tutarlı ve bilgilendirici bir yanıt üretecektir. Bu yanıt, gezi tavsiyeleri, önerilen rotalar, önemli bilgiler ve diğer ilgili detayları içerebilir. LLM, veritabanından gelen en uygun belgelerle desteklenen bu girişle, çok daha doğru ve özgün bir cevap üretecektir.
Özetle, MongoDB bir vektör veritabanı olarak kullanılarak retriever görevini görür. Kullanıcı sorgusuna en benzer belgeleri bulan MongoDB, bu belgeleri LLM'ye sunar ve LLM de bu bilgilere dayanarak daha doğru, güncel ve kişiselleştirilmiş yanıtlar üretir.

d- Bu proje hangi sorunu çözmeyi hedefliyor?

İnternette İstanbul hakkında çok fazla bilgi var ve kullanıcıların doğru ve güvenilir bilgileri bulması zor olabilir. Sistem, bilgileri tek bir yerde toplayarak ve düzenleyerek kullanıcıyı doğru ve güvenilir bir rehberlik hizmeti sunarak bu sorunu çözmektedir.Mevcut gezi rehberleri genellikle genel tavsiyeler sunar ve kullanıcıların bireysel ihtiyaçlarını ve tercihlerini dikkate almaz. İstanbul gezi rehberi, kişiselleştirilmiş tavsiyeler sunarak bu sorunu çözecektir.Ayrıca internetteki bazı gezi bilgileri eski olabilmektedir. Uygulama, veritabanını düzenli olarak güncelleyerek bu sorunu da çözmeyi hedeflemektedir. Aynı zamanda kullanıcıların gezi rotası belirleme, doğru
ve güvenilir mekanları tercih etme gibi konularda uzun araştırmalar yapmak yerine uygulamadan aldığı tavsiyeler sayesinde daha hızlı karar alabilmesini sağlayacaktır.

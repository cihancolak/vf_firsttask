# Docker ile Multi Contanier Proje 🐳


**Tam yığın projemize hoş geldiniz!** Bu depo, modern bir web uygulaması mimarisini şu şekilde göstermektedir:

🖥️ Backend Uygulama (app.py)

Backend uygulamamız Python'un Flask kütüphanesi kullanılarak geliştirilmiştir. Amacı, veritabanıyla etkileşim kurarak API uç noktaları üzerinden veri alışverişi sağlamaktır. İşte backend uygulamasının detayları:

Temel Özellikler:

    MySQL Veritabanı Entegrasyonu: MySQL veritabanıyla bağlantı kurarak veri ekleme, alma ve yönetme işlemlerini gerçekleştirir.
    CORS (Cross-Origin Resource Sharing) Desteği: Farklı kaynaklardan (örneğin, React frontend) gelen isteklere izin vermek için CORS etkinleştirilmiştir. Bu, frontend ve backend uygulamalarının farklı portlarda veya alanlarda çalışabilmesini sağlar.
    API Uç Noktaları:
        /: Backend'in çalıştığını doğrulamak için basit bir "Merhaba" mesajı döndürür.
        /test_db_connection: Veritabanı bağlantısını test etmek için kullanılır. Başarılı bir bağlantı durumunda "Connected to the database" mesajı, başarısızlık durumunda hata mesajı döndürür.
        /data: Veritabanındaki sample_table tablosuyla etkileşim kurar.
            GET İsteği: Tablodaki tüm verileri JSON formatında döndürür.
            POST İsteği: JSON formatında gelen name verisini tabloya ekler.

Çalışma Prensibi:

    Flask uygulaması başlatılır.
    CORS etkinleştirilir.
    /data uç noktasına bir GET isteği geldiğinde, MySQL veritabanına bağlanır ve sample_table tablosundaki tüm verileri çeker. Bu veriler JSON formatına dönüştürülerek frontend'e gönderilir.
    /data uç noktasına bir POST isteği geldiğinde, JSON formatında gönderilen name verisi alınır. Veritabanına bağlanılır ve bu veri sample_table tablosuna eklenir. İşlem başarılı olursa frontend'e "Data added successfully" mesajı gönderilir.
    Diğer uç noktalar (/ ve /test_db_connection) benzer şekilde çalışır.

Not: Veritabanı bağlantı bilgileri (host, kullanıcı adı, parola, veritabanı adı) ortam değişkenleri (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) aracılığıyla sağlanır. Bu, güvenlik açısından önemlidir ve Docker Compose dosyasında bu değişkenleri tanımlamanızı sağlar.

Docker Entegrasyonu:

Bu backend uygulaması Dockerize edilmiştir. Yani, Docker konteyneri içinde çalışacak şekilde tasarlanmıştır. Bu sayede uygulama, farklı ortamlarda tutarlı bir şekilde çalışabilir ve bağımlılık sorunları ortadan kalkar. Dockerfile dosyası, backend uygulamasının Docker imajını oluşturmak için gerekli talimatları içerir.

Geliştirme:

Backend uygulamasını geliştirmek için, Docker Compose kullanarak konteynerleri başlatabilir ve değişiklikleri gerçek zamanlı olarak görebilirsiniz. Gerekirse, veritabanı şemasını veya API uç noktalarını güncelleyebilirsiniz.




- **Backend:** Python (Flask), veri kalıcılığı için MySQL
- **Frontend:** Dinamik kullanıcı arayüzleri için React
- **Docker:** Konteynerleştirme ile geliştirme ve dağıtımı kolaylaştırır
- **Veritabanı:** Kalıcı depolama için MySQL kullanır.

## 🚀 Hızlı Başlangıç Rehberi

1. **Gereksinimler:**
   - **Docker:** Docker ve Docker Compose'un yüklü olduğundan emin olun.
   - **Node.js ve npm (veya yarn):** Ön uç kurulumu için gereklidir.

2. **Depoyu Klonlayın:**
   ```bash
   git clone https://projenizin-depo-adresi.git
   cd proje-adınız


Docker Compose.yaml dosyamin aciklamasi 
```
1. Version:
Dosya, Docker Compose'un 3. sürümünü kullanacağını belirtir. Bu sürüm yaygın olarak kullanılır ve birçok özellikle uyumludur.

2. Services:
Bu bölümde, projenin farklı parçalarını temsil eden servisler (backend, frontend, database) tanımlanır.

    Backend:
        Python Flask ile yazılmış backend uygulamasının nasıl oluşturulacağını belirtir (backend klasöründeki Dockerfile kullanarak).
        Backend'in 5000 numaralı portu kullanacağını ve bu portu bilgisayarınızdaki 5000 numaralı porta bağlayacağını belirtir.
        Backend'in ihtiyaç duyduğu çevre değişkenlerini (veritabanı bağlantı bilgileri) ayarlar.
        Backend'in veritabanı servisine bağlı olduğunu belirtir, yani veritabanı çalışmadan backend başlamaz.
    Frontend:
        React ile yazılmış frontend uygulamasının nasıl oluşturulacağını belirtir (frontend klasöründeki Dockerfile kullanarak).
        Frontend'in 3000 numaralı portu kullanacağını ve bu portu bilgisayarınızdaki 3000 numaralı porta bağlayacağını belirtir.
        Frontend'in backend'e nasıl bağlanacağını belirten bir çevre değişkeni ayarlar.
    Database:
        MySQL 8.0 veritabanı kullanılacağını belirtir.
        Veritabanının root kullanıcısı için parolayı ve oluşturulacak veritabanının adını ayarlar.
        Veritabanının 3306 numaralı portu kullanacağını ve bu portu bilgisayarınızdaki 3306 numaralı porta bağlayacağını belirtir.
        Veritabanı verilerinin kalıcı olarak saklanması için bir volume (db_data) oluşturur.
        Veritabanı ilk başladığında çalıştırılacak SQL komutlarını içeren bir dosyayı belirtir (database/init.sql).

3. Volumes:
Bu bölümde, veritabanı verilerini kalıcı olarak saklamak için kullanılan bir volume tanımlanır (db_data). Bu sayede konteyner silinse bile veriler kaybolmaz.

```

docker-compose up --build


    Uygulamaya Erişim:
        Frontend: Tarayıcınızda http://localhost:3000 adresini açın.
        Backend: Backend API'si http://localhost:5000 adresinde mevcuttur.
        Veritabanı: MySQL veritabanına localhost:3306 adresinden erişilebilir (kullanıcı adı olarak root ve parola olarak rootpassword kullanın).

📂 Proje Yapısı

    backend: Flask uygulama mantığını, veritabanı etkileşimini ve API uç noktalarını içerir.
        Dockerfile
        app.py (ana Flask uygulaması)
        requirements.txt (Python bağımlılıkları)
    frontend: Kullanıcı arayüzünden sorumlu React ön uç kodunu tutar.
        Dockerfile
        package.json (JavaScript bağımlılıkları)
        public/ (statik varlıklar)
        src/ (React bileşenleri ve kaynak kodu)
    database: MySQL veritabanı kurulumunu ve başlatma komut dosyalarını içerir.
        Dockerfile
        init.sql (ilk veritabanı şeması)
    docker-compose.yaml: Dockerize edilmiş geliştirme için servisleri, ağları ve birimleri tanımlar.


    Kodu Değiştirin: Gerektiğinde backend, frontend veya veritabanında değişiklik yapın.
    Docker Compose ile Yeniden Oluşturun: Değişiklikleri uygulamak ve konteynerleri yeniden oluşturmak için docker-compose up --build komutunu çalıştırın.
    Test Edin: Frontend, backend API uç noktalarını ve veritabanı etkileşimlerini test etmek için tercih ettiğiniz araçları kullanın.




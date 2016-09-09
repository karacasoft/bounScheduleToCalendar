#Gereksinimler

* Linux (Ben ArchLinux üzerinde çalıştırdım. Diğer linux'lar üzerinde de çok rahat çalışacağından eminim)
* Python 2.7 (3 desteklenmiyor.(sanırım))
* BeautifulSoup4
* Google API Python Client

Son ikisini yüklemek için bi install script ekledim. Onun çalışması için "pip" gerekiyor. O var mı diye kontrol etmek için "pip -V" diye yazın command line'a. Çalışmazsa kendi linux dağıtımınız için pip yüklemeyi araştırın.

İşletim sisteminiz python 2.7 çalıştırmak için command line'a "python2" yazılmasını gerektiriyorsa (benimki gibi) registrationToGoogle.py dosyasının ilk satırını şununla değiştirebilirsiniz.

 #!/usr/bin/env python2

"python2"yi işletim sisteminizin istediği kelime ile değiştirebilirsiniz.

#Kullanım

Adım adım anlatıyorum. Hiç bi aşamada bi eksiğiniz olmadığından emin olursanız sorun yok.

* Yeni bi klasör açalım (Adı fark etmez). İndirdiğimiz tüm dosyaları buraya atalım.
* Repository'deki registrationToGoogle.py dosyasını indirelim.
* Öncelikle registration sayfamıza girip programımızın sayfasını bilgisayarımıza kaydediyoruz. Sayfanın sadece .htm dosyası önemli. Diğer dosyaları çöpe atabiliriz. İndirilen dosyanın adını registrationPage.htm şeklinde değiştirelim.
saveProgramSS image/png
* Şimdi Google'dan onun serverlarına bağlanabilmemiz için bi anahtar almamız lazım.
- https://console.developers.google.com/ bu siteye giriyoruz.
- Buradan yeni bir proje açıyoruz. Proje adı herhangi bi şey olabilir. Hiç önemli değil.
newProjectSS image/png
- Projenin oluşturulmasını beklerken çayımızdan bir yudum alıyoruz.
- Sonra bulduğumuz ilk arama kısmına Calendar yazıyoruz. Karşımıza çıkan ilk "Google Calendar API" linkine tıklıyoruz.
- Bu düğmeden API kullanımını aktive ediyoruz.
enableAPISS image/png
- Güzel. Şimdi anahtarları alsak fena olmaz. Soldaki menüde "Credentials"ı seçiyoruz.
- Burada yukarıdaki sekmelerden "OAuth consent screen"'e basıp gelen ekranda "Product name shown to users" kısmını herhangi bir şeyle dolduralım. (Sonradan anahtar oluştururken bunu istiyor.)
- Şimdi bir önceki sekmeye("Credentials") geri dönüp "Create credentials"a basalım.
- Açılan menüde "OAuth Client ID" seçelim. Application type'ımız "Other". Other'ı seçip "Create"e basalım.
createCredentialSS image/png
- Gelen pencereyi "OK" deyip kapatalım.
- Oluşturduğumuz anahtara tıklayıp yukarıdaki "Download JSON" düğmesine tıklayalım. Bu bizim uygulamamızın Google ile olan kapısının anahtar dosyası. Önemli bi dosya yani kendi dosyamı paylaşmamamın bi nedeni var. Sizin de paylaşmamanızı tavsiye ediyorum.
- Bu dosyayı script ile aynı klasöre koyup adını "client_secret.json" diye değiştiriyoruz.
- Tamamdır. Her şey hazır. Artık scripti çalıştırabiliriz.
- Command line üzerinde "./registrationToGoogle.py" yazarak scripti çalıştırıyoruz.

#Hatalar

* Hataları buraya issue olarak açarsanız sevinirim. Takibi daha kolay olur bu şekilde.

#Sıkça sorulacağını düşündüğüm sorular

S: Hocam bunun kullanımı biraz gereksiz derecede uzun?
C: İstersen elle teker teker girebilirsin dersleri. Bunu son kullanıcı ürünü olarak çıkarmadım zaten açıkçası. Ama birileri düzenleyip biraz daha güzel özellikler eklerse diye kodu buraya atıyorum.

S: Ben Google hesabım ile girdim. Şimdi başka bi hesapla giriş yapamıyorum.
C: ~/.credentials klasörünü sil. Uygulamayı tekrar çalıştır.

S: Conflict'ler işlenmiyor?
C: Evet. Öyle...

S: Bu şeyde bi hata çıktı ve şu an benim Google takvimim berbat oldu.
C: Sorun yok. Bunun için program yeni bir takvim oluşturup tüm yazacaklarını oraya yazıyor. Solda My Calendars kısmında BOUN Dersler isminde bi takvim olacak. Onu silerek tüm oluşan saçmalıkları silebilirsiniz.

S: Bilgisayarım programın sayesinde kendine ait bir bilince sahip oldu.
C: Harika!

S: Şu an insanlığı yok etmek için planlar yapıyor.
C: Bi kapatıp aç. Düzelir o.

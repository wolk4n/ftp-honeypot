# 📖 FTP Honeypot Projesi

Bu proje, FTP sunucusuna yönelik saldırıları tespit etmek ve analiz etmek amacıyla bir honeypot oluşturur. Honeypot, saldırganların ilgisini çekmek için çeşitli sahte dosyalar içerir ve sunucu üzerindeki aktiviteleri loglar. Bu sayede hiçbir veri kaybetmeden potansiyel kötü niyetli kişiler hakkında bilgi toplanmış olur ve ona göre güvenlik politikaları geliştirilir.

## Özellikler

- **FTP Sunucusu:** FTP protokolü üzerinden bağlantıları kabul eder.
- **Sahte Dosyalar:** Saldırganların ilgisini çekmek için çeşitli sahte dosyalar içerir.
- **Kullanıcı Loglama:** FTP sunucusuna yapılan girişleri ve komutları loglar.
- **Dinamik Komut İşleme:** Gelen FTP komutlarını dinamik olarak işleyip yanıt verir.


## ⚙️ Kurulum

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

```bash
git clone https://github.com/wolk4n/ftp-honeypot.git
cd ftp-honeypot
chmod +x install.sh
./install.sh
python honeypot.py
```
Adımları tamamladıktan sonra tek yapılması gerekilen ilgili ftp sunucusuna bağlanmak olacaktır. Sahte kullanıcı bilgileri aşağıdaki gibidir:
```bash
username: user
password: 12345
```

## Video
eklenecek

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

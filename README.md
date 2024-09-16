# 📖 FTP Honeypot Projesi

Bu proje, FTP sunucusuna yönelik saldırıları tespit etmek ve analiz etmek amacıyla bir honeypot oluşturur. Honeypot, saldırganların ilgisini çekmek için çeşitli sahte dosyalar içerir ve sunucu üzerindeki aktiviteleri loglar. Bu sayede hiçbir veri kaybetmeden potansiyel kötü niyetli kişiler hakkında bilgi toplanmış olur ve ona göre güvenlik politikaları geliştirilir.

## ✨ Özellikler

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

## 🎬 Video
Bu proje hakkında daha fazla bilgi almak ve nasıl çalıştığını görmek için hazırladığım videoyu izleyebilirsiniz:
[![Session Hijacking Demo](https://www.imagevisit.com/images/2024/08/28/MR-ROBOT-1.png)](https://youtu.be/yBi4q-8B-nQ)


## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

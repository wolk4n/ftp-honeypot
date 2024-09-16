# FTP Honeypot Projesi

Bu proje, FTP sunucusuna yönelik saldırıları tespit etmek ve analiz etmek amacıyla bir honeypot oluşturur. Honeypot, saldırganların ilgisini çekmek için çeşitli sahte dosyalar içerir ve sunucu üzerindeki aktiviteleri loglar.

## Özellikler

- **FTP Sunucusu:** FTP protokolü üzerinden bağlantıları kabul eder.
- **Sahte Dosyalar:** Saldırganların ilgisini çekmek için çeşitli sahte dosyalar içerir.
- **Kullanıcı Loglama:** FTP sunucusuna yapılan girişleri ve komutları loglar.
- **Dinamik Komut İşleme:** Gelen FTP komutlarını dinamik olarak işleyip yanıt verir.

## Başlangıç

### Gereksinimler

- Python 3.9 veya üstü
- `pyftpdlib` Python kütüphanesi

### Kurulum

Projeyi yerel makinenize klonlayın:

```bash
git clone https://github.com/<kullanıcı-adı>/ftp-honeypot.git
cd ftp-honeypot

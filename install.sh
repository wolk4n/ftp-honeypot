echo ' __  __     ______     __   __     ______     __  __     ______   ______     ______  
/\ \_\ \   /\  __ \   /\ "-.\ \   /\  ___\   /\ \_\ \   /\  == \ /\  __ \   /\__  _\ 
\ \  __ \  \ \ \/\ \  \ \ \-.  \  \ \  __\   \ \____ \  \ \  _-/ \ \ \/\ \  \/_/\ \/ 
 \ \_\ \_\  \ \_____\  \ \_\\"\_\  \ \_____\  \/\_____\  \ \_\    \ \_____\    \ \_\ 
  \/_/\/_/   \/_____/   \/_/ \/_/   \/_____/   \/_____/   \/_/     \/_____/     \/_/ 
                                                                                     
                                                  
			.:: WELCOME TO FTP HONEYPOT TOOL ::.
			  Coded By wolkan - GitHub: wolk4n
			     [ Instagram: wolkansec ]
			       [ YouTube: wolkann ]
    '
echo "[!] Additional packages preparing.."
echo "[!] Additional packages downloading..."
mkdir "/ftp_honeypot_dir/"
wget https://github.com/wolk4n/ftp-honeypot/blob/main/ftp_dir/passwords.txt -P /ftp_honeypot_dir/
wget https://github.com/wolk4n/ftp-honeypot/blob/main/ftp_dir/important_contacts.csv -P /ftp_honeypot_dir/
wget https://github.com/wolk4n/ftp-honeypot/blob/main/ftp_dir/id_rsa -P /ftp_honeypot_dir/
wget https://github.com/wolk4n/ftp-honeypot/blob/main/ftp_dir/database.sql -P /ftp_honeypot_dir/
wget https://github.com/wolk4n/ftp-honeypot/blob/main/ftp_dir/backup_2024_08_17.log -P /ftp_honeypot_dir/
wget https://github.com/wolk4n/ftp-honeypot/blob/main/ftp_dir/access.log -P /ftp_honeypot_dir/
apt install python3 -y
pip install --upgrade pip
pip install pyftpdlib
pip install socket
pip install logging
echo "[+] Additional packages succesfully downloaded"
echo "[+] Tool ready for use"

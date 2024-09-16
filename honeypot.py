import socket
import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('honeypot.log')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/ftp_honeypot_dir", perm="elradfmw")
authorizer.add_anonymous("/ftp_honeypot_dir")

def banner():
    print(""" __  __     ______     __   __     ______     __  __     ______   ______     ______  
/\ \_\ \   /\  __ \   /\ "-.\ \   /\  ___\   /\ \_\ \   /\  == \ /\  __ \   /\__  _\ 
\ \  __ \  \ \ \/\ \  \ \ \-.  \  \ \  __\   \ \____ \  \ \  _-/ \ \ \/\ \  \/_/\ \/ 
 \ \_\ \_\  \ \_____\  \ \_\\"\_\  \ \_____\  \/\_____\  \ \_\    \ \_____\    \ \_\ 
  \/_/\/_/   \/_____/   \/_/ \/_/   \/_____/   \/_____/   \/_/     \/_____/     \/_/ 
                                                                                     
                                                  
			.:: WELCOME TO FTP HONEYPOT TOOL ::.
			  Coded By wolkan - GitHub: wolk4n
			     [ Instagram: wolkansec ]
			       [ YouTube: wolkann ]
    """)

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address


def log_login(handler, username, password):
    logging.info(f"Login Attempt -> Username: {username}, Password: {password}")


class CustomFTPHandler(FTPHandler):

    def log_command(self, command, arg):
        if arg:
            logging.info(f"User Command: {command} {arg}")
        else:
            logging.info(f"User Command: {command}")
        
    def process_command(self, cmd, arg):
        self.log_command(cmd, arg)
        super().process_command(cmd, arg)

    def ftp_PASS(self, password):
        log_login(self, self.username, password)
        super().ftp_PASS(password)

handler = CustomFTPHandler
handler.authorizer = authorizer
handler.banner = "Private FTP Server - Do Not Enter!"

address = ('0.0.0.0', 21)
server = FTPServer(address, handler)

ip_address = get_ip_address()
banner()
logging.info(f"FTP Server is Startig on {ip_address}")
server.serve_forever()

import imaplib
import email
from email.header import decode_header
import base64
#from bs4 import BeautifulSoup
import re
from configparser import ConfigParser

urlsconf ='config/config.ini'
config =ConfigParser() 
config.read(urlsconf) 

mail_pass = config['login_mail_ru']['mail_pass'] 
username = config['login_mail_ru']['username']
imap_server = "imap.mail.ru"
imap = imaplib.IMAP4_SSL(imap_server)
print(imap.login(username, mail_pass))

# imap.list()
# folders = imap.list()
# print(folders)
# for folder in folders[1]:
#     print(folder)

print(imap.select(b"&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"))

# ddate = '12-December-2022'
# result, data = imap.uid('search', None, '(SENTON %s)' % ddate)
# print(data)
#imap.uid()

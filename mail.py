import imaplib
import email
from email.header import decode_header
import base64
#from bs4 import BeautifulSoup
from configparser import ConfigParser
import asyncio

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
# for folder in folders[1]:
#     print(folder)
def read_mails(count_mails):
    last_mails = list()
    for i in range(count_mails-15, count_mails):
        res, msg = imap.fetch(f'{i}'.encode(), '(RFC822)')  #Для метода search по порядковому номеру письма
        msg = email.message_from_bytes(msg[0][1])
    
        letter_subject = msg["Subject"]
        last_mails.append(decode_header(letter_subject)[0][0].decode())
    return last_mails
# Подклбчение к папке Отправленные
sent_emails = (imap.select(b"&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"))
count_mails = int(sent_emails[1][0].decode("utf-8"))
received_mail = read_mails(count_mails)
for i in received_mail:
    print(i)

# letter_date = email.utils.parsedate_tz(msg["Date"]) # дата получения, приходит в виде строки, дальше надо её парсить в формат datetime
# letter_id = msg["Message-ID"] #айди письма
# letter_from = msg["Return-path"] # e-mail отправителя
# print(letter_date)
# print(type(letter_date), type(letter_id), letter_id, type(letter_from))
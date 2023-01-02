import imaplib
import email
import base64
from email.header import decode_header 
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
# for folder in folders[1]:
#     print(folder)
def read_mails(count_mails):
    last_mails = list()
    text_mails = list()
    for i in range(count_mails, count_mails-5, -1):
        res, msg = imap.fetch(f'{i}'.encode(), '(RFC822)')  
        msg = email.message_from_bytes(msg[0][1]) # Извлекаем часть с содержанием
        letter_subject = msg["Subject"] # Извлекаем тему сообщения в кодеровке
        subject = decode_header(letter_subject)[0][0].decode() # Декодируем в текст
        first_word_subject = subject[:subject.find(" ")] # Вырезаем первое слово из содержания
        if first_word_subject == "Отчет": # При совпадении перовго слова со словом "Отчет", выходим из цикла
            break
        last_mails.append(subject) # Добавляю запись в список

        for part in msg.walk():
            if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                text = base64.b64decode(part.get_payload()).decode()
                text_mails.append(text)   

    return last_mails, text_mails  # Возвращаю список писем за сегодня и текст писем

# Подключение к папке "Отправленные"
sent_emails = (imap.select(b"&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"))
count_mails = int(sent_emails[1][0].decode("utf-8"))
print(count_mails)
received_mails_subjects, recieved_mails_texts = read_mails(count_mails) 

# Создаю список названий магазинов из полученного списка названий отчетов
name_stores = list()
for i in received_mails_subjects:
    if i.find(",", 0, 11) == -1:
        name_store = i[:i.find(" ")]
    else:
        name_store = i[:i.find(",")]
    name_stores.append(name_store)

# Создаю список названий адресов из полученного списка названий отчетов
name_streets = list()
for i in received_mails_subjects:
    name_street = i[i.find(" "):i.rfind(",")]
    name_streets.append(name_street)

# Создаю список комментариев из полученного списка текстов писем
comment_mails = list()
for i in recieved_mails_texts:
    i = i.replace("С уважением Селин Денис", "")
    i = i.replace("\n", "")
    comment_mails.append(f"{i}\n")

for com in comment_mails:
    print(com)

# letter_date = email.utils.parsedate_tz(msg["Date"]) # дата получения, приходит в виде строки, дальше надо её парсить в формат datetime
# letter_id = msg["Message-ID"] #айди письма
# letter_from = msg["Return-path"] # e-mail отправителя
# print(letter_date)
# print(type(letter_date), type(letter_id), letter_id, type(letter_from))
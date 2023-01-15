import imaplib
import email
import base64
from configparser import ConfigParser
from email.header import decode_header 

def connection():
    urlsconf ='src/config/config.ini'
    config =ConfigParser() 
    config.read(urlsconf) 

    mail_pass = config['login_mail_ru']['mail_pass'] 
    username = config['login_mail_ru']['username']
    imap_server = config['imap_server']['imap_server']
    imap = imaplib.IMAP4_SSL(imap_server)
    sts, res = imap.login(username, mail_pass)
    if sts == "OK":
        return imap
    else:
        return False

def read_mails(count_mails, imap):
    last_mails = list()
    text_mails = list()
    for i in range(count_mails, count_mails-16, -1):
        res, msg = imap.fetch(f'{i}'.encode(), '(RFC822)')  
        msg = email.message_from_bytes(msg[0][1]) # Извлекаем часть с содержанием
        letter_subject = msg["Subject"] # Извлекаем тему сообщения в кодеровке
        subject = decode_header(letter_subject)[0][0].decode() # Декодируем в текст
        first_word_subject = subject[:subject.find(" ")] # Вырезаем первое слово из содержания
        print(first_word_subject)
        if first_word_subject == "Отчет": # При совпадении первого слова со словом "Отчет", выходим из цикла
            break
        last_mails.append(subject) # Добавляю запись в список

        for part in msg.walk():
            if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                text = base64.b64decode(part.get_payload()).decode()
                text_mails.append(text)   

    return last_mails, text_mails  # Возвращаю список писем за сегодня и текст писем

def extract_store_names(subject):
    # Создаю список названий магазинов из полученного списка названий отчетов
    name_stores = list()
    for i in subject:
        if i.find(",", 0, 12) == -1:
            name_store = i[:i.find(" ")]
        else:
            name_store = i[:i.find(",")]
        name_stores.append(name_store)
    
    return name_stores

def extract_street_names(subject):     
    # Создаю список названий адресов из полученного списка названий отчетов
    name_streets = list()
    for i in subject:
        name_street = i[i.find(" "):i.rfind(",")]
        name_streets.append(name_street)

    return name_streets   

def extract_message_body(text_body):
    # Создаю список комментариев из полученного списка текстов писем
    comment_mails = list()
    for i in text_body:
        i = i.replace("С уважением Селин Денис", "")
        i = i.replace("\n", "")
        comment_mails.append(f"{i}\n")

    return comment_mails
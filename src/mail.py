import sys
import modules_of_mail

def mail_parse():
    imap = modules_of_mail.connection()
    if not imap:
        sys.exit()

    # Подключение к папке "Отправленные"
    sent_emails = (imap.select(b"&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"))
    count_mails = int(sent_emails[1][0].decode("utf-8"))
    received_mails_subjects, recieved_mails_body = modules_of_mail.read_mails(count_mails, imap) 

    name_stores = modules_of_mail.extract_store_names(received_mails_subjects)
    name_streets = modules_of_mail.extract_street_names(received_mails_subjects)
    message_body = modules_of_mail.extract_message_body(recieved_mails_body)

    return name_stores, name_streets, message_body


from imap_tools import MailBox, MailMessage

# fetch only: SUBJECT, DATE, UID
with MailBox('imap.mail.com').login('test@mail.com', 'pwd') as mailbox:
    for msg in mailbox.fetch(message_parts='(BODY.PEEK[HEADER.FIELDS (SUBJECT DATE)] UID)'):
        print(msg.uid, msg.subject, msg.date_str)
        print(msg.from_ or '-no from_')  # empty
        print(msg.flags or '-no flags')  # empty
        print(msg.text or '-no text')  # empty
        print()

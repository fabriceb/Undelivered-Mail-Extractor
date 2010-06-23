import imaplib
imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
imap.login('fabrice.bernhard@gmail.com','XXXXXXXX')
mboxes = imap.list()[1]
imap.select("Undelivered Mail")
uids = imap.search(None,"(SINCE 23-Jun-2010)")
uids = uids[1][0].split(' ')
emails = []
for uid in uids:
    body = imap.fetch(uid,'(UID BODY[TEXT])')
    text = body[1][0][1]
    m = re.search(r"To: ([^\s]+)", text)
    emails.append(m.group(1))

print emails

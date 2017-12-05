import imaplib

imap = imaplib.IMAP4_SSL('imap.gmail.com')
imap.login('dchkang83', 'password1')
imap.select('inbox')
imap.uid('search', None, 'ALL')




result, data = imap.uid('search', None, 'ALL')

imap.close()
imap.logout()

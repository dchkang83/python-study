import imap
import imaplib
import logging
import smtp
import smtplib
from email.message import EmailMessage


logging.basicConfig(filename='remote_job_log.txt', format='%(asctime)s - %(levelname)s - %(message)s')

# Configure the program by setting some variables.
MY_EMAIL = 'asweigart@gmail.com'    # bot should only respond to me
BOT_EMAIL = 'imatest@coffeeghost.net'
BOT_EMAIL_PASSWORD = 'PASSWORD'
TORRENT_PROGRAM = 'C:\\Program Files (x86)\\qBittorrent\\dbittorrent.exe'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465


def check_and_get_instruction_email():
    # 로그인 imap
    logging.debug('Connecting to IMAP server..')
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    logging.debug('Connected.')

    result, data = imap.select('inbox')

    # 명령관련 모든 메일을 가져온다.
    instructions = []

    # 메일이 없으면 빈 배열을 리턴턴
    if data[0].decode('utf-8') == '0':
        logging.debug('No mail founded..')
        return instructions

    result, data = imap.uid('search', None, '(HEADER Subject "instruction")')
    uids = data[0].split()

    for target_uid in uids:
        result, data = imap.uid('fetch', target_uid, '(RFC822)')
        raw_message = data[0][1]
        email_message = email_message_from_string(raw_message.decode('utf-8'))

        # 메일에서 본문을 추출한다.
        if email_message.is_multipart():
            payload = email_message.get_payload()[0]
            instructions.append(payload.get_payload().strip())
        else:
            instructions.append(email_message.get_payload().strip())

        # 명령어를 추출한 이메일은 삭제한다.
        imap.uid('store', target_uid, '+FLAGS', '(\\Deleted)')
        imap.expunge()

    # 로그아웃
    imap.close()
    imap.logout()

    return instructions

def do_instruction(instruction):

    # 명령어를 분석하여 처리한다.
    subprocess.Popen(TORRENT_PROGRAM + ' ' + instruction)   # 토렌트 프로그램 수행

    # 작업내용 메일 메세지를 작성한다.
    msg = EmailMessage()
    msg['Subject'] = '작업완료 내용'
    msg['From'] = BOT_EMAIL
    msg['To'] = 'recipient@mail.co.kr'
    msg.set_content('''
    다음과 같이 작업이 수행되었습니다.
    {} {}
    좋은하루 되세요.
    '''.format(TORRENT_PROGRAM, instruction))

    # 작업 수행 후 작업내용 메일을 보낸다.
    logging.debug('Connecting to SMTP server at {} to send confirmation email...'.format(SMTP_SERVER))
    smtp.smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.ehlo()
    smtp.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    logging.debug('Connected.')
    smtp.send_message(msg)
    loging.debug('Confirmation email send.')
    smtp.quit()


def main():
    # 매 15분마다 메일을 체크하여 무한 루프를 돈다.
    print('Email bot started. Press Ctrl-C to quit.')
    logging.debug('Email bot started.')

    while True:
        try:
            logging.debug('Getting instructions from email...')
            instructions = check_and_get_instruction_email()

            for instruction in instructions:
                logging.debug('Doing instruction: ' + instruction)
                do_instruction(instruction)
        except Exception as err:
            logging.error(err)



if __name__ == '__main__':
    main()

import smtplib
import email.mime.multipart
import email.mime.text
import time

def sleeptime(min,sec):
    return min*60+sec;
second = sleeptime(0,10);
while 1 == 1:
    time.sleep(second);
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = '13218852211@163.com'
    msg['to'] = '2584465565@qq.com'
    msg['subject'] = 'test'
    content = '''''
    你好，
        这是一封自动发送的邮件。

        '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')
    smtp.login('13218852211@163.com', '607412mei')
    smtp.sendmail('13218852211@163.com', '2584465565@qq.com', str(msg))
    smtp.quit()
import requests, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail(results):
    send_email = "ataproject21@gmail.com"
    send_pw = "new!1234new"

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(send_email, send_pw)
    receive_emails = ['ahhyeon.lee@kt.com']

    for receive in receive_emails:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "[공유] 테스트 자동화 결과 내용 공유"
        msg['From'] = send_email
        msg['To'] = receive
        part1 = MIMEText(makeHTML(results), 'html')
        msg.attach(part1)
        s.sendmail(send_email, receive, msg.as_string())
        s.quit()

def makeHTML(results):
    str = ""
    for result in results : 
        str += """<p style="padding:5px 0 0 0;">▷ 테스트 케이스명 : """ + result[0] + """</p>
         <table style="margin: 10px 0 10px 0;" border="1" cellpadding="0" cellspacing="0" width="40%"> 
            <tr>
                <td style="padding: 10px;" align="center">케이스</td>
                <td style="padding: 10px;" align="center">결과</td>
            </tr>"""
        for case in result[1] : 
            str += """<tr> <td style="padding: 10px;" align="center">""" + case[0] + """</td> <td style="padding: 10px;" align="center">""" + case[1] + """</td></tr>"""
        str += """</table>"""

    html = """\
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>테스트 자동화 결과 메일</title>
    </head>
    <body>
        <h4>테스트 자동화 결과 내용 공유</h4>
        <p style="padding:5px 0 0 0;">안녕하세요. 테스트 자동화 수행 내용 공유드립니다.</p>
        """ + str + """
    </body>
    </html>
    """
    return html
   

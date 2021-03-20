from flask import render_template, Flask
from flask_mail import Message
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from flask import Flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)


class Register:

    def __init__(self, request, dbconnection, mail):
        self.con = dbconnection
        self.request = request
        self.mail = mail
        self.city = self.request.form.get('city')
        self.platform = self.request.form.get('socialMedia')
        self.rows = self.checkDataExist(self.city, self.platform)
        print(self.rows)

    def checkDataExist(self, city, platform):
        print(city)
        query = "SELECT emailId  FROM cyber_email WHERE cityOrState = '" + city + "'"

        # '" + email + "'"
        with self.con:
            cur = self.con.cursor()
            # cur.execute("SELECT *  FROM Logindata WHERE email = (?) " , (email,))
            cur.execute(query)
            rows = cur.fetchone()
            # print(cur)
            email = rows[0]
            print(rows[0])
        print(self.sendMessage(email, city, platform))
        return rows[0]

    def sendMessage(self, email, city, platform):
        # sender_email="codent1330@gmail.com"
        # receiver_email=[email]
        #
        # msg = MIMEMultipart()
        # msg['Subject'] = '[Email Test]'
        # msg['From'] = sender_email
        # msg['To'] = receiver_email
        #
        # msgText = MIMEText('<b>%s</b>' % (city), 'html')
        # msg.attach(msgText)
        #
        #
        # with open(r"C:\Users\anjuv\OneDrive\Desktop\hacknitr\image.png", 'rb') as fp:
        #     img = MIMEImage(fp.read())
        #     img.add_header('Content-Disposition', 'attachment', filename="image.png")
        #     msg.attach(img)
        #
        # try:
        #     with smtplib.SMTP('smtp.gmail.com.', 587) as smtpObj:
        #         smtpObj.ehlo()
        #         smtpObj.starttls()
        #         smtpObj.login("codent1330@gmail.com", "bhuvanmin")
        #         smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
        # except Exception as e:
        #     print(e)


        mail_msg = Message('Cyber Crime Report', sender='codent1330@gmail.com', recipients=[email])
        # element=r"C:\Users\anjuv\OneDrive\Desktop\hacknitr\static\image.png"
        mail_msg.html = render_template('sent.html', city=city, platform=platform,  _external=True)
        # with open(r"C:\Users\anjuv\OneDrive\Desktop\hacknitr\static\image.png", "rb") as fp:
        #     maintype, subtype = attachment.content_type.split('/')
        #     mail_msg.attach("image.png", "static", fp.read())
        # # mail_msg.attach('image.png', 'static', open(join(mail_blueprint.static_folder, 'image.png'), 'rb').read(),
        # #            'inline', headers=[['Content-ID', '<Myimage>'], ])
        # with open(r"C:\Users\anjuv\OneDrive\Desktop\hacknitr\image.png", 'rb') as fp:
        #     img = MIMEImage(fp.read())
        #     img.add_header('Content-Disposition', 'attachment', filename="image.png")
        #     mail_msg.attach(img)
        self.mail.send(mail_msg)
        return 'ok'


if __name__ == "__main__":
    app.run(debug=True)

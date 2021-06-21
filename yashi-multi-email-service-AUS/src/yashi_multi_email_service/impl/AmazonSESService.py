from .EmailManager import EmailManager
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class AmazonSESService(EmailManager):
	"""AWS SES Service implementation to send email"""
	USERNAME_SMTP = None
	PASSWORD_SMTP = None

	HOST = "email-smtp.ap-south-1.amazonaws.com"
	PORT = 587

	SENDER = None
	SENDERNAME = None

	def __init__(self, config):
		self.USERNAME_SMTP = config.get("USERNAME_SMTP")
		self.PASSWORD_SMTP = config.get("PASSWORD_SMTP")
		self.SENDER = config.get("FROM_EMAIL")
		self.SENDERNAME = config.get("FROM_EMAIL_NAME")
		
	def send_email(self, context):
		msg = MIMEMultipart('alternative')
		msg['Subject'] = context.get("subject")
		msg['From'] = email.utils.formataddr((self.SENDERNAME, self.SENDER))
		msg['To'] = context.get("to_email")

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(context.get("body_text"), 'plain')
		msg.attach(part1)

		# Try to send the message.
		try:  
		    server = smtplib.SMTP(self.HOST, self.PORT)
		    server.ehlo()
		    server.starttls()
		    #stmplib docs recommend calling ehlo() before & after starttls()
		    server.ehlo()
		    server.login(self.USERNAME_SMTP, self.PASSWORD_SMTP)
		    res = server.sendmail(self.SENDER, context.get("to_email"), msg.as_string())
		    server.close()
		# Display an error message if something goes wrong.
		except Exception as e:
		    # print ("Error: ", e)
		    return ("amazon_SES", False)
		else:
			return ("amazon_SES", True)
		    
				



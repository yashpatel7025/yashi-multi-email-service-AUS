from .EmailManager import EmailManager
import email, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class GoogleSMTPService(EmailManager):
	"""Goggle SMTP Service implementation to send email"""

	GOOGLE_SMTP_USERNAME = None
	GOOGLE_SMTP_PASSWORD = None
	GOOGLE_SERVER = "smtp.googlemail.com"
	
	SENDER = None
	SENDERNAME = None

	def __init__(self, config):
		self.GOOGLE_SMTP_USERNAME = config.get("GOOGLE_SMTP_USERNAME")
		self.GOOGLE_SMTP_PASSWORD = config.get("GOOGLE_SMTP_PASSWORD")
		self.SENDER = config.get("FROM_EMAIL")
		self.SENDERNAME = config.get("FROM_EMAIL_NAME")
		
	def send_email(self, context):
		message = MIMEMultipart()
		message["From"] = email.utils.formataddr((self.SENDERNAME, self.SENDER))
		message["To"] = context.get("to_email")
		message["Subject"] = context.get("subject")
		# Add body to email
		part1 = MIMEText(context.get("body_text"), 'plain')
		message.attach(part1)

		# Log in to server using secure context and send email
		# Try to send the message.
		try:  
			ssl_context = ssl.create_default_context()
			with smtplib.SMTP_SSL(self.GOOGLE_SERVER, 465, context=ssl_context) as server:
			    server.login(self.SENDER, self.GOOGLE_SMTP_PASSWORD)
			    server.sendmail(self.SENDER, context.get("to_email"), message.as_string())
		# Display an error message if something goes wrong.
		except Exception as e:
			# print ("Error: ", e)
		    return ("google_SMTP", False)
		else:
		    return ("google_SMTP", True)
from .EmailManager import EmailManager
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content

class SendGridService(EmailManager):
	"""docstring for ClassName"""
	SENDGRID_API_kEY = None
	SENDER = None

	def __init__(self, config):
		self.SENDGRID_API_kEY = config.get("SENDGRID_API_kEY")
		self.SENDER = config.get("FROM_EMAIL")

	def send_email(self, context):
		message = Mail(
		    from_email= self.SENDER,
		    to_emails=context.get("to_email"),
		    subject=context.get("subject"),
		    html_content=Content("text/plain", context.get("body_text")))
		try:
		    sg = SendGridAPIClient(self.SENDGRID_API_kEY)
		    response = sg.send(message)
		    if response.status_code==202:
		        return ("send_grid", True)
		    return ("send_grid", False)
		except Exception as e:
		    return ("send_grid", False)

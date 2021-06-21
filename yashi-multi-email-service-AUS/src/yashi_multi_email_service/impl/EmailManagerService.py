from .EmailManager import EmailManager
from yashi_multi_email_service.factory.EmailServiceFactory import EmailServiceFactory
from yashi_multi_email_service.Exceptions.Exception import CustomException

class EmailManagerService(EmailManager):

	available_services = ["send_grid", "google_SMTP", "amazon_SES"]

	"""Email Manager Service implementation to send email"""
	def send_email(self , context):
		if not context.get("config"):
			raise CustomException("config not found")
		
		selected_service = context.get("config").get("DEFAULT_SERVICE")

		if selected_service and selected_service not in self.available_services:
			raise CustomException("invalid service name in context")
		services = self.available_services.copy()
		if selected_service:
			services.remove(selected_service)
			services.append(selected_service)
		while len(services):
			service = services.pop()
			service, sent_status = EmailServiceFactory.getEmailServiceInstance(service)(context.get("config")).send_email(context)
			if sent_status:
				return (service, sent_status)
		return (False, False)


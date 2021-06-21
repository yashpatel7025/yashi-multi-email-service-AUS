from yashi_multi_email_service.impl.AmazonSESService import AmazonSESService
from yashi_multi_email_service.impl.GoogleSMTPService import GoogleSMTPService
from yashi_multi_email_service.impl.SendGridService import SendGridService


class EmailServiceFactory(object):
	"""Factory class for seleting Email Service"""

	def getEmailServiceInstance(service_name):
		services = {
        "amazon_SES": AmazonSESService,
        "google_SMTP": GoogleSMTPService,
        "send_grid": SendGridService
        }
		return services.get(service_name, AmazonSESService)
  

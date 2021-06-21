from abc import ABC, abstractmethod
# interface
class EmailManager(ABC):
	
	@abstractmethod
	def send_email(self, context):
		"""this method sends email"""
		raise NotImplementedError

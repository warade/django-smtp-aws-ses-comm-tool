from django.test import TestCase
from .utils import sendMail, validate, welcomeMail, checkTemplateExists
from django.core.exceptions import ValidationError
from django.template import TemplateDoesNotExist
import datetime

# Variables initialized
valTemp = 'welcome.html'
invalTemp = 'elcome.html'
valSender = "warade.anshul@gmail.com"
invalSender = "warade.anshul.gmail.com"
valRecipient = "anshul@brightmoney.co"
invalRecipient = "anshul.brightmoney.co"
now = datetime.datetime.now()
kwargs = {"username": "faraday_anshul", "full_name": "Anshul Warade","signup_date": now}

class MyTestCases(TestCase):

	# Testing validation error in case of invalid emails
	def test_email_validation_raiseError(self):
		with self.assertRaises(ValidationError):
			validate(valSender, [invalRecipient,])
			validate(invalSender, [valRecipient,])

	# Testing for valid template name
	def test_checkTemplateExists(self):
		with self.assertRaises(TemplateDoesNotExist):
				checkTemplateExists(invalTemp)

	# Testing for sending mail directly through template
	def test_welcomeMail(self):
		# args = {'welcome.html', 'warade.anshul@gmail.com', ['anshul@brightmoney.co',]}
		self.assertEqual(1, welcomeMail(valTemp, valSender, [valRecipient], **kwargs))

	# Testing for sending mail
	def test_sendMail(self):
		# args = {'welcome.html', 'warade.anshul@gmail.com', ['anshul@brightmoney.co',]}
		self.assertEqual(1, sendMail(valTemp, valSender, [valRecipient,], **kwargs))





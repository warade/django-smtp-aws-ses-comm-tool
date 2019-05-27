# reference https://github.com/vintasoftware/django-templated-email

from django.shortcuts import render
from django.core.mail import send_mail
from templated_email import send_templated_mail
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Validate sender and recipient email address!
def validate(sender, recipient_list):
	validate_email(sender)
	for recipient in recipient_list:
		validate_email(recipient)


# Mail backend for welcome.html template
def welcomeMail(*args, **kwargs):
	templateName = args[0]
	sender = args[1]
	recipient_list = args[2]
	try:
		send_templated_mail(
			template_name=templateName,
	        from_email=sender,
	        recipient_list=recipient_list,
	        context={
	            'username': kwargs["username"],
	            'full_name': kwargs["full_name"],
	            'signup_date': kwargs["signup_date"]
	        }
		)
		return 1
	except:
		return 0

def checkTemplateExists(templateName):
	try:
		get_template('templated_email/' + templateName)
	except TemplateDoesNotExist:
		msg = "Template " + templateName + " does not exist!"
		raise TemplateDoesNotExist(msg)

def sendMail(*args, **kwargs):
	checkTemplateExists(args[0])
	validate(args[1], args[2])
	if args[0] == "welcome.html":
		return welcomeMail(*args, **kwargs)

## this is how we will send the email on another app
# import datetime
# from brightMail.utils import sendMail
# now = datetime.datetime.now()
# kwargs = {"username": "varun", "full_name": "Varun Modi","signup_date": now}
# sendMail('welcome.html', 'warade.anshul@gmail.com', ['anshul@brightmoney.co',], **kwargs)

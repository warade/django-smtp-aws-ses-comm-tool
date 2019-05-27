from django.shortcuts import render
from django.shortcuts import redirect

from django.http import Http404
from django.core.mail import send_mail

def sendMail(request):
	context = {
		'message': "Email Sent!"
	}
	response = send_mail('Test subject', '<h1> This is the body </h1>', 'warade.anshul@gmails.com',['anshul@brightmoney.co'], fail_silently=False)
	return render(request, 'amazing.html', context)
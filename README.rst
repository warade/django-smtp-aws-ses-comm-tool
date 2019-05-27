=====
brightMail
=====

brightMail is a django app designed for the brightMoney
templated emails which uses SMTP backend of django to send emails.

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. Run following to install

	pip install dist/django-brightMail-0.1.tar.gz


2. Add "brightMail" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'brightMail',
    ]
    
3. Install the package:
	https://github.com/bancek/django-smtp-ssl

4. You need to have your SMTP credentials as EMAIL_HOST_USER and EMAIL_HOST_PASSWORD,For every region SMTP credentials vary. So create your SMTP credentials based on what you are choosing as your region. Follow the steps:
	Sign in to the AWS Management Console and open the Amazon SES console at https://console.aws.amazon.com/ses/.
	In the navigation pane, choose SMTP Settings.
	In the content pane, choose Create My SMTP Credentials.
	For Create User for SMTP, type a name for your SMTP user. Alternatively, you can use the default value that is provided in this field. When you finish, choose Create. 
	
5. After getting the credentials, you need to verify email addresses of the sender and recipient for sandbox mode. You dont need to verify the recipient in production mode. (Read the docs).
	1. Go to https://aws.amazon.com/ses/ and Get started.
	2. Choose the simple email service under Customer Engagement.
	3. Go to Email Addresses in your left.
	4. Add Email addresses and verify them.

6. When installing brightMail, it will automatically install django-templated-email (https://github.com/vintasoftware/django-templated-email) just cross check it once by running 'pip3 list'

7. Include following settings in settings.py
	from templated_email.backends.vanilla_django import TemplateBackend
	EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
	
	TEMPLATED_EMAIL_BACKEND = TemplateBackend
	TEMPLATED_EMAIL_AUTO_PLAIN = False
	TEMPLATED_EMAIL_TEMPLATE_DIR = 'templated_email/' #use '' for top level template dir, ensure there is a trailing slash
	TEMPLATED_EMAIL_FILE_EXTENSION = 'html'
	# HOST AND PORT may vary, I used us-west-2 region
	EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
	EMAIL_PORT = 465
	EMAIL_HOST_USER = your_SMTP_username
	EMAIL_HOST_PASSWORD = your_SMTP_password
	EMAIL_USE_TLS = True

8. Include the file and use it's utils functions to send templated emails:

    from brightMail.utils import sendMail

9. Use it to send mails, notice that context data i.e. kwargs key value pairs should include all the variables used in specified template.
	
	kwargs = {"key": "value", "key": "value"}
	sendMail(templateName, sender, recipient_list, **kwargs)

10. Templates can be accessed from templates/templated_email


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
import smtplib

from django.core.mail import EmailMessage

from django.conf import settings
from .forms import EmailForm
import smtplib, ssl


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'emailattachment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    #  Single File Attachment
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            # attach = request.FILES['attach']

            # mail = EmailMessage(
            #         subject, message, settings.EMAIL_HOST_USER, [email])
            #     # mail.attach(attach.name, attach.read(), attach.content_type)
            # mail.send()
            # return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s' % email})
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "aniketsingh20681@gmail.com"  # Enter your address
            receiver_email = email  # Enter receiver address
            password = "vejozcfhunanadfb"
            # message = """\
            # Subject: su

            # This message is sent from Aniket Singh to test Email."""
            message = message
            subject = subject


            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
               server.login(sender_email, password)
               server.sendmail(sender_email, receiver_email, message,subject)
               return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s' % email})


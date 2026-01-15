from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from PortFolio import settings
from Portfolio.forms import connectForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from Portfolio.forms import connectForm
import threading


# Create your views here.

def intro(request):
    return render(request, "Portfolio/Home.html")





def send_email_async(email_message):
    try:
        email_message.send(fail_silently=False)
    except Exception as e:
        print("Email error:", e)


def connect(request):
    if request.method == "POST":
        form = connectForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            email_message = EmailMessage(
                subject=f"New Portfolio Message from {email}",
                body=f"Message:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],
            )

            # 🔥 NON-BLOCKING EMAIL SEND
            threading.Thread(
                target=send_email_async,
                args=(email_message,)
            ).start()

            messages.success(request, "Message sent successfully ✅")
            return render(request, "Portfolio/Home.html")

        else:
            messages.error(request, "Invalid form data ❌")
            return render(request, "Portfolio/Home.html")

    return render(request, "Portfolio/Home.html")

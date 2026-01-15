from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from PortFolio import settings
from Portfolio.forms import connectForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage


# Create your views here.

def intro(request):
    return render(request, "Portfolio/Home.html")


def connect(request):

    if request.method == "POST":
        form = connectForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            print(email, message)

            try:

                email_message = EmailMessage(
                    subject=f"New Portfolio Message from {email}",
                    body=f"Message:\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.DEFAULT_FROM_EMAIL],
                    reply_to=[email],
                )

                email_message.send(fail_silently=False)
                messages.success(request,"Message sent successfully")

            except Exception as e:
                print(e)
                messages.error(request, f"Something went wrong!{e}")
                failed_message = "sorry we are unable to connect you to Pintu Kandara"
                return render(request,"Portfolio/Home.html",context={"context_message":failed_message})

            return render(request, "Portfolio/Home.html")
        else:
            return render(request, "Portfolio/Home.html")

    else:
        form = connectForm()
    return render(request, "Portfolio/Home.html")
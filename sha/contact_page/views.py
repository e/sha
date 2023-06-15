from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm


def twots(request):
    context = {"active_tab": "twots"}
    return render(request, "contact_page/twots.html", context)


def kkc(request):
    context = {"active_tab": "kkc"}
    return render(request, "contact_page/kkc.html", context)


def ceremonies(request):
    context = {"active_tab": "ceremonies"}
    return render(request, "contact_page/ceremonies.html", context)


def training(request):
    context = {"active_tab": "training"}
    return render(request, "contact_page/training.html", context)


def project(request):
    context = {"active_tab": "project"}
    return render(request, "contact_page/project.html", context)


def thanks(request):
    context = {"active_tab": "project"}
    return render(request, "contact_page/thanks.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["marcosbartolome@gmail.com"]
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = ContactForm()

    context = {"form": form, "active_tab": "contact"}
    return render(request, "contact_page/contact.html", context)

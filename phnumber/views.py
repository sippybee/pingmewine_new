from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import json
import logging
import os
from .models import Deal
from .forms import ClientForm
logger = logging.getLogger(__name__)

twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')


def send_message(request):

    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
        body='Hi, your test result is Make fucking sale already. Great job',
        from_=twilio_number,
        to='+12013136587' 
    )




class DealDetailView(ListView):
    model = Deal
    template_name = "index_api.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DealDetailView, self).get_context_data(*args, **kwargs)
        # context["modules"] = Module.objects.all()
        # context["tags"] = Tag.objects.all()
        # # instance = self.get_object()
        
        # context["related"] = sorted(Product.objects.get_related(instance)[:5], key=lambda x: x.title)
        # context["number_of_reviews"] = comments.count()
        
        return context
    
class PingMeView(View):
    # template_name = "request_quote.html"
    # form_class = RFQForm
    # success_url = ' '

    def get(self, request, *args, **kwargs):
        form = ClientForm()
        context = {'form': form}
        # modules = Module.objects.all()
        # context["modules"] = modules
        print("GGGGET")
        return render(request, "index_api.html", context)

    def post(self, request, *args, **kwargs):
        print("Hi")
        form = ClientForm(data=request.POST)
        if form.is_valid():
            fone_number = form.cleaned_data['phone'].as_e164
            client = Client(twilio_account_sid, twilio_auth_token)

            message = client.messages.create(
                body='Hi, thank you for signig up! We are searching for best deals and you will hear from us soon',
                from_=twilio_number,
                to=f'{fone_number}' 
            )
            # print(phone.as_e164)
            # phone = PhoneNumber.from_string(phone_number=raw_phone, region='RU').as_e164
        #     email = form.data.get("email")
        #     rfq = form.data.get("rfq")
        #     full_name = form.data.get("name")
        #     company = form.data.get("company")
        #     from_email = settings.DEFAULT_FROM_EMAIL
        #     to_email = ["art@roboticview.com"]
        #     contact_message = message_form.format(full_name,company,email,rfq)
        #     print("contact_message",contact_message)
        #     message_to_me = Mail(
        #         from_email=from_email,
        #         to_emails="art@roboticview.com",
        #         subject='A Request for Corporate Training',
        #         html_content=contact_message
        #     )
        #     message_to_them = Mail(
        #         from_email=from_email,
        #         to_emails=email,
        #         subject='We have recieved your request',
        #         html_content=conformation_message
        #     )
        #     try:
        #         response = sg.send(message_to_me)
        #         print("response",response)
        #         if response.status_code == 202:
        #             conformation = sg.send(message_to_them) 
        #             messages.success(request, "Thank you. We've emailed you a confirmation" )
        #     except Exception as e:
        #         messages.error(request, "Something went wrong. Please email us at python@artyudin.com" )
        #         print("huy")
        #         pass
        #     return render(request, 'request_quote.html', {'form': form})
        # messages.error(request, "Something went wrong. Please email us at python@artyudin.com" )
        print("Not valid")

        return render(request, "index_api.html", {'form': form})
    
@method_decorator(csrf_exempt, name='dispatch')
class WineChatView(View):
    def post(self, request, *args, **kwargs):
        incoming_msg = request.POST.get('Body', '').lower()
        print(incoming_msg)
        print("DDDDDD",request.POST)
        resp = MessagingResponse()
        msg = resp.message()
        responded = False
        if 'hi' in incoming_msg:
            my_response = "Buy some wine!"
            msg.body(my_response)
            responded = True
            print(dir(msg))
            return HttpResponse('Success!')


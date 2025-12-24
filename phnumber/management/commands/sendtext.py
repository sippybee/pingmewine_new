from django.core.management.base import BaseCommand, CommandError
from twilio.rest import Client
# import phonenumbers
import os
# from apps.pingme.models import Phonenumber
# from apps.accounts.models import PingStatus
# from .util import get_phone_numbers

  
PATH="/workspace/september2025.1.csv"



twilio_account_sid = 'ACf9deebb2ba3ac128c92a4da25828a472'
twilio_auth_token = '1d20fa53a0f4bc61d721f00ee9facd05'
twilio_number = '+18482798466'

def send_message(message,PHONENUMBER):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body = message,
        from_ = twilio_number,
        # media_url=['https://winecopilot.com/static/img/PMW.png'],
        to=PHONENUMBER 
    )
    print("Created",dir(message))
    return message.date_sent



class Command(BaseCommand):
    def handle(self, *args, **options):
        TMPL = '''{}\n\n{}\n\n{}'''.strip()
        greeting = 'A smooth Chianti made to be savored — Buy one, get the second 50% off! Just $18.00 a bottle.'.strip() 
        first = "Buy now, or come This Friday from 6 - 7 PM to judge for yourself, Pizza is on us.".strip() 
        # second = "Join today and receive a complimentary decanter with your first delivery on Feb 28th!".strip() 
        third = "Stop by 584 Myrtle Ave., or order now at https://itipsy.com/pic".strip() 
    
        # test
        client = Client(twilio_account_sid, twilio_auth_token)
        
        # numbers_all = Phonenumber.objects.all()
        # numbers = [(n,n.phone_number.as_e164) for n in numbers_all]
        numbers = []
        # numbers = get_phone_numbers(PATH)
        numbers.append('2013136587')
        # numbers.append('7323097540')
        counter = 0
        for to_number in numbers:
            # print(to_number)
            try:
                message = client.messages.create(
                    body = TMPL.format(greeting, first, third),
                    # media_url=["https://tipsy.nyc3.digitaloceanspaces.com/Wine-Tasting-with-pizza.png"],
                    from_ = twilio_number,
                    to = to_number,
                )
                print(f'Message sent to {message.to} with ID: {message._properties}')
                print("error_code",message.error_code)
                print("error_message",message.error_message)
                print("status",message.status)
                # new_record = PingStatus(number=obj, body=message._properties['body'], date_sent=message._properties['date_updated'], status=message._properties['status'])
                # new_record.save()
                # print("record created")
                counter+=1
                print("Counter",counter)
            except Exception as e:
                print(e)
                print("Message not sent")
                print(f'Number: {to_number} not sent')
        print("Counter",counter)
        # numbers = get_phone_numbers(PATH)
        print(numbers)

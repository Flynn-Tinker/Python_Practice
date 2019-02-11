from six.moves import input
from googlevoice import Voice
# If last visit - day >= 150 days and Text has not been sent before, then run script

def run():
    voice = Voice()
    voice.login()
    client_name = 'Kayla'
    dog_name = 'Radar'
    phoneNumber = '4017145786'

    text = ("Hi {}, we'd love to have you back for another appointment for {}. - Animal Kingdom Grooming." \
    "To book: https://squ.re/2SxhzaJ").format(client_name,dog_name)

    voice.send_sms(phoneNumber, text)


__name__ == '__main__' and run()
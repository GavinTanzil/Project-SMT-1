import random
from datetime import datetime

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello Bois!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`What seems to be the problem?`'

    if p_message == 'mars igs':
        return 'https://youtu.be/HM1BN2Qm8Bo?si=6vwyRaXgIZ5D447c'

    if p_message == 'igs passwordnya apa bois?':
        return 'THE FIRST CHOICE TO THE BEST FUTURE!'

    if p_message == '!timestamp':
        timestamp = datetime.now()
        a = timestamp.strftime('%H:%M:%S')
        return a

    if p_message == 'regan':
        return 'SEPUH'

    if p_message == 'marvellino':
        return 'IM DEMON 1'

    if p_message == 'richard':
        return 'Im diamond 3'

    if p_message == 'deren':
        return 'Im diamond 1'

    if p_message == 'gavin':
        return 'Im diamond 1 (almost) :)'

    if p_message == '!Google':
        return 'https://www.google.com'

    if p_message == 'igs':
        return 'here is the result that i have searched up for you : https://www.ignatiusglobal.sch.id'

    return 'I dont know what you said my friend! Either you type "!help" or you can just find it in : https://www.google.com'



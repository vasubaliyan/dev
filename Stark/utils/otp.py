import re
from base64 import b64encode
import random
import string
#from django.utils.text import slugify
from io import BytesIO



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def unique_key_generator(instance):

    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_key_generator(instance)
    return key




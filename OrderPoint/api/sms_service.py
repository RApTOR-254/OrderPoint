import africastalking
from django.conf import settings

africastalking.initialize(
    username=settings.AT_API_USERNAME,
    api_key=settings.AT_API_KEY,
)

sms = africastalking.SMS

def send_sms(message, recipients, sender_id=None):
    """
    Sends an SMS via africa's talking.
    args:
        message=(str): Information to be sent to Customer,
        recipients=(list[str]): list of phone_numbers in international format e.g ["+254702xxxxxx],
        sender_id=(str): --Registered shortcode for production environment
                         --None for development environment.
    """

    try:
        response = sms.send(message, recipients, sender_id)
        return response
    except Exception as e:
        return {"error": str(e)}
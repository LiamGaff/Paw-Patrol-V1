# from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.conf import settings

# class StripeWH_Handler:
#     """Handle Stripe webhooks"""

#     def __init__(self, request):
#         self.request = request

#     def my_webhook_view(request):
#         payload = request.body
#         event = None

#         try:
#             event = stripe.Event.construct_from(
#                 json.loads(payload), stripe.api_key
#             )
#         except ValueError as e:
#             # Invalid payload
#             return HttpResponse(status=400)

#         # Handle the event
#         if event.type == 'payment_intent.succeeded':
#             payment_intent = event.data.object  # contains a stripe.PaymentIntent
#             print('PaymentIntent was successful!')
#         elif event.type == 'payment_method.attached':
#             payment_method = event.data.object  # contains a stripe.PaymentMethod
#             print('PaymentMethod was attached to a Customer!')
#         # ... handle other event types
#         else:
#             print('Unhandled event type {}'.format(event.type))

#         return HttpResponse(status=200)

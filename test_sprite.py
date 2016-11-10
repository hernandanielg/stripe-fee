import stripe
stripe.api_key = "sk_test_xJNBke1EQ4YPIrZo81lwTSjo"

try:
    token = stripe.Token.create(
      card={
          "number": '4242424242424242',
          "exp_month": 12,
          "exp_year": 2017,
          "cvc": '123'
      },
    )
    print("Token is %s" % token.id)
    pass
except stripe.error.CardError as e:
    body = e.json_body
    err  = body['error']

    print("Status is: %s" % e.http_status)
    print("Type is: %s" % err['type'])
    print("Code is: %s" % err['code'])
    # param is '' in this case
    print("Param is: %s" % err['param'])
    print("Message is: %s" % err['message'])


print("Token: %s" % token.id)

customer = stripe.Customer.create(
  description="Usuario Prueba",
  source=token.id
)

print("Customer: %s" % customer.id)



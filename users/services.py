import stripe

from config.settings import STRIPE_APIKEY

stripe.api_key = STRIPE_APIKEY


def create_stripe_product(name):
    product = stripe.Product.create(name=name)

    return product.get("id")


def create_stripe_price(amount, product):
    return stripe.Price.create(
        currency="rub", unit_amount=amount * 100, product=product
    )


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )

    return session.get("id"), session.get("url")

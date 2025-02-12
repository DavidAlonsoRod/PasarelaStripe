import os
import dotenv
import stripe

# Cargar las variables de entorno

dotenv.load_dotenv()
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

stripe.api_key = STRIPE_SECRET_KEY

# Crear un método de pago

def create_payment_method () -> str:

    try:
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={"token": "tok_visa"}
        )
        print(f"Método de pago creado con ID: {payment_method.id}")

        return payment_method.id
    except stripe.error.StripeError as e:
        print(f"Error al crear el método de pago: {e.user_message}")
        return ""

# Crear un pago

def create_payment (payment_method_id: str, client_id: str, amount: int, currency:str, product_id:str) :
    
    try:
        payment = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
            payment_method=payment_method_id,
            confirm=True,
            customer=client_id,
            metadata={"product_id": product_id}

        )
    
        print(f"Pago creado con ID: {payment.id} realizado correctamente") 
   
    except stripe.error.CardError as e:
        print(f"Error en la tarjeta: {e.user_message}")
    except stripe.error.StripeError as e:
        print(f"Error en stripe: {e.user_message}")



# Crear un cliente

def create_user (name, email):

    try:
        client = stripe.Customer.create(
            name=name,
            email=email
        )
        print(f"Cliente {name} creado con ID: {client.id}")

        return client.id
    except stripe.error.StripeError as e:
        print(f"Error al crear el cliente: {e.user_message}")
        return ""
    
#   


# Asociar método de pago a un cliente


def add_payment_method_to_user (payment_method_id, client_id):

    try:
        stripe.PaymentMethod.attach(
            payment_method_id,
            customer=client_id
        )
        print(f"Método de pago {payment_method_id} asociado al cliente {client_id}")

    except stripe.error.StripeError as e:
        print(f"Error al asociar el método de pago al cliente: {e.user_message}")

def get_product():
    
    products = stripe.Product.list(limit=1)
    return products ["data"] [0]["id"]
        


   
def get_product_price (product_id):

    price = stripe.Price.list(product=product_id, limit=1)

    price_id= price ["data"] [0]["id"]
    amount = price ["data"] [0]["unit_amount"]
    currency = price ["data"] [0]["currency"]

    return price_id, amount, currency


   
client_id = create_user ('María', 'maridp@gmail.com')
   
payment_method_id=create_payment_method ()

add_payment_method_to_user(payment_method_id, client_id)


product_id = get_product()
price_id, amount, currency = get_product_price(product_id)

create_payment(payment_method_id, client_id, amount, currency)
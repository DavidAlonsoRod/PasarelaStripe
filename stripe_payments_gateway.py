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

def create_payment (payment_method_id: str, cliente_id: str):
    
    try:
        payment = stripe.PaymentIntent.create(
            amount=5 * 100,
            currency="usd",
            payment_method_types=["card"],
            payment_method=payment_method_id,
            confirm=True,
            customer=cliente_id

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
    
create_user ('David', 'hello@davilondev.com')


# Asociar métdo de pago a un cliente


def add_payment_method_to_user (payment_method_id, client_id):

    try:
        stripe.PaymentMethod.attach(
            payment_method_id,
            customer=client_id
        )
        print(f"Método de pago {payment_method_id} asociado al cliente {client_id}")

    except stripe.error.StripeError as e:
        print(f"Error al asociar el método de pago al cliente: {e.user_message}")

def get_products ():
    try:
        products = stripe.Product.list(limit=5)
        for product in products:
        
            print(f"Productos: {product}")

    except stripe.error.StripeError as e:
        print(f"Error al obtener los productos: {e.user_message}")

# def create_product (name, price):

#     try:
#         product = stripe.Product.create(
#             price=price,
#             name=name,
#             description="Producto de prueba",   
#         )
#         print(f"Producto {name} creado con ID: {product.id}")

#         return product.id
#     except stripe.error.StripeError as e:
#         print(f"Error al crear el producto: {e.user_message}")
#         return ""

   
# client_id = create_user ('David', 'hello@davilondev.com')
   
# payment_method_id=create_payment_method ()

# create_payment(payment_method_id, client_id)

get_products()
import json

def lambda_handler(event, context):
    productos = [
        {"id": 1, "nombre": "Laptop", "precio": 1500},
        {"id": 2, "nombre": "Mouse", "precio": 20},
        {"id": 3, "nombre": "Teclado", "precio": 45}
    ]
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(productos)
    }
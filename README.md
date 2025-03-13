
# 🧪 Demostración Práctica - Serverless vs. Contenedores en AWS

Esta demostración contiene dos implementaciones de una API simple de productos para comparar **Serverless (AWS Lambda)** y **Contenedores (ECS Fargate)** como opciones arquitectónicas en AWS.

---

## 📦 Estructura del Proyecto

```
.
├── lambda/
│   ├── lambda_function.py
├── contenedores/
│   ├── app.py
│   ├── Dockerfile
└── README.md
```

---

## ✅ Requisitos Previos

- AWS CLI configurado (`aws configure`)
- Docker instalado (para la parte de contenedores)
- Cuenta de AWS con permisos para:
  - Lambda
  - API Gateway
  - IAM
  - ECS
  - ECR
  - Fargate
- Repositorio ECR para contenedor

---

## 🚀 Parte 1: Serverless con AWS Lambda

### 📁 Código Lambda (Python)

Crear una funcion lambda llamada ProductosFunction

`lambda/lambda_function.py`:
```python
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
```

### 📜 Crear una API REST con ApiGateway

- Crear una nueva API REST, poner un nombre, en modo regional
- Crear un metodo GET, seleccionando la funcion lambda creada en la sección anterior

### 🔗 Obtener el endpoint

Después del despliegue con un stage productos, ve a la consola de API Gateway para copiar la URL base.

---

## 🐳 Parte 2: Contenedores con ECS Fargate

### 📁 Código API (Python Flask)

`contenedores/app.py`:
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/productos", methods=["GET"])
def productos():
    return jsonify([
        {"id": 1, "nombre": "Laptop", "precio": 1500},
        {"id": 2, "nombre": "Mouse", "precio": 20},
        {"id": 3, "nombre": "Teclado", "precio": 45}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 🐳 Dockerfile

`contenedores/Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]
```

### 🏗️ Construir y subir a ECR

```bash
# 1. Crear repositorio ECR (solo si no existe)
aws ecr create-repository --repository-name productos-api

# 2. Login a ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# 3. Build, tag y push
docker build -t productos-api .
docker tag productos-api:latest <account-id>.dkr.ecr.<region>.amazonaws.com/productos-api
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/productos-api
```

> ⚠️ Reemplaza `<account-id>` y `<region>` con los valores correspondientes a tu cuenta y región.

### 🚀 Despliegue en ECS Fargate

- Crea un cluster en ECS
- Crea una definicion de tarea, con la URI del contenedor
- Crea un servicio con la definicion de tarea y asegurate de abrir los puertos 5000 o 80 para el grupo de seguridad

---

## 🧪 Pruebas

- Usa Postman, curl o navegador para probar ambos endpoints:
  - `https://<api-gateway-url>/productos`
  - `http://<ip-task-ecs>/productos`

Ambos deben devolver el mismo JSON con la lista de productos.

---

## 📝 Créditos

Demostración realizada como parte del webinar:  
**“Serverless vs. Contenedores: ¿Cuál es la Mejor Opción para tu Arquitectura?”**

https://www.youtube.com/watch?v=PBdMEumK3wE
---

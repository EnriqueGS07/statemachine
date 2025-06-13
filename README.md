# Maquina de estados: Prueba tecnca Sainapsis
### By: Enrique González Suárez

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-3.2-green)
![Demo](https://img.shields.io/badge/demo-online-blue)
![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)
[![Swagger UI](https://img.shields.io/badge/docs-Swagger_UI-blue?logo=swagger)](https://TU_DOMINIO/swagger/)



Para esta prueba se construyo una maquina de estados con back y front para gestionar ordenes de compras que estan relacionadas con diferentes productos.


❗*Se crearon dos repositorios, uno para el back y otro para el front, en este Repo podemos encontrar el Back-end y el front-end lo econtramos en el repo: https://github.com/EnriqueGS07/statemachine-front*

## 🚀 Demo

http://zappa-front.s3-website-us-east-1.amazonaws.com

## 📦 Tecnologías

- Frontend: React + TypeScript
- Backend: Python + Django
- Infraestructura: AWS Lambda + S3 + MongoDB

## 🛠️ Instalación y ejecución local
1. Clona el repositorio
```
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```
2. Configura el ambiente del back
```
python -m venv venv 
venv/Scripts/Activate  
pip install -r requirements.txt
```
3. Inicia tu servidor
```
python manage.py runserver
```
Cuando hagas esto tu servidor de Django deberia estar corriendo en http://127.0.0.1:8000/ y podras acceder desde tu navegador o hacer peticiones desde postman o el front de esta aplicación.

Si quieres ver documentación de la API puedes entrar a http://127.0.0.1:8000/swagger

## ⚙️ Configuración y despliegue
*Los siguientes pasos fueron realizados y no son necesarios para que la aplicación se ejecute en un ambiente local*

Se uso la herramienta Zappa la cual empaqueta la aplicación y la prepara para el despliegue, esta construida para pyhton y permite ejecutar el backend en AWS Lambda con pocos comandos

1. Inicialización
```
zappa init
```
despues de ejecutar este comando saldrán preguntas de configuración de zappa con AWS, como resultado saldra un archivo llamado **zappa_settings.**json de este estilo
```
{
  "production": {
    "app_function": "myproject.wsgi.application",
    "aws_region": "us-east-1",
    "profile_name": "default",
    "project_name": "myproject",
    "runtime": "python3.11",
    "s3_bucket": "my-zappa-bucket"
  }
}
```
2. Desplegar en AWS Lambda
```
zappa deploy dev
```
con este comando zappa crea configura y despliega en AWS Lambda la API y esta lista para probar desplegada





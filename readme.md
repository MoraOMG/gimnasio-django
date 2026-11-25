# PowerFit Gym

Aplicación web para gestionar planes de entrenamiento de un gimnasio.
Hecha con Django y MySQL.

Alumno: Juan Manuel Mora Tobar

## Qué hace
Permite crear, ver, editar y eliminar planes de entrenamiento.

## Cómo ejecutarla
1. Encender Apache y MySQL en XAMPP.
2. Crear la base gimnasio_db en phpMyAdmin.
3. Instalar los requisitos: pip install -r requirements.txt
4. Crear las tablas: python manage.py migrate
5. Iniciar el servidor: python manage.py runserver
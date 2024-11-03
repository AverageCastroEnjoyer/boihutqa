# Proyecto: Aseguramiento de la Calidad

## Estudiantes
- Santiago Ramos
- Manfred Jones
- Esteban Castro

## Enlace al proyecto original
[https://github.com/shaongitbd/boihut](https://github.com/shaongitbd/boihut)

---
## Instalacion
```python
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Ejecucion
```python
python3 manage.py runserver
```

## Probrar tests unitarios
```python
python3 manage.py test
```

## Para probar la cobertura
### Instalar la herramienta
```python
pip install coverage
```
### Correr la herramienta
```python
coverage run manage.py test
```
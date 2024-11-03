Proyecto Aseguramiento de la calidad
Para instalar:

```python
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Para correr
```python
python3 manage.py runserver
```

Para probrar tests unitarios
```python
python3 manage.py test
```

Para probrar la cobertura
Instalar la herramienta
```python
pip install coverage
```
Correr la herramienta
```python
coverage run manage.py test
```
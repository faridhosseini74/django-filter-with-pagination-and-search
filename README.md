# django-filter-with-pagination-and-search
default database is MySQL, you should replace config of your own database in (django-filter-with-pagination-and-search/setting.py) and change data model in (core/model.py)
and change filter function in (core/views.py) for make it your own and run:

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
and you all set ;)

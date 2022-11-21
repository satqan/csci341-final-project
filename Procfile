release: python project/manage.py migrate
web: gunicorn --chdir project project.wsgi:application && cd project

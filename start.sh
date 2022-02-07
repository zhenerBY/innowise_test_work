#!/usr/bin/env bash

python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
gunicorn -b 0.0.0.0:8000 config.wsgi --log-file -
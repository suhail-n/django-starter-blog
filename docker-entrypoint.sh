#!/bin/bash
# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
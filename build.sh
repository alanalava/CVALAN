#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# --- COMANDO DE LIMPIEZA TOTAL ---
# Borra el historial de acciones recientes (lo que se ve feo)
# Y borra todos los datos de tus tablas de Perfil para empezar de cero
echo "from django.contrib.admin.models import LogEntry; \
from Perfil.models import DatosPersonales; \
LogEntry.objects.all().delete(); \
DatosPersonales.objects.all().delete();" \
| python manage.py shell

# Crear/Asegurar superusuario
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='Jandry').exists() or \
User.objects.create_superuser('Jandry', 'Jandry@gmail.com', 'NCQM200406')" \
| python manage.py shell
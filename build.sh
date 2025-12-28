#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recopilar archivos estáticos
python manage.py collectstatic --no-input

# 3. LIMPIEZA TOTAL (Opcional, úsala solo esta vez para limpiar las pruebas)
# Si quieres que se borre todo lo anterior para empezar de cero, deja la siguiente línea.
# Si ya no quieres que se borre nada más en el futuro, ponle un # al principio.
python manage.py flush --no-input

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear el superusuario automáticamente
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='Jandry').exists() or \
User.objects.create_superuser('Jandry', 'Jandry@gmail.com', 'NCQM200406')" \
| python manage.py shell
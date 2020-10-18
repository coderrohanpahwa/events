Requirements :- 
asgiref==3.2.10
certifi==2020.6.20
chardet==3.0.4
Django==3.1.2
idna==2.10
psycopg2==2.8.6
PyJWT==1.7.1
pytz==2020.1
requests==2.24.0
six==1.15.0
sqlparse==0.4.1
twilio==6.46.0
urllib3==1.25.10

Database Used :- postgresql (You can use default and make sure you do run python manage.py makemigrations , python manage.py migrate )
If using postgresql make sure you do update your credentials in settings.py/Databases


Make sure you do have Twilio account and update auth_token and account_sid in myapp/views.py 

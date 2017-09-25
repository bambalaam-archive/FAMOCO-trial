# FAMOCO-trial

## Installation

```
(enter a virtualenv, if you want to, before this step)
(sudo) apt install python-m2crypto aapt
pip install -r requirements.txt
python manage.py makemigrations apks
python manage.py migrate
python manage.py createsuperuser
```

## Running server

```
python manage.py runserver
```


## API Calls

### Root of the API

The API Root is available at the following address:

```
http://127.0.0.1:8000/apks/api/
```

It is browsable through hyperlinks in the resulting JSON.

### List all available APKs

Either through the API viewer on the website:

```
http://127.0.0.1:8000/apks/api/list/

```

Or through a CURL call:

```
curl http://127.0.0.1:8000/apks/api/list/
```


### Get specific APK by ID

Either through the API viewer on the website:

```
http://127.0.0.1:8000/apks/api/list/<index>/

```

Or through a CURL call:

```
curl http://127.0.0.1:8000/apks/api/list/<index>/
```

### Delete specific APK by ID

Either through the API viewer on the website, at the same page as above. If the user has ownership of the uploaded APK (or is a superuser), a red button saying "DELETE" will appear on the API viewer.

Or through a CURL call:

```
curl -u <username> http://127.0.0.1:8000/apks/api/list/<index>/ -X "DELETE"
```

After this call, the user will be prompted to enter the password for the username provided.

### Upload APK

It is necessary to register an account on the website before being able to upload an APK.

For the upload itself, two methods are possible. The first one is to upload it through the website, the other one is through a CURL call.

This is the preferred syntax, others are possible though:

```
curl -u <username> http://127.0.0.1:8000/apks/api/upload/ --upload-file <path-to-file>
```

After this call, the user will be prompted to enter the password for the username provided.

### List all users

Either through the API viewer on the website:

```
http://127.0.0.1:8000/apks/api/users/

```

Or through a CURL call:

```
curl http://127.0.0.1:8000/apks/api/users/
```

### Get specific User by ID

Either through the API viewer on the website:

```
http://127.0.0.1:8000/apks/api/users/<index>/

```

Or through a CURL call:

```
curl http://127.0.0.1:8000/apks/api/users/<index>/
```

## TO DO

- Remove extra images that are gathered
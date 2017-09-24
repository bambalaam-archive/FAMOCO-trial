# FAMOCO-trial

## Installation

```
(enter a virtualenv, if you want to, before this step)
(sudo) apt install python-m2crypto appt
pip install -r requirements.txt
```

## Running server

```
python manage.py runserver
```


## API Calls

### List all available APKs

Either through the API viewer on the website:

```
http://127.0.0.1:8000/apks/api/list/

```

Or through a CURL call
```
curl http://127.0.0.1:8000/apks/api/list/
```


### Get specific APK by ID

Either through the API viewer on the website:

```
http://127.0.0.1:8000/apks/api/list/<index>/

```

Or through a CURL call
```
curl http://127.0.0.1:8000/apks/api/list/<index>/
```

### Upload APK

This is the preferred method, others are possible though.

```
curl http://127.0.0.1:8000/apks/api/upload/ --upload-file <path-to-file>
```


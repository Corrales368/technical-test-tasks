# Task app
This project in a system to manage tasks.



## Environment Variables

Before you start, you must supply enviroment variables. I give you freedom to complete the .env file. **Some variables are options as long as you run the app in _dev_ mode**; because in dev, the database is sqlite.

`SECRET_KEY` 

`DEBUG`

## Usage

To deploy this project run with docker.

```bash
  docker build -t task-app .
  docker run -t -i -p 8000:8000 task-app 
```

or if you prefer "old school". 🤔

```bash
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
```


## About development

## Feedback

If you have any feedback, please reach out to us at santi368444110@gmail.com



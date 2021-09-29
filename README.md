# Eye


## How to install 🔧

Clone the repo in your PC

```
git clone https://github.com/zamu5/Eye.git
```

Install requirements

```
pip install requirements.txt
```

Run migrations

```
python manage.py migrate
```

Run server using port 8000

```
python manage.py runserver 8000
```

## How to use it 📦

The Eye have two functional endpoints:

#### Create a new event 

(localhost:8000/events/create) POST

This endpoint is used to add a new event to the queue, once the project have resources, it starts getting elements from the queue and create register of Model Event for each register.

the body of the request must be with the next format, the data key could be different because it gonna be save it as a json field, so it doesn't matter the info or structure inside this key. The other keys must be strings and must be the same key name as the example
```
{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "cta click",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
    "element": "chat bubble"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
```

#### Get events 
(localhost:8000/events/list) GET

This endpoint is used to request a list of events using a json format in the request, in the order to get events the user could use a session_id, a category or a time range. so the body of the reques could have the 3 filters or only one.

```
{
    "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
    "category": "page interaction",
    "since": "2021-01-01",
    "until": "2021-01-02"
}
```


* **Sergio Zamudio** - [zamu5](https://github.com/zamu5)

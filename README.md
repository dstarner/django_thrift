# Django Thrift

Run an Apache Thrift RPC Server through Django.

## Installation

Install with pip.

```bash
pip install django-thrift
```

## Configuration

To configure the application, you will need to add `django_thrift` to your `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'django_thrift',
]
```

You will also need to include the location and service name for your Thrift File. This also goes in `settings.py`

```python
THRIFT = {
    "FILE": "pingpong.thrift",
    "SERVICE": "PingPong"
}
```

## Mapping Thrift Function to Python

To map a Thrift function to our Django application, we will use a *Service Handler*. In our `views.py` function we can set up one of our routes like so.

```python
from django_thrift.handler import create_handler


handler = create_handler()  # Create the service handler that maps


@handler.map_function("ping")  # Maps the `ping_handler` function to Thrift `ping` 
def ping_handler():
    return "pong"
```

## Management

To run the RPC Server, run the following command. Note that you will need the `DJANGO_SETTINGS_MODULE` defined so that Django Thrift can load the correct settings.

```bash
./manange.py runrpcserver
```

## Deployment

To deploy the RPC server to production, use [`gunicorn_thrift`](https://github.com/eleme/gunicorn_thrift) with the command below...

```bash
gunicorn_thrift django_thrift.server.rpc:APP
```

## Example

```python
service PingPong {
    string ping(),
}
```

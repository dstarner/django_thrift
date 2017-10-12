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

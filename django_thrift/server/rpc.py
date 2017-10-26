import importlib
import os
import warnings

import django
from django.conf import settings
from django_thrift.handler import create_handler
from django_thrift.file import thrift_module as THRIFT_MODULE

import thriftpy
from thriftpy.protocol import TBinaryProtocolFactory
from thriftpy.server import TThreadedServer
from thriftpy.thrift import TProcessor, TClient
from thriftpy.transport import (
    TBufferedTransportFactory,
    TServerSocket,
    TSSLServerSocket,
    TSocket,
    TSSLSocket,
)

if not os.getenv("DJANGO_SETTINGS_MODULE", None):
    raise ValueError("'DJANGO_SETTINGS_MODULE' environment variable must exist!")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


def create_processor():
    """Creates a Gunicorn Thrift compatible TProcessor"""
    service = getattr(THRIFT_MODULE, settings.THRIFT["SERVICE"])

    for app in [x for x in settings.INSTALLED_APPS if not x.startswith("django")]:
        importlib.import_module("%s.views" % app)

    return TProcessor(service, create_handler())


def make_server(host="localhost", port=9090, unix_socket=None,
                proto_factory=TBinaryProtocolFactory(),
                trans_factory=TBufferedTransportFactory(),
                client_timeout=3000, certfile=None):
    """Creates a Thrift RPC server and serves it with configuration"""
    processor = create_processor()

    if unix_socket:
        server_socket = TServerSocket(unix_socket=unix_socket)
        if certfile:
            warnings.warn("SSL only works with host:port, not unix_socket.")
    elif host and port:
        if certfile:
            server_socket = TSSLServerSocket(
                host=host, port=port, client_timeout=client_timeout,
                certfile=certfile)
        else:
            server_socket = TServerSocket(
                host=host, port=port, client_timeout=client_timeout)
    else:
        raise ValueError("Either host/port or unix_socket must be provided.")

    server = TThreadedServer(processor, server_socket,
                             iprot_factory=proto_factory,
                             itrans_factory=trans_factory)

    print('Starting Thrift RPC server running @ %s:%s' % (host, port))

    try:
        server.serve()
    except KeyboardInterrupt:
        print()
        print("Stopping Server from Keyboard Interruption")
        exit()


APP = create_processor()

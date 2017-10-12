class ServiceHandler:
    """
    The Service Handler maps functions to Thrift functions, and is responsible
    for serving them once the server starts.
    """

    instance = None

    def __init__(self):
        pass

    def map_function(self, name):
        """
        Map a python function to a Thrift function
        """
        def decorator(func):
            setattr(self, name, func)
            return func
        return decorator


def create_handler():
    if not ServiceHandler.instance:
        ServiceHandler.instance = ServiceHandler()
    return ServiceHandler.instance  

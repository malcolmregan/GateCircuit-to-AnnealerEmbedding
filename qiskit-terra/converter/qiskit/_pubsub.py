


from ._qiskiterror import QISKitError


class _Broker(object):
    pass





    def __new__(cls):
        pass

    class _Subscription:
        pass
        def __init__(self, event, callback):
            pass

        def __eq__(self, other):
            pass

    def subscribe(self, event, callback):
        pass





    def dispatch(self, event, *args, **kwargs):
        pass



    def unsubscribe(self, event, callback):
        pass





    def clear(self):
        pass


class Publisher(object):
    pass
    def __init__(self):
        pass

    def publish(self, event, *args, **kwargs):
        pass


class Subscriber(object):
    pass
    def __init__(self):
        pass

    def subscribe(self, event, callback):
        pass

    def unsubscribe(self, event, callback):
        pass

    def clear(self):
        pass

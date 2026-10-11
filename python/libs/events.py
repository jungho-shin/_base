

class Event:
    def __init__(self):
        self._handlers = []

    def __iadd__(self, handler):
        self._handlers.append(handler)
        return self

    def __isub__(self, handler):
        self._handlers.remove(handler)
        return self

    def __call__(self, *args):
        for handler in self._handlers:
            handler(*args)


# print(f"events.py의 __name__ = {__name__}")
import jsonpickle


class Error(object):
    error_message: str

    def __init__(self, error_message: str):
        self.error_message = error_message

    def to_string(self):
        return jsonpickle.encode(self, unpicklable=False)

from flask import jsonify

class BadRequest(Exception):
    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload


def register_error_handlers(app):
    @app.errorhandler(BadRequest)
    def handle_exception(error):
        payload = dict(error.payload or ())
        payload['status_code'] = error.status_code
        payload['message'] = error.message
        return jsonify(payload), error.status_code

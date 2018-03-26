from pyramid.view import exception_view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound
from forecast_service.utils.error_handler import ErrorHandler


@exception_view_config(HTTPNotFound)
def failed_validation(request):
    response = Response("404 Not Found")
    response.status_int = 404
    return response


def generate_bad_request():
    from pyramid.response import Response
    msg = ErrorHandler.get_error()
    response = Response()
    response.json = msg
    response.status_code = 400
    return response

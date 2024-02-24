from rest_framework.views import exception_handler


def exception_handler_with_http_code(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data["code"] = response.status_code
    return response


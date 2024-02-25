from constants.status import STATUS
from rest_framework.exceptions import (
    APIException,
    NotAuthenticated,
    NotFound,
    PermissionDenied,
    Throttled,
)


class CustomBaseException(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code


class InvalidRequest(CustomBaseException):
    def __init__(self, detail):
        super().__init__(detail=detail, code=STATUS.BAD_REQ)


class NotAuthenticated(NotAuthenticated):
    def __init__(self, detail=None):
        if detail is None:
            detail = "You are not authorized to perform this action!"
        super().__init__(detail=detail, code=STATUS.NO_AUTH)


class PermissionError(PermissionDenied):
    def __init__(self, detail=None):
        if detail is None:
            detail = "You do not have the permission to perform this operation!"
        super().__init__(detail=detail, code=STATUS.PERMISSION_ERROR)


class ResourceNotFound(NotFound):
    def __init__(self, detail=None):
        if detail is None:
            detail = "The requested resource is not available!"
        super().__init__(detail=detail, code=STATUS.NOT_FOUND)


class RateLimitReached(Throttled):
    def __init__(self, detail=None):
        if detail is None:
            detail = "Too many requests! Please try again after some time!"
        super().__init__(detail=detail, code=STATUS.RATE_LIMIT)


class ServerError(CustomBaseException):
    def __init__(self):
        detail = "Something went wrong.. Please try again!"
        super().__init__(detail=detail, code=STATUS.SERVER_ERROR)

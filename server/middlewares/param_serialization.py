from rest_framework.exceptions import ValidationError
from utils.logman import logman

class ParamSerializerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        _parsed = False
        if hasattr(view_func, 'param_serializer'):
            param_serializer_class = getattr(view_func, 'param_serializer')

            # Get request query params
            params = request.query_params

            # Validate and parse the query params using the serializer
            serializer = param_serializer_class(data=params)
            try:
                serializer.is_valid(raise_exception=True)
                # If valid, parsed data will be available in serializer.validated_data
                parsed_params = serializer.validated_data
                _parsed = True
                request.parsed_params = parsed_params
            except ValidationError as e:
                request.parsed_params = {"_error": str(e)}
                logman.exception(msg=f"Param parsing error")
        else:
            request.parsed_params = {}

        # Assign boolean value directly without converting to string
        request.parsed_params['_parsed'] = _parsed # type: ignore

from django.urls import resolve
from rest_framework import status
from rest_framework.response import Response


class ParamSerializerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver_match = resolve(request.path)
        view_func = resolver_match.func

        # Extract the class-based DRF view
        view_class = getattr(view_func, "view_class", None)

        if view_class and hasattr(view_class, "param_serializer_class"):
            param_serializer_class = view_class.param_serializer_class

            # Validate request query params using the serializer
            serializer_instance = param_serializer_class(data=request.GET)
            if serializer_instance.is_valid():
                request.cleaned_params = (
                    serializer_instance.validated_data
                )  # Attach validated data to request
            else:
                return Response(
                    {"error": serializer_instance.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return self.get_response(request)

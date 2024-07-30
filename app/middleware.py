from django.http import HttpResponseBadRequest
from django.utils.deprecation import (
    MiddlewareMixin,
)


class ApiVersionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.supported_versions = {"v1", "v2"}  # Define supported versions

    def __call__(self, request):
        api_version = request.META.get(
            "HTTP_API_VERSION", "v1"
        )  # Default to v1 if not specified

        print(api_version)

        if api_version not in self.supported_versions:
            return HttpResponseBadRequest("Invalid API version")

        request.api_version = api_version

        response = self.get_response(request)
        return response

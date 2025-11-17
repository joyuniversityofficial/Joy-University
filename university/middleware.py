import sys
import os

class BrokenPipeErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except BrokenPipeError:
            # Client disconnected, silently ignore
            pass

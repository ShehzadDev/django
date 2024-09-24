import time


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response

    def process_request(self, request):
        request.start_time = time.time()
        request.custom_message = f"Hello, this is a custom message from middleware!"

    def process_response(self, request, response):
        if hasattr(request, "start_time"):
            duration = time.time() - request.start_time
            response["X-Processing-Time"] = f"{duration:.2f} seconds"
        return response

    def process_exception(self, request, exception):
        print(f"Exception occurred: {exception}")

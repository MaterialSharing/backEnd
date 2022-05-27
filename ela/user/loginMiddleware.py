class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("LoginMiddleware init")

    def __call__(self, request):
        path = request.path
        print("url:", path)
        response = self.get_response(request)
        return response

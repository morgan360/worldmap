class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("CORS Middleware activated")  # Log to confirm activation
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "app://obsidian.md"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Origin, Content-Type, Accept"
        return response

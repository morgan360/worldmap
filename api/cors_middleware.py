class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Add the necessary CORS headers here
        response["Access-Control-Allow-Origin"] = "app://obsidian.md"  # or "*" for a less secure but more flexible approach
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Origin, Content-Type, Accept"
        return response

import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle CORS headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Parse query parameters
        query_params = urllib.parse.parse_qs(self.path[7:])  # Ignore '/api?'
        
        # Get the names from query parameters (e.g., name=X&name=Y)
        names = query_params.get('name', [])
        marks = [self.get_marks(name) for name in names]
        
        # Respond with the marks
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def get_marks(self, name):
        # Replace this with your actual marks data lookup
        data = {
            "X": 10,
            "Y": 20,
            # Add more names and marks as needed
        }
        return data.get(name, "Not found")  # Return "Not found" if name doesn't exist

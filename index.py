import json
import os
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler

# Load the student marks from a JSON file (or embed them directly)
STUDENT_MARKS = [
    [{"name":"LYxs","marks":88},{"name":"mA","marks":23},{"name":"uB5ho","marks":87},{"name":"H","marks":81},{"name":"3","marks":62},{"name":"65ekYL","marks":48},{"name":"c8HQc","marks":88},{"name":"ZRVTaeuAkD","marks":9},{"name":"C","marks":98},{"name":"YH0N0","marks":59},{"name":"0MahLb","marks":13},{"name":"ZQ6MeKKxxz","marks":69},{"name":"MOHGKdz","marks":98},{"name":"dgW","marks":7},{"name":"1","marks":61},{"name":"2rPjITQM","marks":97},{"name":"bsd","marks":67},{"name":"yJr","marks":13},{"name":"nlwI1","marks":38},{"name":"iM","marks":26},{"name":"uQ","marks":71},{"name":"v84e","marks":90},{"name":"SY0Yn2","marks":41},{"name":"4dsBfpL","marks":4},{"name":"Z","marks":28},{"name":"CUmK","marks":15},{"name":"7drQ","marks":91},{"name":"6WPWGo","marks":61},{"name":"U","marks":46},{"name":"06ruU0C32","marks":40},{"name":"QQoUK","marks":18},{"name":"T0hFYx55A","marks":74},{"name":"Qj9","marks":52},{"name":"1wR","marks":38},{"name":"ONCL5KEXyg","marks":22},{"name":"D2LY","marks":69},{"name":"RHoRP","marks":62},{"name":"NJKn9ykU0Y","marks":14},{"name":"lmvK","marks":23},{"name":"IQyblYYE","marks":98},{"name":"czY","marks":11},{"name":"rWTxctQA","marks":85},{"name":"CX","marks":0},{"name":"bRHLn","marks":23},{"name":"uu","marks":91},{"name":"lJI","marks":75},{"name":"6wa","marks":29},{"name":"h1AKC","marks":88},{"name":"AUZ","marks":80},{"name":"mA81ZecL","marks":86},{"name":"JV","marks":65},{"name":"y","marks":74},{"name":"DpUveB3eF0","marks":6},{"name":"bWY","marks":43},{"name":"LDrr","marks":39},{"name":"cCoZX1f","marks":1},{"name":"ahlo3","marks":97},{"name":"b","marks":23},{"name":"EezOm0","marks":94},{"name":"8n","marks":31},{"name":"ay2id4x8y","marks":64},{"name":"uIN05","marks":4},{"name":"t7Ij","marks":24},{"name":"Env1kaBR","marks":41},{"name":"mh55R8AZzi","marks":85},{"name":"Hg8R4d0jq","marks":59},{"name":"a6nEcS4d","marks":48},{"name":"o4","marks":13},{"name":"Ps","marks":37},{"name":"BQaKCT","marks":55},{"name":"VXPx1U7i","marks":21},{"name":"Jk","marks":54},{"name":"W6qE3","marks":17},{"name":"4Jc","marks":7},{"name":"RTPhlUx","marks":68},{"name":"cAZTjIjZrM","marks":96},{"name":"ozK8qU","marks":28},{"name":"3","marks":5},{"name":"q","marks":82},{"name":"SmnTt5tNl","marks":83},{"name":"1QFJ8HkQ","marks":90},{"name":"IySbnat5H","marks":34},{"name":"l22nI","marks":73},{"name":"oxTupdA","marks":80},{"name":"sGzbIaB","marks":91},{"name":"MTJcRLjko","marks":52},{"name":"ranyBLmV6w","marks":48},{"name":"XqxiGgQkcq","marks":0},{"name":"6GFD","marks":12},{"name":"l9g0CXtm","marks":35},{"name":"AiWs2e","marks":51},{"name":"lh","marks":5},{"name":"C","marks":97},{"name":"MYXKt20CkS","marks":18},{"name":"O","marks":12},{"name":"Ih8xyQd","marks":31},{"name":"gDA","marks":13},{"name":"G","marks":83},{"name":"2wfZwK0A","marks":80},{"name":"DXr","marks":68}]
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = parse_qs(self.path.split('?')[-1])
        names = query.get("name", [])

        # Find marks for requested names
        marks_list = [entry["marks"] for entry in STUDENT_MARKS if entry["name"] in names]

        # Construct response
        response = json.dumps({"marks": marks_list})

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

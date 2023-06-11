from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("${{ values.path }}/hello_world", methods=["GET"])
def hello_world():
    return "hello from ${{ values.entity_name | lower | replace(' ','-')}}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

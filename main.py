from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from koinu import conv2
import os

app = Flask(__name__)
CORS(app)


@app.route('/api/option/<string:NLPSymbol>', methods=["POST", "GET"])
def nlp(NLPSymbol):
    print(NLPSymbol)  # デバック用
    return jsonify(conv2(NLPSymbol))


def main():
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == '__main__':
    main()

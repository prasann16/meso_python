from flask import Flask, request, jsonify
import get_summary

app = Flask(__name__)

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    prediction = get_summary.get_summary(text)
    return jsonify({'result':prediction})


if __name__ == '__main__':
    app.run(port=5000, debug=True)

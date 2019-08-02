from flask import Flask, request, jsonify
import model

app = Flask(__name__)

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    prediction = model.get_summary(text)
    return jsonify({'result':prediction})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

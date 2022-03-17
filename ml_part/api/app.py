from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
@app.route("/home", methods=["POST"])
def home():
    post_data = request.form['data']
    print(post_data)  
    return f"Hello - {post_data}"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("API2: ได้รับคำขอจาก API1")
    return "สวัสดีจาก API2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

from flask import Flask
from routes.bd_cad import bd_bp

app = Flask(__name__)

app.register_blueprint(bd_bp, url_prefix='/bd')

@app.route('/')
def home():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
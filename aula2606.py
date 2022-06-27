from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello! Yara, Manu, Alana, Lari e Liriel'

app.run(host="0.0.0.0", debug=True)

# cmd: ip addr
# ip: http://191.52.7.73:5000
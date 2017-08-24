from flask import Flask, request, jsonify
app = Flask(__name__)

port = 4000
ip = "192.168.1.2"

@app.route('/it')
def ciao():
	return "Buongiorno!\n"

@app.route('/hola')
def name():
	name = request.args.get('name')
	return "Hola %s!\n" % name

@app.route('/login', methods=['POST'])
def login():
	username = request.form.get('username')
	password = request.form.get('password')
	return "Login successful for %s:%s\n" % (username, password)


app.run(ip, port)


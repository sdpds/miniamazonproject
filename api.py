##hello
from flask import Flask,render_template,request
app = Flask(__name__)  ##dunder method

@app.route('/') ##Decorators
#def hello_world():
	#return 'Hello, World!'

def home():
	return render_template('home.html')    

@app.route('/about') ##Decorators
def about():
	#return 'My name is Subhradip'
	return render_template('about.html')

@app.route('/contact') ##Decorators
def contact():
	#return 'My Contact is 96XXXXXX39'
	return render_template('contact.html') 

@app.route('/login',methods=['POST']) ##Decorators
def login():
	user = {'username' : 'Subhradip', 'password': 'password'}
	username = request.form['username']
	password = request.form['password']

	if user['username'] == username:
		if user['password'] == password:
			return "login succesful!"
		return "password doesn't match"
	return"username doesn't match"
			

app.run(debug=True) #if it is appr.run() then the debugger will be off. debug=True means debugger mode will be on in terminal
from flask import Flask
app=Flask(__name__)
app.config["DEBUG"]=True
@app.route("/")
@app.route("/hello")
def hello_world():
	return "HELLO WORLD ! I LOVE YOU !"
@app.route("/test/<search_query>")
def search(search_query):
	return search_query
@app.route("/integer/<int:value>")
def int_type(value):
	print(value+1)
	return("I I 143")
@app.route("/float/<float:value>")
def float_type(value):
	print(value+1)
	return "I love ...."
@app.route("/path/<path:value>")
def path_typ(value):
	print(value)
	return "correct"
@app.route("/name/<name>")
def index(name):
	if name.lower()=="michael":
		return "Hello ,{}".format(name), 200
	else:
		return "not found",404
if __name__=="__main__":
	app.run()

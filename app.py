# from flask import Flask

# app=Flask(__name__)

# import random
# from random import randit



# @app.route("/hello")
# def hello():
# 	return "Hello World!"

# @app.route("/Goodbye")
# def Goodbye():
# 	return "Goodbye!"
# @app.route("/")
# def index():
# 	return "My name is em ellol"
# if __name__=="__main__":
# 	app.run(port=4000, debug=True)

	
# 	
from flask import Flask, render_template
# import random
app=Flask(__name__)
@app.route("/web")
# def quote():
# 	h=["my name is Hala","I am 15","my fav color is blue"]
# 	x=(random.choice(h))
# 	return x
def num():
	return render_template("mywebsite.html")

if __name__=="__main__":
	app.run(port=7000, debug=True)
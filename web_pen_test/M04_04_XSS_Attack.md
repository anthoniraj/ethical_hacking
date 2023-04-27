# Cross-site scripting (or XSS) Attack
- Author: `Anthoniraj Amalanathan`

## Cross-site scripting (or XSS) 
- Cross Site Scripting attack means sending and injecting malicious code or script. Malicious code is usually written with client-side programming language like Javascript.

## Prerequisites
- Python Flask Application 
- Simple HTML Page with Jinja Template
- Javascript Alert and HTML Image Tag 

## Types of XSS attacks
- There are a few methods by which XSS can be manipulated:

|Type|Origin|Description|
| -------- | ------- |---------|
|Stored|Server|The malicious code is inserted in the application (usually as a link) by the attacker. The code is activated every time a user clicks the link.|
|Reflected|	Server|	The attacker delivers a malicious link externally from the vulnerable web site application to a user. When clicked, malicious code is sent to the vulnerable web site, which reflects the attack back to the user’s browser.|
|DOM-based|Client|The attacker forces the user's browser to render a malicious page. The data in the page itself delivers the cross-site scripting data.|


## HTML Script
	```html
	<!DOCTYPE html>
	{% autoescape false %} <!-- This should be true for Preventing XSS Attack-->
	<html lang="en">
	<head>
	    <title>XSS Demo</title>
	</head>
	<body>
	    <h1>Hi {{ name }}</h1>
	</body>
	</html>
	{% endautoescape %}
	```

## Flask App (app.py)
	```python
	from flask import Flask, render_template, request

	app = Flask(__name__)

	@app.route("/")
	def home():
	    return "<h1>Welcome Page</h1>"

	@app.route("/greet")
	def greet():
	    value = request.args.get('name')
	    return render_template('greet.html', name = value)

	if __name__ == '__main__':
	    app.run(host="0.0.0.0",port=8080, debug=True)
	```

## XSS Attack
- Start the Flask Server `python app.py`
- Access the Web Page `http://127.0.0.1:8080/greet`
- Access the page with value `http://127.0.0.1:8080/greet?name=Anthoniraj`
- Access the page with Script
`http://127.0.0.1:8080/greet?name=<script>alert('Code Injected!');</script>`
- Access the page with HTML Elements
`http://127.0.0.1:8080/greet?name=Anthoniraj<br><img src="https://picsum.photos/200/300">`

## Prevention
- To prevent XSS Attack, Enable auto escape in HTML Page using Jinja Templates
	```html
	{% autoescape true %}
		html script
	{% endautoescape %}
	```
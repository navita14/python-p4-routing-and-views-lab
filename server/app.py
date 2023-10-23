#!/usr/bin/env python3

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():
    #Your index() view should be routed to at the base URL with /.
    #It should Contain an h1 element that contains the title of this
    body = '<h1>Python Operations with Flask Routing and Views</h1>'
    return make_response(body, 200) #make_response is not needed. flask will do it for you
    #make response only needed if you are passing a configuration option through it

@app.route('/print/<param>')
def print_string(param):
    #A print_string view should take one parameter, a string. 
    #It should print the string in the terminal and display it in the web browser. 
    #Its URL should be of the format /print/parameter
    print(param)
    return make_response(param,200)

@app.route('/count/<int:x>')
def count(x):
    body = ''
    #A count() view should take one parameter, an integer. 
    #It should display all numbers in the range of that parameter on separate lines. 
    #Its URL should be of the format /count/parameter.
    for num in range(0, x):#dont need to put 0 as 0 always in defined. you need to enter 1/ range excludes the stop function why is 10
        body += f'{num}<br />'
    return body, 200


@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    body = ''
    #A math() view should take three parameters: num1, operation, and num2. 
    #It must perform the appropriate operation on the two numbers in the order that they are presented. 
    #The included operations should be: +, -, *, div (/ would change the URL path), and %. 
    #Its URL should be of the format /math/<num1><operation><num2>
    print(num1, operation, num2)
    if operation  == '+':
        body = num1 + num2
    elif operation  == '-':
        body = num1 - num2
    elif operation  == '*':
        body = num1 * num2
    elif operation  == '%':
        body = num1 % num2
    else:
        body = ''
    return str(body), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

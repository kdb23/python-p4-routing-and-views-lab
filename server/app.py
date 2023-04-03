#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print (param)
    return f'{param}'

@app.route('/count/<int:number>')
def count_parameter(number): 
    output = ''
    for i in range(0, number):
        output += str(i) + '\n'
    return output

# A math() view should take three parameters: num1, operation, and num2. It must perform the appropriate operation on the two numbers in the order that they are presented. The included operations should be: +, -, *, div (/ would change the URL path), and %. Its URL should be of the format /math/<num1><operation><num2>

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation =='*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid Operation'
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

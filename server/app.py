#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''displays "Python Operations with Flask Routing and Views" in h1 in browser.'''
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string (parameter):
    '''displays text of route in browser.'''
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    '''counts through range of parameter in "/count/<parameter" on separate lines.'''
    return '\n'.join([str(i) for i in range(int(parameter))])

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    '''performs math operation on num1 and num2 and displays result.'''
    if operation == '+':
        return str(int(num1) + int(num2))
    elif operation == '-':
        return str(int(num1) - int(num2))
    elif operation == '*':
        return str(int(num1) * int(num2))
    elif operation == 'div':
        return str(int(num1) / int(num2))
    
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

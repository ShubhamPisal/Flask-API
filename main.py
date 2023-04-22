from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if(sum == copy_n):
        result = {
            "Number":copy_n,
            "Armstrong":True,
            "Appowner":"SHUBHAM"
        } 

    else:
        result = {
            "Number":copy_n,
            "Armstrong":False,
            "Appowner":"SHUBHAM"
        }
    return jsonify(result)

@app.route('/evenodd/<int:n>')
def evenodd(n):
    number = n
    if(number % 2 == 0):
        result = {
            "Number":n,
            "Even":False,
            "Appowner":"SHUBHAM"
        } 

    else:
        result = {
            "Number":n,
            "Even":True,
            "Appowner":"SHUBHAM"
        } 
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True ,port = 8000)

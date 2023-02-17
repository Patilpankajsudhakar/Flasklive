from flask import Flask,request
app=Flask(__name__)

# route 
@app.route("/")
def hello_world():
    return "Hello world"

@app.route('/aboutus')
def aboutus():
    return "we are ineuron"

@app.route('/demo',methods=['POST'])
def math_operation():
    if (request.method=="POST"):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=0
        
        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=="division":
            result=num1/num2
        

        return "The operation is {} and the result is {}".format(operation,result)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
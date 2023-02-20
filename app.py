from flask import Flask,request,render_template
app=Flask(__name__)

# route 
@app.route("/")
def hello_world():
    return render_template("index.html")

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
        else:
            result=num1-num2
            
        return "The operation is {} and the result is {}".format(operation,result)

    
@app.route('/operation',methods=['POST'])
def math_operation_1():
    if (request.method=="POST"):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0
        
        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=="division":
            result=num1/num2
        else:
            result=num1-num2
            
        return render_template("result.html",result=result)
#Discount calculatior    
@app.route("/discount_count",methods=["POST"])
def discount_count():
    if (request.method=="POST"):
        item1=int(request.form["item1"])
        item2=int(request.form["item2"])
        item3=int(request.form["item3"])
        item4=int(request.form["item4"])
        item5=int(request.form["item5"])
        Totalcost=item1+item2+item3+item4+item5
        result=0
        if Totalcost <=1000:
            discount_onitem=Totalcost*0.10
            result=Totalcost-discount_onitem
        elif Totalcost >1000 and Totalcost <=2000:
            discount_onitem=Totalcost*0.20
            result=Totalcost-discount_onitem
        elif Totalcost>2000:
            discount_onitem=Totalcost*0.30
            result=Totalcost-discount_onitem
        else:
            result= Totalcost
            discount_onitem="NO discount"
        return render_template("result.html",result=result)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
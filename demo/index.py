from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient
import itertools
import re
import json

def connect():
    # Substitute the 5 pieces of information you got when creating
    # the Mongo DB Database (underlined in red in the screenshots)
    # Obviously, do not store your password as plaintext in practice
    client = MongoClient('mongodb://localhost:27017/')
    db = client.hb
    #handle.authenticate("demo-user","12345678")
    return db

app = Flask(__name__)
db = connect()



# Bind our index page to both www.domain.com/ 
#and www.domain.com/index
@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    print "hg"
    userinputs = [x for x in db.product.find()]
    return render_template('index.html', userinputs=userinputs)



@app.route('/ret',methods=['GET','POST'])
def ret():
    item1=request.form.get("bn")
    print item1
    item=request.form.get("item")
    #k=db.product.find()
    #k={}
    #k=db.product.find({'name': {'$regex': "$item",'$options':"$i"}})
    g=db.product.find({"$and" : [{'Name': {'$regex': item,'$options':"$i"}},{'type':item1}]})
    pipes=[pipe for pipe in g ]
    #pipes=[pipe for pipe in db.product.find( {[ {{'Name': {'$regex': item,'$options':"$i"}}, {'type':item1}} ] } )]
    return render_template('ret.html', pipes=pipes)


@app.route('/map/<prod>',methods=['GET','POST'])
def map(prod):
    prod = prod.replace("ZZZZZ",'/')
    pipes=[pipe for pipe in db.product.find({'Name':prod})]
    p = pipes[0]
    strr = p['Details']
    strr = strr.replace("u'", "'").replace("'", '"')
    d = json.loads(strr)
    return render_template('map.html',pipes=pipes,prod=prod, p=p, d=sorted(d.items()))



@app.route('/map/compare/<serial>',methods=['GET','POST'])

def compare(serial):
    print serial
    vens=[ven for ven in db.vendors.find({'SerialN':serial})]
    price=[i['Price'] for i in vens]
    if len(price) == 0:
	return render_template('apology.html')
    
    k=min(price)
    #print k
    n=[j for j in vens if j['Price']==k]
    r=[j['Ratings'] for j in vens]
    l=[]
    for rt in r:
        if(rt!="Not Available"):
         l.append(rt.split(" ")[0])
    #print l
    t=max(l)
    #print t
    #print t+ " out" +" of" +" 5" +" stars"
    t1=[j for j in vens if j['Ratings'] == t+ " out" +" of" +" 5" +" stars"]
    print t1
    #print n
    #print len(vens)
    p=len(vens)
    if(p==0):
        return render_template('../apology.html',p=p)
    else:
        return render_template('compare.html',vens=vens,p=p,n=n,t1=t1)


@app.route("/analytic", methods=['POST'])
def analytic():
    return render_template('analytic.html')


@app.route("/write", methods=['POST'])
def write():
    userinput = request.form.get("userinput")
    oid = db.product.insert({"message":userinput})
    return redirect ("/")

@app.route("/deleteall", methods=['GET'])

def deleteall():
    handle.product.remove()
    return redirect ("/")

# Remove the "debug=True" for production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 9007))

    app.run(host='0.0.0.0', port=port, debug=True)

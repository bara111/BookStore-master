from flask import Flask,request,redirect

app = Flask(__name__)

@app.route('/buy/dos/id',methods=['GET'])
def buyDos():
    id = request.args.get("id", "")
    return redirect("http://bara1111.pythonanywhere.com/buy/dos/id?id="+str(id)) #call request when handling buy request of DOS book
@app.route('/buy/graduateSchool/id',methods=['GET'])
def buyGraduateSchool():
    id = request.args.get("id", "")
    return redirect("http://bara1111.pythonanywhere.com/buy/graduateSchool/id?id="+str(id)) #call request when handling buy request of graduateSchool book

if __name__=="__main__":
        app.debug = False
        app.run(host = '0.0.0.0',port=5000)

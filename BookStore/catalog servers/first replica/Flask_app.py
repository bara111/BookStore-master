import os
import json
from flask import Flask,request,redirect


def readDistributedSystemsFile(): #read DOS files
    dataForDosBooks = {}
    namesForDosBooks=[]
    quantitysForDosBooks=[]
    idsForDosBooks=[]
    dataForDosBooks['book'] = []
    f = open("/home/bara111/FlaskApp/distributed_systems.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_distributed_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_distributed_systems.txt", "r")

    for x in f:
        namesForDosBooks.append(x)
    for n in m:
        quantitysForDosBooks.append(n)
    for g in t:
        idsForDosBooks.append(g)
    for i in range(len(namesForDosBooks)):
        dataForDosBooks['book'].append({'name': namesForDosBooks[i],'quantity':quantitysForDosBooks[i],'id':idsForDosBooks[i]})




def readGraduateSchoolFile():  #read graduateSchool files
    dataForGraduateSchool = {}
    namesForGraduateSchool=[]
    quantitysForGraduateSchool=[]
    idsForGraduateSchool=[]
    dataForGraduateSchool['book'] = []
    f = open("/home/bara111/FlaskApp/graduate_school.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_graduate_school_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_graduate_school.txt", "r")

    for x in f:
        namesForGraduateSchool.append(x)
    for n in m:
        quantitysForGraduateSchool.append(n)
    for g in t:
        idsForGraduateSchool.append(g)
    for i in range(len(namesForGraduateSchool)):
        dataForGraduateSchool['book'].append({'name': namesForGraduateSchool[i],'quantity':quantitysForDosBooks[i],'id':idsForGraduateSchool[i]})

app=Flask(__name__)
@app.route('/search/dos',methods=['GET']) #handle search by DOS catagory
def dos():
    dataForDosBooks = {}
    namesForDosBooks=[]
    quantitysForDosBooks=[]
    idsForDosBooks=[]
    dataForDosBooks['book'] = []
    f = open("/home/bara111/FlaskApp/distributed_systems.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_distributed_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_distributed_systems.txt", "r")

    for x in f:
        namesForDosBooks.append(x)
    for n in m:
        quantitysForDosBooks.append(n)
    for g in t:
        idsForDosBooks.append(g)
    for i in range(len(namesForDosBooks)):
        dataForDosBooks['book'].append({'name': namesForDosBooks[i],'quantity':quantitysForDosBooks[i],'id':idsForDosBooks[i]})
    dataDos={}
    dataDos['book'] = []
    name = request.args.get("dos", "")
    nameFormated = "{}".format(name)
    for i in range(len(namesForDosBooks)):
        if(nameFormated in namesForDosBooks[i]):
                dataDos['book'].append({'name': namesForDosBooks[i],'quantity':quantitysForDosBooks[i],'id':idsForDosBooks[i]})
    return dataDos

@app.route('/search/graduateSchool',methods=['GET']) #handle search by graduateSchool catagory
def graduateSchool():
    dataForGraduateSchool = {}
    namesForGraduateSchool=[]
    quantitysForGraduateSchool=[]
    idsForGraduateSchool=[]
    dataForGraduateSchool['book'] = []
    f = open("/home/bara111/FlaskApp/graduate_school.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_graduate_school_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_graduate_school.txt", "r")

    for x in f:
        namesForGraduateSchool.append(x)
    for n in m:
        quantitysForGraduateSchool.append(n)
    for g in t:
        idsForGraduateSchool.append(g)
    for i in range(len(namesForGraduateSchool)):
        dataForGraduateSchool['book'].append({'name': namesForGraduateSchool[i],'quantity':quantitysForGraduateSchool[i],'id':idsForGraduateSchool[i]})
    dataGD={}
    dataGD['book'] = []
    name = request.args.get("graduateSchool", "")
    nameFormated = "{}".format(name)
    for i in range(len(namesForGraduateSchool)):
        if(nameFormated in namesForGraduateSchool[i]):
                dataGD['book'].append({'name': namesForGraduateSchool[i],'quantity':quantitysForGraduateSchool[i],'id':idsForGraduateSchool[i]})
    return dataGD
@app.route('/search/id',methods=['GET']) #handle search by ID catagory
def id():
    dataForDosBooks = {}
    namesForDosBooks=[]
    quantitysForDosBooks=[]
    idsForDosBooks=[]
    dataForDosBooks['book'] = []
    f = open("/home/bara111/FlaskApp/distributed_systems.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_distributed_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_distributed_systems.txt", "r")

    for x in f:
        namesForDosBooks.append(x)
    for n in m:
        quantitysForDosBooks.append(n)
    for g in t:
        idsForDosBooks.append(g)
    for i in range(len(namesForDosBooks)):
        dataForDosBooks['book'].append({'name': namesForDosBooks[i],'quantity':quantitysForDosBooks[i],'id':idsForDosBooks[i]})
    dataForGraduateSchool = {}
    namesForGraduateSchool=[]
    quantitysForGraduateSchool=[]
    idsForGraduateSchool=[]
    dataForGraduateSchool['book'] = []
    q = open("/home/bara111/FlaskApp/graduate_school.txt", "r")
    w = open("/home/bara111/FlaskApp/quantity_graduate_school_systems.txt", "r")
    e = open("/home/bara111/FlaskApp/id_graduate_school.txt", "r")

    for x in q:
        namesForGraduateSchool.append(x)
    for n in w:
        quantitysForGraduateSchool.append(n)
    for g in e:
        idsForGraduateSchool.append(g)
    for i in range(len(namesForGraduateSchool)):
        dataForGraduateSchool['book'].append({'name': namesForGraduateSchool[i],'quantity':quantitysForDosBooks[i],'id':idsForGraduateSchool[i]})

    dataGD={}
    dataGD['book'] = []
    id = request.args.get("id", "")
    idFormated = "{}".format(id)
    for i in range(len(namesForGraduateSchool)):
        if(idFormated in idsForGraduateSchool[i]):
                dataGD['book'].append({'name': namesForGraduateSchool[i],'quantity':quantitysForGraduateSchool[i],'id':idsForGraduateSchool[i]})
    for i in range(len(namesForDosBooks)):
        if(idFormated in idsForDosBooks[i]):
                dataGD['book'].append({'name': namesForDosBooks[i],'quantity':quantitysForDosBooks[i],'id':idsForDosBooks[i]})
    return dataGD

@app.route('/buy/graduateSchool/id',methods=['GET']) #handle buy from graduateSchool catagory
def buyGraduateSchoolId():
    dataForGraduateSchool = {}
    namesForGraduateSchool=[]
    quantitysForGraduateSchool=[]
    idsForGraduateSchool=[]
    dataForGraduateSchool['book'] = []
    f = open("/home/bara111/FlaskApp/graduate_school.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_graduate_school_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_graduate_school.txt", "r")

    for x in f:
        namesForGraduateSchool.append(x)
    for n in m:
        quantitysForGraduateSchool.append(n)
    for g in t:
        idsForGraduateSchool.append(g)
    for i in range(len(namesForGraduateSchool)):
        dataForGraduateSchool['book'].append({'name': namesForGraduateSchool[i],'quantity':quantitysForGraduateSchool[i],'id':idsForGraduateSchool[i]})
    index = -1
    quantitysGraduateSchool=[]
    m = open("/home/bara111/FlaskApp/quantity_graduate_school_systems.txt", "r")
    for n in m:
        quantitysGraduateSchool.append(n)
    id = request.args.get("id", "")
    idFormated = "{}".format(id)
    for i in range(len(namesForGraduateSchool)):
        data=idsForGraduateSchool[i]
        data=data[:-1]
        dataInt = int(data)
        idFormated=int(idFormated)
        if(dataInt == idFormated):
                index = i
    if (index != -1):
                dataWithEnter = quantitysGraduateSchool[index]
                dataFormated = dataWithEnter[:-1]
                dataFormatedInt = int(dataFormated)
                if(dataFormatedInt!=0):
                          dataFormatedInt = dataFormatedInt-1
                          FormatedStringAfterSale = str(dataFormatedInt)+"\n"
                          quantitysGraduateSchool[index] = FormatedStringAfterSale
                          f = open('/home/bara111/FlaskApp/quantity_graduate_school_systems.txt', 'w')
                          for i in range(len(namesForGraduateSchool)):
                               f.write(quantitysGraduateSchool[i])
                          f.close()
                          return redirect("http://bara1111.pythonanywhere.com/update/graduateSchool/id?id="+str(id)) #call request while buying is success to update other servers
                else:
                    return '{ "status":"fail"}'
@app.route('/update/graduateSchool/id',methods=['GET']) #handle update of graduateSchool catagory when buying from other servers
def updateGraduateSchoolId():
    dataForGraduateSchool = {}
    namesForGraduateSchool=[]
    quantitysForGraduateSchool=[]
    idsForGraduateSchool=[]
    dataForGraduateSchool['book'] = []
    f = open("/home/bara111/FlaskApp/graduate_school.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_graduate_school_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_graduate_school.txt", "r")

    for x in f:
        namesForGraduateSchool.append(x)
    for n in m:
        quantitysForGraduateSchool.append(n)
    for g in t:
        idsForGraduateSchool.append(g)
    for i in range(len(namesForGraduateSchool)):
        dataForGraduateSchool['book'].append({'name': namesForGraduateSchool[i],'quantity':quantitysForGraduateSchool[i],'id':idsForGraduateSchool[i]})
    index = -1
    quantitysGraduateSchool=[]
    m = open("/home/bara111/FlaskApp/quantity_graduate_school_systems.txt", "r")
    for n in m:
        quantitysGraduateSchool.append(n)
    id = request.args.get("id", "")
    idFormated = "{}".format(id)
    for i in range(len(namesForGraduateSchool)):
        data=idsForGraduateSchool[i]
        data=data[:-1]
        dataInt = int(data)
        idFormated=int(idFormated)
        if(dataInt == idFormated):
                index = i
    if (index != -1):
                dataWithEnter = quantitysGraduateSchool[index]
                dataFormated = dataWithEnter[:-1]
                dataFormatedInt = int(dataFormated)
                if(dataFormatedInt!=0):
                          dataFormatedInt = dataFormatedInt-1
                          FormatedStringAfterSale = str(dataFormatedInt)+"\n"
                          quantitysGraduateSchool[index] = FormatedStringAfterSale
                          f = open('/home/bara111/FlaskApp/quantity_graduate_school_systems.txt', 'w')
                          for i in range(len(namesForGraduateSchool)):
                               f.write(quantitysGraduateSchool[i])
                          f.close()
                          return '{ "status":"success"}'
                else:
                    return '{ "status":"fail"}'

@app.route('/buy/dos/id',methods=['GET']) #handle buy from DOS catagory
def buyDOSId():
    dataForDosBooks = {}
    namesForDosBooks=[]
    quantitysForDosBooks=[]
    idsForDosBooks=[]
    dataForDosBooks['book'] = []
    f = open("/home/bara111/FlaskApp/distributed_systems.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_distributed_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_distributed_systems.txt", "r")

    for x in f:
        namesForDosBooks.append(x)
    for n in m:
        quantitysForDosBooks.append(n)
    for g in t:
        idsForDosBooks.append(g)
    for i in range(len(namesForDosBooks)):
        dataForDosBooks['book'].append({'name': namesForDosBooks[i],'quantity':quantitysForDosBooks[i],'id':idsForDosBooks[i]})
    index = -1
    quantitysDOS=[]
    m = open("/home/bara111/FlaskApp/quantity_distributed_systems.txt", "r")
    for n in m:
        quantitysDOS.append(n)
    id = request.args.get("id", "")
    idFormated = "{}".format(id)
    for i in range(len(namesForDosBooks)):
        data=idsForDosBooks[i]
        data=data[:-1]
        dataInt = int(data)
        idFormated=int(idFormated)
        if(dataInt == idFormated):
                index = i
    if (index != -1):
                dataWithEnter = quantitysDOS[index]
                dataFormated = dataWithEnter[:-1]
                dataFormatedInt = int(dataFormated)
                if(dataFormatedInt!=0):
                          dataFormatedInt = dataFormatedInt-1
                          FormatedStringAfterSale = str(dataFormatedInt)+"\n"
                          quantitysDOS[index] = FormatedStringAfterSale
                          f = open('/home/bara111/FlaskApp/quantity_distributed_systems.txt', 'w')
                          for i in range(len(namesForDosBooks)):
                              f.write(quantitysDOS[i])
                          f.close()
                          return redirect("http://bara1111.pythonanywhere.com/update/dos/id?id="+str(id)) #call request while buying is success to update other servers
                else:
                    return '{ "status":"fail"}'

@app.route('/update/dos/id',methods=['GET'])
def updateDOSId():   #handle update of DOS catagory when buying from other servers
    dataForDosBooks = {}
    namesForDosBooks=[]
    quantitysForDosBooks=[]
    idsForDosBooks=[]
    dataForDosBooks['book'] = []
    f = open("/home/bara111/FlaskApp/distributed_systems.txt", "r")
    m = open("/home/bara111/FlaskApp/quantity_distributed_systems.txt", "r")
    t = open("/home/bara111/FlaskApp/id_distributed_systems.txt", "r")

    for x in f:
        namesForDosBooks.append(x)
    for n in m:
        quantitysForDosBooks.append(n)
    for g in t:
        idsForDosBooks.append(g)
    for i in range(len(namesForDosBooks)):
        dataForDosBooks['book'].append({'name': namesForDosBooks[i],'quantity':quantitysForDosBooks[i],'id':idsForDosBooks[i]})
    index = -1
    quantitysDOS=[]
    m = open("/home/bara111/FlaskApp/quantity_distributed_systems.txt", "r")
    for n in m:
        quantitysDOS.append(n)
    id = request.args.get("id", "")
    idFormated = "{}".format(id)
    for i in range(len(namesForDosBooks)):
        data=idsForDosBooks[i]
        data=data[:-1]
        dataInt = int(data)
        idFormated=int(idFormated)
        if(dataInt == idFormated):
                index = i
    if (index != -1):
                dataWithEnter = quantitysDOS[index]
                dataFormated = dataWithEnter[:-1]
                dataFormatedInt = int(dataFormated)
                if(dataFormatedInt!=0):
                          dataFormatedInt = dataFormatedInt-1
                          FormatedStringAfterSale = str(dataFormatedInt)+"\n"
                          quantitysDOS[index] = FormatedStringAfterSale
                          f = open('/home/bara111/FlaskApp/quantity_distributed_systems.txt', 'w')
                          for i in range(len(namesForDosBooks)):
                              f.write(quantitysDOS[i])
                          f.close()
                          return '{ "status":"success"}'
                else:
                    return '{ "status":"fail"}'

if __name__=="__main__":
        app.debug = False
        app.run(host = '0.0.0.0',port=5000)

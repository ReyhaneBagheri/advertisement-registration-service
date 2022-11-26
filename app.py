from flask import Flask, request, jsonify
import projectjavad as database , s3
import uuid
import os
import send

app =Flask(__name__)

@app.route('/test' , methods=['POST'])
def test():
    
    if request.method == "POST":
        description = request.form.get("description")
        email=request.form.get("email")
        image= request.files.get("image")

        image_name = image.filename

        id ,object_name = database.insert_data(description, email, image_name)
        s3.adds3(image, object_name)
        send.RabbitMQ_().send(str(id))
        return jsonify({"response" : "your message was registered with this id : " + (id)})
    
    
@app.route('/test2' , methods=['GET'])
def test2():
    if request.method == "GET":
        id2 = request.form.get("id")
        record=database.returnItem(str(id2))
        #return jsonify({"response":(record)})
        for row in record:
            #print(row[4])
            if row[4]=="0":
                return jsonify({"response": "Pending...","state": row[4], "record" : record})

            if row[4]=="-1":
                return jsonify({"response": "failed"})

            if row[4]=="1":
                #row[3] is objectname
                url=s3.generate_presigned_url('project-javad',row[3])
                return jsonify({"response": record ,"url": url})
                    
    return jsonify({"response": "Get request called"})

if __name__ =='__main__':
    
    app.run(debug=True , port=9090)


    
    
from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
app=Flask(__name__)
mysql=MySQL(app)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "khizar_abbas"

# @app.route("/expense", methods=["POST"])
# def expense():
#     data=request.get_json()
#     amount=data.get("amount")
#     des=data.get("des")
#     print(amount,des)
#     return jsonify("your data is posted")
@app.route("/expense",methods=["POST"])
def expense():
    data=request.get_json()
    balaces=data.get("balaces")
    khizar=data.get("khizar")
    cursor=mysql.connection.cursor()
    #print here
    print(balaces)
    print(khizar)
    query="INSERT INTO amount_des(amo,description) VALUES(%s,%s)"
    cursor.execute(query,(balaces,khizar))
    cursor =mysql.connection.commit()
    return jsonify("your data is added")
#post methods---
# @app.route("/expense1",methods=["POST"])
# def expense1():
#     Data=request.get_json()
#     name=Data.get("name")
#     email=Data.get("email")
#     cursor=mysql.connection.cursor()
#     query="INSERT INTO users(name,email) VALUES(%s,%s)"
#     cursor.execute(query,(name,email))
#     cursor =mysql.connection.commit()
#      #print here..
#     print(name)
#     print(email)
#     return jsonify("hello")
# get methods---
@app.route("/",methods=["GET"])
def expense2():
    cursor=mysql.connection.cursor()
    query="SELECT name ,email FROM users"
    result = cursor.execute(query)
    result=cursor.fetchall()
    print(result)
    return jsonify (result)
# delete methods---
@app.route('/expenses3/<int:id>', methods=['DELETE'])
def delete_expense(id):
    cursor=mysql.connection.cursor()
    query="DELETE FROM users WHERE id=%s"
    cursor.execute(query,(id,))
    cursor=mysql.connection.commit()
    return jsonify ("hello")
# update method (put)
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")


    cursor=mysql.connection.cursor()
    qurey="""UPDATE users
            SET name=%s,email=%s
            WHERE id=%s"""
    cursor.execute(qurey,(name,email,id))
    cursor=mysql.connection.commit()
    print("name", name)
    print("email", email)
    print("id", id)
    return jsonify ("change")

# post karn--


@app.route("/khazir_details",methods=["POST"])
def khazir_details():
    data=request.get_json()
    name=data.get("name")
    age=data.get("age")
    father_name=data.get("father_name")
    cursor=mysql.connection.cursor()
    #print here
    print("qalab abbas")
    print("age" "3year")
    print("father_name" "khizar")
    query="INSERT INTO khazir_details(name,age,father_name) VALUES(%s,%s,%s)"
    cursor.execute(query,(name,age,father_name))
    cursor =mysql.connection.commit()
    return jsonify("your data is added")
# get krn
@app.route("/khazir_details1",methods=["GET"])
def expense9():
    cursor=mysql.connection.cursor()
    query="SELECT name ,age father_name FROM khazir_details"
    result = cursor.execute(query)
    result=cursor.fetchall()
    print(result)
    return jsonify (result)
# delete karn---

@app.route('/khazir_details3/<int:id>', methods=['DELETE'])
def delete_khazir_details3(id):
    cursor=mysql.connection.cursor()
    query="DELETE FROM users WHERE id=%s"
    cursor.execute(query,(id,))
    cursor=mysql.connection.commit()
    return jsonify ("hello")
# update krn--
@app.route("/khazir_details5/<int:id>", methods=['PUT'])
def update_user1(id):
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    father_name = data.get("father_name")

    cursor = mysql.connection.cursor()
    query = """
        UPDATE khazir_details
        SET name=%s, age=%s, father_name=%s
        WHERE id=%s
    """
    cursor.execute(query, (name, age, father_name, id))
    mysql.connection.commit()

    print("name:", name)
    print("age:", age)
    print("father_name:", father_name)

    return jsonify({"message": "User updated successfully"})
if __name__ == "__main__":
    app.run(debug=True)


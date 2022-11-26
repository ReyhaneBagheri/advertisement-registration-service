import mysql.connector
import uuid

mydb = mysql.connector.connect(
host = "mysql-237ed598-reyhane-f73a.aivencloud.com",
port = 15125,
user = "avnadmin",
password = "AVNS_04Mn_qU4fNc1lRHoc9j",
database = "defaultdb",
use_pure= True
)
#print("hello")
print(mydb)
    
    
def create_table():

    mycursor = mydb.cursor()

    mycursor.execute(" CREATE TABLE projavad2 (id varchar(255) primary key  , description varchar(255) , email varchar(255),object_name varchar(255) ,state varchar(255), category varchar(255) ) " )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)
    
    
def insert_data(d , e , image_name ):

    mycursor = mydb.cursor()
    
    sql = "INSERT INTO projavad2 (id ,description , email, object_name , state , category  ) VALUES (%s ,%s, %s,%s , %s, %s)"
    id_ = uuid.uuid1().hex
    o =str(id_ )+ image_name
    print(id_)
    val = (str(id_) , d , e , o , "0"  , "NULL")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return id_ , o
    
    
def select():
    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM projavad2")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
        

def deleteTable():
    mycursor = mydb.cursor()

    mycursor.execute("DROP TABLE projavad2")

    myresult = mycursor.fetchall()
    print("deleteee Table projavad2")


def deleteItems():
    mycursor = mydb.cursor()

    mycursor.execute("DELETE FROM  projavad2")

    myresult = mycursor.fetchall()
    print("deleteee Items from table projavad2")
    
def returnItem(id):
    mycursor = mydb.cursor()
    sql_select_query = """select * from projavad2 where id = %s"""
    # set variable in query
    mycursor.execute(sql_select_query, (id,))
    # fetch result
    record = mycursor.fetchall()
    return record
    #for row in record:
    #    print("Id = ", row[0], )
    #   print("Name = ", row[1])
    #   print("Join Date = ", row[2])
    #    print("Salary  = ", row[3], "\n")
   
def updatTablestate(id , state ):
    mycursor = mydb.cursor()
    
    sql = "UPDATE projavad2 SET state = %s WHERE id = %s"
    val = (state, id)
    mycursor.execute(sql, val)
    mydb.commit()
    #print("1")
def updatTablecat(id , category):
    mycursor = mydb.cursor()
    
    sql = "UPDATE projavad2 SET category = %s WHERE id = %s"
    val = (category, id)
    mycursor.execute(sql, val)
    mydb.commit()
    #print("2")
    
    
    
       

#if __name__ == "__main__":
    
    #updatTablestate('49b7da5d684011edb8a85c879c9b432f', "0")
    #updatTablecat('49b7da5d684011edb8a85c879c9b432f', "null")
    #deleteTable()
    #create_table()
    #insert_data("hiii2" ,"rey@.com" , "knkjdfg.jpg")
    #select()
    #response=returnItem('75cc10936b7b11edb0d35c879c9b432f')
    #print(response)
    #for row in response:
     #   print(row[0])
      #  print(row[1])
       # print(row[2])
       # print(row[3])
       # print(row[4])
        #print(row[5])
        #if row[4]=="0":
         #   print("response Pending...")
            #text= 'Your ad has been approved. '+'url of immage :' + str(row[3])
        #elif row[4]=="-1":
         #   print("response failed")

        
    #deleteItems()
    #select()

import pymongo
clint = pymongo.MongoClient('mongodb+srv://Ducat101:DUCAT@cluster0.gvtwd.mongodb.net/',tlsAllowInvalidCertificates=True)

mydb = clint['Ducat']

coll = mydb.students
coll1 = mydb.placed

def admission(ducat_id,st_name,c_name,duration):
    coll.insert_one({"id":ducat_id,"name":st_name,"course":c_name,"duration":duration,"status":"Incomplete"})

def total(): # total no.of student list
    for el in coll.find():
        print(f"student_id:{el["id"]} name:{el["name"]} course:{el["course"]}") 

def extention(ducat_id,duration):
    coll.update_one({"id":ducat_id},{"$inc":{"duration":duration}}) 

def placed(ducat_id,name,course):
    coll1.insert_one({"id":ducat_id,"name":name,"course":course})

def certificate(ducat_id):
    for el in coll.find({"id":ducat_id}):
        if(el["status"]=="Completed"):
            print(el) 
        elif(el["status"]!="Completed"):
            print("Course is Incompleted.Please talk to your councellor") 
        else:
            print("Invalid User") 

def delete(ducat_id):
    coll.delete_one({"id":ducat_id}) 

def updateofStatus(ducat_id,currentStatus):
    coll.update_one({"id":ducat_id},{"$set":{"status":currentStatus}})

def placedlist():
    for el in coll1.find():
        print(el) 


def main():
    while(True):
        print("Press 1 for New Admissiion") 
        print("Press 2 for Total Student") 
        print("Press 3 for Extention of Course") 
        print("Press 4 for List of Placed Student")  
        print("Press 5 for Certificate of Course") 
        print("Press 6 for Delete a Data") 
        print("Press 7 for Updation of Status") 
        print("Press 8 for Placed Student List") 
        print("Press 9 for Exit from Database") 
 
        choice=int(input("Enter the Operation:")) 
        if(choice==1):
            # ducat_id,st_name,c_name,duration,status
            ducat_id=int(input("Enter Id:")) 
            st_name=input("Enter Name:") 
            c_name=input("Enter Course name:") 
            duration=int(input("Enter Total Months:"))
            admission(ducat_id,st_name,c_name,duration) 
            print("------------------------------------") 
            print("Data Inserted in Database! Move to Next...")
            print("------------------------------------") 
        elif(choice==2):
            print("--------------------------------------") 
            total() 
            print("--------------------------------------") 
        elif(choice==3):
            ducat_id=int(input("Enter Id:")) 
            duration=int(input("Enter the duration:")) 
            extention(ducat_id,duration) 
        elif(choice==4):
            ducat_id=int(input("Enter Id:")) 
            name=input("Enter name:") 
            course=input("Enter the course:") 
            placed(ducat_id,name,course) 
        elif(choice==5):
            ducat_id=int(input("Enter the id:")) 
            certificate(ducat_id) 
        elif(choice==6):
            ducat_id=int(input("Enter id to delete:")) 
            delete(ducat_id) 
        elif(choice==7):
            ducat_id=int(input("Enter id to update:")) 
            status=input("Enter current status of Course:") 
            updateofStatus(ducat_id,status) 
        elif(choice==8):
            placedlist() 
        elif(choice==9):
            break 
        else:
            print("Invalid Operation") 

if __name__=="__main__":
    main()



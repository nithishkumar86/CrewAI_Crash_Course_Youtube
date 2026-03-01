import requests


'''Simple Rule:


Talking to FastAPI/REST API → always use json= ✅
Talking to HTML Forms → use data= ✅

'''

BASE_URL = "http://127.0.0.1:8000"

#-------------------------------GET----------------------------------------------#

# GET all students
def get_all_students():
    response = requests.get(f"{BASE_URL}/students")
    return response.json()

#-------------------------------GET----------------------------------------------#

# GET single student
def get_student(name: str):
    response = requests.get(f"{BASE_URL}/single_students/{name}")
    return response.json()


#-------------------------------POST----------------------------------------------#


# json= → When sending JSON data (most common in FastAPI)


# POST create student
def create_student(id: int, name: str):
    response = requests.post(
        f"{BASE_URL}/students",
        json={"id": id, "name": name} # ← automatically sets Content-Type: application/json
    )
    return response.json()



#-------------------------------UPDATE----------------------------------------------#

# PUT update student
def update_student(student_id: int, name: str):
    response = requests.put(
        f"{BASE_URL}/students/{student_id}",
        json={"id": student_id, "name": name}
    )
    return response.json()

#-------------------------------DELETE----------------------------------------------#

# DELETE student
def delete_student(student_id: int):
    response = requests.delete(f"{BASE_URL}/students/{student_id}")
    return response.json()




if __name__ == '__main__':
    # Test all
    print(get_all_students())
    # print(get_student("John"))
    # print(create_student(3, "Alice"))
    # print(update_student(1, "NithishKumar"))
    # print(delete_student(2))
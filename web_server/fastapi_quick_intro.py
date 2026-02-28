from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

students = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
]

@app.get("/students")
def get_student():
    return students


class Student(BaseModel):
    id: int
    name: str

@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())
    return {"message": "Student created", "student": student}

@app.get("/single_students")
def get_students(name: str):   # ← add this
    if name:
        return [s for s in students if s["name"] == name]
    return students


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for s in students:
        if s["id"] == student_id:
            s["name"] = student.name
            return {"message": "Student updated", "student": s}
    return {"message": "Student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            return {"message": "Student deleted"}
    return {"message": "Student not found"}


if __name__ == "__main__":
    uvicorn.run(app='fastapi_quick_intro:app', host='127.0.0.1', port=8000, reload=True)
# app/main.py
from fastapi import FastAPI, HTTPException, status
from .schemas import User

app = FastAPI()
users: list[User] = []

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

#Get all the users
@app.get("/api/users")
def get_users():
    return users

#Gets all users using their id
@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#Creates new users and shows an error if user already exists
@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user
    
# Practice Exercises
#Add a PUT endpoint to update and existing user
#Add a Delete endpoint to Delete and existing user
#Add Health endpoint
# Add a student id to the User class that must start with S followed by exactly 7 digits

#Updates users and shows an error if user already exists
@app.put("/api/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for i, u in enumerate(users):
        if u.user_id == user_id:
            users[i] = updated_user
            return updated_user
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

#Deletes users and shows an error if user id is not found
@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            users.remove(u)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="user_id not found"
    )

#Gets health status
@app.get("/health")
def health():
    return {'status': 'ok'}

 #Reflection
 #1. Why install from requirements.txt instead of ad-hoc pip install?
 #1.We install from requirements.txt as it insures that everyone is working with the same libraries

 #2.What does coverage tell you that "all tests passed" doesn't?
 #2."All tests passed"indicates that existing tests ran without errors, while coverage shows which part of code were executed by the tests.

 #3.Why does assert error paths (422/404/409) as well as happy paths?
 #3.validates error responses and negative paths

 #4.What signal does a green GitHub Action send to teammates?
 #4.Shows that a workflow on a commit or branch has been completed.
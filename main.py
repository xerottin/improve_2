# from abc import ABC, abstractmethod
# from fastapi import FastAPI, Depends
#
# app = FastAPI()
#
# class User(ABC):
#     @abstractmethod
#     def get_permision(self):
#         pass
#
#
# class Admin(User):
#     def get_permision(self):
#         return ["read", "write", "delete"]
#
# class RegularUser(User):
#     def get_permision(self):
#         return ["read"]
#
# def get_current_user(is_admin: bool) -> User:
#     if is_admin:
#         return Admin()
#     return RegularUser()
#
# @app.get("/permission")
# def read_permision(user: User= Depends(get_current_user)):
#     return {"permision": user.get_permision()}
#
#



# def add_numbers(*args):
#     return sum(args)
#
# print(add_numbers(1, 2, 3, 4))
# print(add_numbers())


import os

path = os.getcwd()

print(path)

os.chdir("/home/hamid/Workspace/python-lessons/problems")

os.system("python3 serbest-is.py")
print(os.getcwd())
print(os.listdir())

print("Hello, World!")

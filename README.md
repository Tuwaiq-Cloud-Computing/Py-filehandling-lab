import requests
import json



file = open("string.txt", "r")
data = file.read()

listA = data.split(",")
print("\n data converted to list ", listA)
file.close()


user = {"firstname": "Ada"}
user["family name"] = "Byron"

user["brother"] = "Pancho"

print(user)

del user["brother"]
del user["family name"]

print(user)
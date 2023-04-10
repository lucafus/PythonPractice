#CAMPING LIST

supplies = ["test", "sleeping bags", "light", "knife", "flash drive", "water", "tent"]
#print(camping_list)

#camp_site = ["Cristal Lake", 404, 89.5, True]

#supplies = supplies + ["toilet paper", "bidet"]

supplies.insert(-1, "toilet paper")
supplies.insert(0, "bidet")

supplies.remove("tent")
print("This item was deleted: " + supplies.pop(2))
print(supplies)
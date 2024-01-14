# invites = [
#     'tupac', 'micheal jackson', 'pop smoke', '21 savage', 'rihanna',
#     'justin beiber', 'oldMe'
# ]

# tuple1 = (300, 21, 99, 23)
# print(len(tuple1))

# for number in range(0, len(tuple1)):
#     print(f"Number is - {tuple1[number]}")

poeple = []
poeple.append({"Fname": "Ojongsdsdsd Ndip", "Lname": "Shey Clinton"})
poeple.append({"Fname": "John", "Lname": "Doe"})

# for item in poeple:
#     print(item.get("Fname"), item.get("Lnames"))

for name in poeple:
    for k, v in name.items():
        print(f"\nKey : {k}")
        print(f"All is goonee bruhhhh: {v}")
    print("------------------------")

# print(poeple[0].get("Fname", "Not yet set"))

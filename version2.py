from Dog import Dog

users = {
    'ojong clinton': {
        'full_name': "Ojong Ndip Shey Clinton",
        'age': 22,
        'location': "Cameroon Yaounde",
    },
    'chi samuel': {
        'full_name': "Chi bords Apeng",
        'age': 26,
        'location': "Cameroon Yaounde",
    }
}

dog1 = Dog("one", "two")
dog1.roll_over()

# for name, props in users.items():
#     print(
#         f"""{name} \n \t Full name is : {props["full_name"]} \n \t Age is : {props["age"]} \n \t Location is : {props["location"]}"""
#     )

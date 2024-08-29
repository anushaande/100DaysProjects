from users import User, UserList



user_list = UserList()
user1 = user_list.userList[0]

print(user_list.userList[0].id)
user = User(user1.id, user1.name, user1.address, user1.phn)
# # in_person = input("Whom to find?: ")
user_list.get_users()
user.follow(user_list.userList[1])
user_list.get_users()

# print(user_list.find_user(in_person))


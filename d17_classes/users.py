class User():
    def __init__(self, id, name, address, phn):
        self.id = id
        self.name = name
        self.address = address
        self.phn = phn
        self.followers = 0
        self.following = 0

    def follow(self, user_to_follow):
        user_to_follow.followers +=1
        self.following +=1

class UserList():
    def __init__(self):
        self.userList = [
            User("000", "Anu", "sjigfhjvn jhfn", "8989898980"),
            User("001", "Anu1", "sjigfhjvn jhfn", "8989898981"),
            User("002", "Anu2", "sjigfhjvn jhfn", "8989898982"),
            User("003", "Anu3", "sjigfhjvn jhfn", "8989898983"),
            User("004", "Anu4", "sjigfhjvn jhfn", "8989898984"),
            User("005", "Anu5", "sjigfhjvn jhfn", "8989898985"),
        ]

    def get_users(self):
        print("NAME   -   FOLLOWERS   -    FOLLOWING")
        for user in self.userList:
            print (f"{user.name} - {user.followers} - {user.following}")

    def find_user(self, person):
        for user in self.userList:
            if person == user.name:
                return "person found."
        return "Person not found."

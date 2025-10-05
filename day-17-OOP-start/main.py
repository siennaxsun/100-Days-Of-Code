# create your own class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # function to change the followers and following whenever a user follows another each other
    # so when calling this function, it means a user object follows and follows back another user
    # so his/her follower and following accounts goes up by 1
    def follow(self, user):
        user.followers += 1
        self.following += 1


# create your object from your class
user_1 = User("001", "angela")
user_2 = User("002", "Jack")

# user1 follows user2
user_1.follow(user_2)
print (user_1.followers)
print (user_1.following)
print (user_2.followers)
print (user_2.following)


# print(f"the first user ID is: {user_1.id}")
# print(f"the first user followers is: {user_1.followers}")
#
# user_2.followers = 100
# print(f"the second user followers is: {user_2.followers}")









# add as many attributes to your object as you want
# user_1.id = "001"
# user_1.username = "anngela"
# print(user_1.username)









# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
# my_car = Car(5)
# print(my_car)
# print(my_car.seats)
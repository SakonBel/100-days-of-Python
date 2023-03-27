# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("darkgreen")
# timmy.forward(75)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)


# class User:
#     pass


# user_1 = User()
# user_1.id = "001"
# user_1.username = "bel"

# print(user_1.username)

class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.username = name
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1


user_1 = User("001", "bel")
user_2 = User("002", "maew")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.followings)
print(user_2.followers)
print(user_2.followings)

print("Welcome! Can i get to know you better.")

name= input("What's your name? ")
age = input("How old are you? ")
favorite_color= input("What's your favorite color? ")
favorite_food= input("What's your favorite food? ")
city= input("Which city do you live in? ")
University = input("Which university do you attend? ")
musician= input("Who's your favorite musician artist? ")
outing= input("Do you like going to parties? ")

print("\n Personalized summary! ")
print(f"Hello, {name}!")
print(f"Youn are{age} years old, wow  that's a nice color {favorite_color},and enjoy eating{favorite_food}.")
print(f"Life must be awesome and fun in {city}!")
print(f"You attend{University}, that's a great school.")
print(f"And of course, cheering for {musician} makes life more exciting")
print(f" {outing} wow then you like enjoying.")

def main():
    while True:
        details =collect_persoal_details()


fruits = {"apple": "red",
          "orange": "orange",
          "lime": "green",
          "mango": "yellow"}

veggies = {"cababge": "green",
           "carrot": "orange",
           "beet": "red"}

# fruits will be added to veg, not new dictionary returned
veggies.update(fruits)
print(fruits)
print(veggies)

nice_all = fruits.copy()



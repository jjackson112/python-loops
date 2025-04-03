age_list = [5, 7, 12, 13, 9, 21, 11, 10]
num_eligible = 0

for years in age_list:
  if years > 9:
    num_eligible = num_eligible + 1
  print(num_eligible)

# T0 Do List exercise
todo_list = []
done = False

print("Type 'done' at any time to exit")

# setting the loop to not done means it will run as long as done is not True
while not done:
  new_item = input("Add an item to your to do list:")
  if new_item == "done":
    done = True
    print(todo_list)
  else:
    todo_list.append(new_item)
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure (column,row)? Input range 11 to 33: ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# if num is 23 (column, row)
column = int(position[1])-1
row = int(position[0])-1
map[column].pop(row) # remove existing item
map[column].insert(row, "X") # replace with new item in same position






#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


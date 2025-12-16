people = 4  # friends who went trick-or-treating
bg1 = 37
bg2 = 22
bg3 = 8
bg4 = 30

# Part 1: Combine the haul
candy_total = 97
print(f'candy total:{candy_total}')



# Part 2: Fair sharing (include yourself)
People = 5
share = candy_total // people
leftover = candy_total % people
print(f"Each person gets:{share}")
print(f"Leftover candy:{leftover}")



# Part 3: Include the sick friends
# Variable reassignment is fine - previous values were already printed
people = 7
share = candy_total // people
leftover = candy_total % people
print(f"Each person gets:{share}")
print(f"Leftover candy:{leftover}")

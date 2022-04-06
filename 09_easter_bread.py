budget = float(input())
flour_kg_price = float(input())
total_price = 0
number_of_breads = 0
colored_eggs = 0

egg_pack_price = 0.75*flour_kg_price
milk_liter_price = 1.25*flour_kg_price

while True:
    price = flour_kg_price + egg_pack_price + milk_liter_price/4
    if price + total_price >= budget:
        break
    else:
        total_price += price
        number_of_breads += 1
        colored_eggs += 3

    if number_of_breads % 3 == 0:
        colored_eggs -= (number_of_breads - 2)


money_left = budget - total_price

print(f'You made {number_of_breads} loaves of Easter bread! Now you have {colored_eggs} \
eggs and {money_left:.2f}BGN left.')

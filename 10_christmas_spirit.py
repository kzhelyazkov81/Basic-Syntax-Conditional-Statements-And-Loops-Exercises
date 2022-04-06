quantity = int(input())
days = int(input())

ornament_set = 0
tree_skirt = 0
tree_garlands = 0
tree_lights = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15
christmas_spirit = 0

for i in range(1, days+1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        ornament_set += quantity
        christmas_spirit += 5
    if i % 3 == 0:
        tree_skirt += quantity
        tree_garlands += quantity
        christmas_spirit += 13
    if i % 5 == 0:
        tree_lights += quantity
        christmas_spirit += 17
        if i % 3 == 0:
            christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        tree_skirt += 1
        tree_garlands += 1
        tree_lights += 1

if days % 10 == 0:
    christmas_spirit -= 30

budget = ornament_set_price*ornament_set + tree_skirt_price*tree_skirt + tree_garlands_price*tree_garlands + \
    tree_lights_price*tree_lights

print(f'Total cost: {budget}')
print(f'Total spirit: {christmas_spirit}')

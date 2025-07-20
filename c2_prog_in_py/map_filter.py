menu = ['espresso','mocha','latte','cappuccino','cortado','americano']

def find_coffee(coffee):
    if coffee[0]=='c':
        return coffee

map_coffee = list(map(find_coffee,menu))
print(map_coffee)

# for x in map_coffee:
#     print(x)
# lst = input().split()
# print(lst)
# print(list(map(int,lst)))

filter_coffee = filter(find_coffee,menu)
for x in filter_coffee:
    print(x)

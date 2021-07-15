fighters = {'Goku':9999, 'Vegeta':8999, 'Krilin':2575, 'Yamcha':1500}

# print(fighters.get('Goku'))

# print(fighters.items())

# print(fighters.keys())

# print(fighters.popitem())
# print(fighters)

'''
print(fighters.setdefault('Videl'))
print(fighters.setdefault('Mr. Satan', 10))
print(fighters)
'''

new_fighters = {'Ryu':7563, 'Ken Masters': 7563, 'Heihachi': 8888}
fighters.update(new_fighters)
print(fighters)

update_fighters={'Ryu': 8500, 'Heihachi': 666}
fighters.update(update_fighters)
print(fighters)
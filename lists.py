fighters=['Goku', 'Goku', 'Goku', 'Piccoro', 'Goten', 'Broly', 'Freeza', 'Vegeta']
years = [3, "1983", 2.5, 547, "1994"]

print("goku" in fighters)
print("Goku" in fighters)

print(fighters.count('Goku'))
print("Piccoro is at position " + str(fighters.index('Piccoro')))

"""
print(fighters, years)
fighters.append("Nappa")
print(fighters)

fighters.extend(years)
print(fighters)

fighters.remove("Nappa")
print(fighters)

fighters.pop(0)
print(fighters)

fighters.pop(-1)
print(fighters)

numbers=[7, 1875, 4, 15.3, 69, 75.75]
numbers.sort()
print(numbers)
"""
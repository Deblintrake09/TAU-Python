fighters=['Goku', 'Piccoro', 'Goten', 'Broly', 'Freeza', 'Vegeta']

for fighter in fighters:
    print('Are you ready to take on {}?'.format(fighter))

for number in range(1,12):
    print("Number {}".format(number))

temp_c = 40
while temp_c > 20:
    print("The water is {} degrees Celsius".format(temp_c))
    temp_c -= 1
    if temp_c == 33:
        break

for number in range(1,11):
    if number== 7:
        print('Skipping number 7.')
        continue
    print('This is the number {}.'.format(number))

for number in range(1,11):
    if number == 3:
        pass
    print('This is the number {}.'.format(number))

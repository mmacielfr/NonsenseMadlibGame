print("Let's write a story together!")
print('\nPlease enter the following: ')
print()

adjective = input('Adjective: ')
animal = input('Animal: ')
verb = input('Verb: ')
exclamation = input('Exclamation: ')
verb_2 = input('Verb 2: ')
verb_3 = input('Verb 3: ')

print('\n This is your story:')
print()
# print('The other day, I was really in trouble. It all started when I saw a very ' 
# + adjective + ' ' + animal + ' ' + verb + ' down the hallway. ' +
# exclamation.upper() + '! I yelled. But all I could think to do was to ' +
# verb_2 + ' over and over. Miraculously, that caused it to stop, but not before it tried to ' + verb_3 +
# ' right in front of my family.')

print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. "{exclamation.upper()}!" I yelled. But all I could think to do was to {verb_2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_3} right in front of my family.')

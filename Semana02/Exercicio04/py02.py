print('hello word')

message = 'hello word'
print(message)

message1 = 'bobby\'s world'
print(message1)

message2 = "bobby's world"
print(message2)

message3 = """bobby's world was a good
cartoon in the 1990s"""
print(message3)


print(len(message))

print(message[0])

print(message[10])

##print(message[11])

print(message[0:5])

print(message[:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count('hello'))

print(message.count('l'))

print(message.find('world'))

print(message.find('universe'))

new_message = message.replace('world', 'universe')
print(new_message)

greeting = 'hello'
name = 'vinicius'

message4 = greeting + name
print(message4)
message5 = greeting + ', ' + name
print(message5)
message6 = greeting + ', ' + name + '. Welcome!'
print(message6)
message7 = '{}, {}. Welcome!'.format(greeting, name)
print(message7)
message8 = f'{greeting}, {name}. Welcome!'
print(message8)
message8 = f'{greeting}, {name.upper()}. Welcome!'
print(message8)
print(dir(name))
print(help(str))
print(help(str.lower))
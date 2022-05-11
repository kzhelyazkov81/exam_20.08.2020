def move(message, number):
    front = message[:number]
    back = message[number:]
    message = back + front
    return message


def insert(message, index, value):
    front = message[:index]
    back = message[index:]
    message = front + value + back
    return message


def change_all(message, substring, replacement):
    message = message.replace(substring, replacement)
    return message


message = input()
while True:
    command = input()
    if command == "Decode":
        break
    command = command.split('|')
    action = command[0]
    if action == 'Move':
        message = move(message, int(command[1]))
    elif action == 'Insert':
        message = insert(message, int(command[1]), command[2])
    elif action == 'ChangeAll':
        message = change_all(message, command[1], command[2])

print(f'The decrypted message is: {message}')

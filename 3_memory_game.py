def additional(seq, count):
    element = '-' + str(count) + 'a'
    index = len(seq) // 2
    seq.insert(index, element)
    seq.insert(index, element)
    print('Invalid input! Adding additional elements to the board')
    return seq


def play(seq, index1, index2):
    if seq[index1] == seq[index2]:
        element = seq[index1]
        seq.remove(element)
        seq.remove(element)
        print(f'Congrats! You have found matching elements - {element}!')
    else:
        print('Try again!')
    return seq


sequence = input().split(' ')
valid = True
counter = 0
while True:
    command = input()
    if command == 'end':
        break
    else:
        command = list(map(int, command.split(' ')))
    counter += 1
    if command[0] == command[1]:
        valid = False
    elif command[0] < 0 or command[0] >= len(sequence):
        valid = False
    elif command[1] < 0 or command[1] >= len(sequence):
        valid = False
    else:
        valid = True
    if not valid:
        sequence = additional(sequence, counter)
    else:
        sequence = play(sequence, command[0], command[1])
    if len(sequence) == 0:
        break

if len(sequence) == 0:
    print(f'You have won in {counter} turns!')
else:
    current_sequence = ' '.join(sequence)
    print(f"Sorry you lose :(\n{current_sequence}")

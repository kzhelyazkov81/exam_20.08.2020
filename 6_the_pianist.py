def add(piece, composer, key):
    current_piece = dict()
    current_piece['composer'] = composer
    current_piece['key'] = key
    pieces[piece] = current_piece


def remove(piece):
    if piece in pieces:
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key):
    if piece in pieces:
        pieces[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


n = int(input())
pieces = dict()
for i in range(n):
    data = input().split('|')
    piece = data[0]
    composer = data[1]
    key = data[2]
    add(piece, composer, key)


while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split('|')
    action = command[0]
    if action == 'Add':
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in pieces:
            add(piece, composer, key)
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f"{piece} is already in the collection!")
    elif action == 'Remove':
        piece = command[1]
        remove(piece)
    elif action == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        change_key(piece, new_key)

for piece in pieces:
    composer = pieces[piece]['composer']
    key = pieces[piece]['key']
    print(f"{piece} -> Composer: {composer}, Key: {key}")

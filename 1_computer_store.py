computer_receipt = 0
discount = 0

while True:
    command = input()
    if command == 'special':
        discount = 0.1
        break
    elif command == 'regular':
        break
    else:
        price = float(command)
        if price < 0:
            print('Invalid price!')
        else:
            computer_receipt += price


if computer_receipt == 0:
    print('Invalid order!')
else:
    taxes = 0.2 * computer_receipt
    total_price = (computer_receipt + taxes) * (1-discount)
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {computer_receipt:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')


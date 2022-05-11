queue = int(input())
lift = list(map(int, input().split(' ')))

for i in range(len(lift)):
    while lift[i] < 4:
        lift[i] += 1
        queue -= 1
        if queue == 0:
            break
    if queue == 0:
        break
full_lift = True
for i in lift:
    if i < 4:
        full_lift = False
wagons = ' '.join(list(map(str, lift)))
if queue == 0 and not full_lift:
    print(f"The lift has empty spots!\n{wagons}")
elif queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!\n{wagons}")
else:
    print(f'{wagons}')

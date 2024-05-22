def input_handler():
    capacity, count = list((map(int, input().split(' '))))

    objects = list()
    for _ in range(count):
        weight, value = list(map(int, input().split(' ')))
        obj = {
            'weight': weight,
            'value': value,
        }
        objects.append(obj)

    return capacity, objects


def knapsack(capacity, objects):
    choices = list()
    values = 0

    sorted_objects = sorted(objects, key=lambda obj: obj['value'] / obj['weight'], reverse=True)

    for item in sorted_objects:
        if item['weight'] <= capacity:
            capacity -= item['weight']
            values += item['value']
            choices.append(objects.index(item) + 1)

    return choices, values


def main():
    capacity, objects = input_handler()
    choices, values = knapsack(capacity, objects)

    print(choices)
    print(values)


if __name__ == '__main__':
    main()

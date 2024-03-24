from Polynomial import Polynomial


def main(p0, p1):
    menu()
    choice = int(input())
    match choice:
        case 0:
            e, c = input("enter exp & coef for add term: ").split(' ')
            p0.add_term(int(e), int(c))
        case 1:
            e = int(input("enter exp for remove term: "))
            p0.remove_term(e)
        case 2:
            p0.add(p1)
        case 3:
            p0.sub(p1)
        case 4:
            p0.mult(p1)
        case 5:
            p0.print()


def menu():
    print("__________________________________________________________________________________________")
    print("\n0 -> add term")
    print("1 -> remove term")
    print("2 -> add polynomial")
    print("3 -> subtract polynomial")
    print("4 -> multiply polynomial")
    print("5 -> print polynomial")
    print("\nEnter the number: ", end='')


if __name__ == '__main__':
    p0 = Polynomial()
    p1 = Polynomial()
    while True:
        print("\n0 -> p0\n1 -> p1\n2 -> Exit\n")
        obj = int(input("Select the object: "))
        if obj == 2:
            break
        elif obj == 0:
            main(p0=p0, p1=p1)
        elif obj == 1:
            main(p0=p1, p1=p0)

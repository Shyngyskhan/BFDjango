def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print (election(x, y, z))


def election(x, y, z):
    if x + y + z > 1:
        return 1
    else:
        return 0

main()

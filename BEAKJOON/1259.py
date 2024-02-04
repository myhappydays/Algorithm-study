while True:
    A = input()
    if A == '0':
        break
    elif A == A[::-1]:
        print("yes")
    else:
        print("no")

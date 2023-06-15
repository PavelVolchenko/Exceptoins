def divide(a, b):
    try:
        if len(a) != len(b):
            raise Exception
        else:
            c = list()
            for i in range(len(a)):
                c.append(a[i] / b[i])
            return c
    except Exception:
        print("Array size not equal")


a = [2, 5, 6, 2, 4, 5]
b = [4, 2, 4, 2, 1]

print(divide(a, b))

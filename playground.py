def add(*args):
    # add_up = [number for number in args]
    # print(sum(add_up))     OR

    # sum_of = []
    # for i in args:
    #     sum_of.append(i)
    # print(sum(sum_of))        OR

    #     The Shortest
    print(sum(args))


# add(2, 5, 6, 8, 10, 10)


def calculate(n, **kwargs):
    add_up = [value for key, value in kwargs.items()]
    print(add_up)

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(n= 5, add= 3, multiply= 5)

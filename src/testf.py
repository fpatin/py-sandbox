def greeting(name):
    return "Hello " + name


def greeting2(name: str) -> str:
    return "Hello " + name


if __name__ == '__main__':
    print(greeting(123))
    print(greeting2(123))
    print(greeting(b"Alice"))
    print(greeting2(b"Alice"))

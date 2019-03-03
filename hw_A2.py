def sayhello(x):
    if x == 0 :
        return None
    print("Hello world!")
    sayhello(x - 1)


sayhello(10)

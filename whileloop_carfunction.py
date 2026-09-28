command=""
is_carstarted=True
is_carstopped=False
while True:
    command=input(">")
    if command == "start":
        if is_carstarted:
            print("car has already started..")
        else:
            print("car started..")
    elif command == "stop":
        if is_carstopped:
            print("car has already stopped..")
        else:
            print("car stopped..")
    elif command == "help":
        print("""
        start-to start car
        stop-to stop car
        quit-to quit car""")
    elif command == "quit":
        break
    else:
        print("invalid command")

command=""
while True:
    command=input(">")
    if command == "start":
        print("car started..")
    elif command == "stop":
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

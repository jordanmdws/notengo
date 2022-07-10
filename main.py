
print('Welcome to Note&Go')
print()


def add():
    note = input("Enter Note Here: ")

    with open("notengo.txt", "a") as f:
        f.write(note + "\n")


def view():
    with open("notengo.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())


def erase():
    with open("notengo.txt", "a") as f:
        f.truncate(0)


while True:
    mode = input(
        "Would you like to add or view your notes? (add/view/erase) Pres q to quit: ").lower()
    if mode == "q":
        quit()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "erase":
        confirmation = input(
            "Are you sure you want to delete. (Cannot be recovered! 'yes/no: ").lower()
        if confirmation == "yes":
            erase()
        if confirmation == "no":
            pass
    else:
        print("invalid Function! Retry.")
        continue

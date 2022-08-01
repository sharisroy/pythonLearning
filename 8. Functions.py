# Without Parameter
def print_message():
    print("Hello Bangladesh!")


print_message()


# With Parameter

def print_message(message):
    print(message)


print_message("Hello Bangladesh!")


# With Parameter

def print_message(message, defult_Message="Kemon acho tomara"):
    print(message)
    print(defult_Message)


print_message("Hello Bangladesh!")


# Return Value
def take_input():
    value = input("Enter Your Name: ")
    return value


name = take_input()
print("Hello Mr." + name)

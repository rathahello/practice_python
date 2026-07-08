from countdown import countdown_timer
from generate_pwd import generate_password
def main():
    # *****Run 5 countdown timers in a loop*****
    # value = 0
    # while value < 5:
    #     value += 1
    #     countdown_timer()
    # *****Run countdown timer indefinitely*****
    while True:
        print("1. Countdown timer")
        print("2. Password generator")
        choice = input("Enter your choice (1 or 2): ")
        try:
            choice = int(choice)
            if choice == 1:
                countdown_timer()
            elif choice == 2:
                generate_password()
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
main()
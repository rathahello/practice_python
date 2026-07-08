import time

def countdown_timer():
    print("\n--- ⏱️ Countdown Timer ---")
    while True:
        try:
            seconds = int(input("Enter time in seconds to count down: "))
            if seconds <=0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\nTimer Started!")
    while seconds > 0:
        # divmod calculates minutes and remaining seconds
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"

        # \r overwrites the current line in the console
        print(timer_format, end="\r")
        
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")
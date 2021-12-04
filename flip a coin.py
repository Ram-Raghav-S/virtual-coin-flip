print("This program flips a coin.")
loop_number = 1
correct_streak = 0
while True:
    try:
        from random import seed
        from random import randint
        call = input("Call heads or tails. ")
        call = call.lower()
        b = randint(0, 1000000000000000000000000000000000000000)
        if b % 2 == 0:
            if call == "heads":
                print("Yay! your call was correct.")
                correct_streak += 1
                print(f"You are on a streak of {correct_streak}")
                print("\n")
            elif call == "tails":
                print("Tough luck! your call was incorrect.")
                correct_streak = 0
                print(f"You are on a streak of {correct_streak}")
                print("\n")
            else:
                print("Please enter a valid call.")

        elif b % 2 == 1:
            if call == "tails":
                print("Yay! your call was correct.")
                correct_streak += 1
                print(f"You are on a streak of {correct_streak}")
                print("\n")
            elif call == "heads":
                print("Tough luck! your call was incorrect.")
                correct_streak = 0
                print(f"You are on a streak of {correct_streak}")
                print("\n")
            else:
                print("Please enter a valid call.")

    except Exception:
        print("Please enter a valid call.")

from random import randint

def main():
    n = None
    m = None
    while n is None or m is None:
        try:
            n = int(input("Enter the lower bound (n): "))
            m = int(input("Enter the upper bound (m): "))
            if n >= m:
                print("Invalid range. Please ensure that n < m.")
                n, m = None, None
        except ValueError:
            print("Please enter valid integers for n and m.")
    
    secret_number = randint(n, m)
    attempt_limit = 10
    print(f"Guess the number between {n} and {m}. You have {attempt_limit} attempts.")
    for i in range(attempt_limit):
        print(f"Attempts remaining: {attempt_limit - i}")
        try:
            guess = int(input("Enter your guess: "))
            if guess < n or guess > m:
                print(f"Your guess is out of bounds. Please guess a number between {n} and {m}.")
                continue
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You've guessed the number!")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
from random import randint

count = 0
amount = int(input("Enter the amount you want to bet: (Bet only 100 min and max 20000 Amount): "))

# Validate the amount
if amount < 100 or amount > 20000:
    print("Amount must be more than 100 and less than 20000")
    exit()
else:
    original_amount = amount  # Store the original amount for calculations
    while True:
        count += 1
        num = int(input("Enter a number between 1 and 10: "))
        win_nom = randint(1, 3)  # Generate a random winning number between 1 and 3

        if num == win_nom:
            amount = amount * win_nom
            print("You win!")
            print("Your Profit: +{}".format(amount - original_amount))
            break
        else:
            # Calculate the loss for the attempt
            loss = int(amount * 0.3)
            amount -= loss  # Reduce the amount by 30%

            print("Try again!")
            print("Remaining Amount: {}".format(amount))
            print("Loss in this attempt: -{}".format(loss))
            print("Total Loss So Far: -{}".format(original_amount - amount))

        if count == 3:
            final_loss = original_amount - amount  # Total loss as difference from the original amount
            print("You lose! Maximum attempts reached.")
            print("Final Loss: -{}".format(final_loss))
            break

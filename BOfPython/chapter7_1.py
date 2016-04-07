number =23
guess = int(input("Enter the nuber : "))

if guess == number:
    print("congratulations. you gussed it.")
    print("but yo do not win any prizes!")
elif guess < number:
    print("No, it is a little higher than that")
else:
    print("No, it is a little lower than that")

print("Done!")
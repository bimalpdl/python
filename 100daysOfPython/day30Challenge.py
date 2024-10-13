print("30 days down- What did you think?")
print()
for i in range(1,5): # it was supposed to be 30 days
    thought = input(f"Day {i}:\n")
    print()
    text = f"You thought your day {i} was"
    print(f"{text:^50}")
    print(f"{thought:^50}")



RICE_PRICE = 30
MILK_PER_PACK = 1000
total = 0


def check_choice(choice, donate):
    if choice == 'm':
        print(f"Money = {donate:.2f}")
    elif choice == 'r':
        print(f"")


def update_rice(donate, current):
    new_rice = (donate/RICE_PRICE) + current
    return new_rice


def update_milk(donate, current):
    new_milk = (donate*MILK_PER_PACK)+current


def display(rice, milk, money, total):
    total = (rice*RICE_PRICE)+money + (MILK_PER_PACK*milk)
    print(f"Current donation:")
    print(f"Money = {money:.2f} baht")
    print(f"rice = {rice:.2f} kg.")
    print(f"Milk = {milk:.2f} packs.")
    print(f"Total = {total:.2f}")


money = 0
rice_donate = 0
milk_donate = 0
total = 0
while True:
    donate = int(input("Enter donation amount: "))
    choice = input("Enter donation choice (m/r) : ")
    if choice == 'r':
        money += donate
    elif choice == 'r':
        rice_donate = update_rice(donate, total)
    elif choice == 'm':
        milk_donate = update_milk(donate, total)
    elif donate == -1:
        break
    else:
        print("Wrong choice.Start Over")
    display(rice_donate, milk_donate, money, total)

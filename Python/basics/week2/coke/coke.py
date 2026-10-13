#16/07/2026
#A machine sells coke (50 cent) that only accepts 25, 10 and 5 cents coin, assumpt that user only input integer
#Prompts the user till they have fully paid for their coke, and output change amount after finished.
#1. Continuously prompt the user for their coin amount. While loop to check for correct values
#2. Substract the Due with the correspoding coin amount
#3. Continue till 50cent or over were inputed 
#4. Return the Change amount. Return ) if paid exact amount

def coin_prompt():
    price = 50

    while price > 0:
        print(f"Amount Due: {price}")
        money = input("Insert Coin: ")

        if money in ["25", "10", "5"]:
            price -= int(money)

    print(f"Change Owed: {-price}")

def main():
    coin_prompt()

if __name__ == "__main__":
    main()
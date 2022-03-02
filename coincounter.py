def main():
    amount =int(input("How many pennies do you have: "))
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while amount > 0:
        if amount >= 100:
            amount -= 100
            dollars += 1
          
        elif amount >= 25:
            amount -= 25
            quarters +=1
          
        elif amount >= 10:
            amount -= 10
            dimes +=1
            
        elif amount >= 5:
            amount -= 5
            nickels +=1
          
        else:
            pennies += amount
            amount=0

    print (f"""dollars: {dollars}
    quarters: {quarters}
    dimes: {dimes}
    nickles: {nickels}
    pennies: {pennies}""")

    main()
    main()

#creating a vending machine

print("Hello")
print("______________________________")
print("WELCOME TO VENDING MACHINE")
print("......................................................................................")
print("[Languages= English / Arabic]")
print("______________________________")

#Select a language
Language = {
    '1' : 'English' , 
    '2' : 'Arabic'
}
Language_code=input('please select the Language:')
if Language_code== 'English' :
    print("You have selected English")
elif Language_code=='Arabic' :
 print("You have selected Arabic")


#Codes of the Items in the GYM
items={
   '101' : 'Pre workout' , 
   '102' : 'Protien bar' , 
   '103' : 'L-carnitine' , 
   '104' : 'Black wolf shot' , 
   '105' : 'Protien chips' , 
   '106' : 'Protien cookie' , 
   '107' : 'Water' , 
   '108' : 'Steriods' , 
   '109' : 'C4 can' ,
   '110' : 'Banana' , 
   '111' : 'Redbull' , 
   '112' : 'Protien Shake' , 
   '113' : 'Greek yougurt' ,
   '114' : 'Gatorade' ,
   '115' : 'Beef jerky' , 


}

print("MENU OF GYM STOP")
print("...........................................................................")
print("1. Pre workout                    AED 30 ,      Code: 101 ,         Stock:50")
print("2. Protien bar                       AED 10 ,      Code: 102 ,         Stock:90")
print("3.L-carnitine                     AED 20 ,      Code: 103 ,         Stock:30 ")
print("4. Black wolf shot                        AED 25 ,      Code: 104 ,         Stock:50")
print("5. Protien chips                  AED 10 ,      Code: 105 ,         Stock:100")
print("6. Protien cookie                      AED 10 ,      Code: 106 ,         Stock:70")
print("7.  Water                    AED 3 ,      Code: 107 ,         Stock:100")
print("8.  Steriods                AED 150 ,      Code: 108 ,         Stock:40")
print("9. C4 can                       AED 30 ,      Code: 109 ,         Stock:120")
print("10. Banana                   AED 5 ,      Code: 110 ,         Stock:60")
print("11. Redbull                    AED 15 ,      Code: 111 ,         Stock:50")
print("12. Protien Shake                      AED 35 ,      Code: 112 ,         Stock:90")
print("13. Greek yougurt                   AED 10 ,      Code: 113 ,         Stock:40")
print("14. Gatorade                      AED 15 ,      Code: 114 ,         Stock:50")
print("15. Beef jerky                     AED 40 ,      Code: 115 ,         Stock:30")   
print("............................................................................")

#Price of items in the GYM STOP
Preworkout=30
Protienbar=10
Lcarnitine=20
Blackwolfshot=25
Protienchips=10
Protiencookie=10
Water=3
Steriods=150
C4can=30
Banana=5
Redbull=15
Protienshake=35
Greekyougurt=10
Gatorade=15
Beefjerky=40

#check stock
stock=3000
if stock>0:
    print("________________________")
    print("We have snacks and beverages in stock. Please make your selection.")
    print("_______________________")


#This is for Entering The Product Code      
items_code=input('Please enter the Product Code you would like to buy:')

# Enter the Amount of Money
money=int(input("Thankyou for your selection .Please insert the money:"))



#Choice for Additional Item
choice = {
   '1': 'yes' ,
   '2': 'no'
}
choice=input('Snackers and Drinkers would like to suggest you to have some tissue? (yes/no):')
if choice== 'yes':
   print("...............................")
   print("Thankyou for your Selection")
elif choice== 'no':
   print("Thankyou for your Selection")

   #Calculating and Returning the Correct Change Of Twizzlers
   if items_code=='101':
      if money >= Preworkout:
         money=money-Preworkout

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Twix
   if items_code=='102':
      if money >= Protienbar:
         money=money-Protienbar

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Hersheys
   if items_code=='103':
      if money >= Lcarnitine:
         money=money-Lcarnitine

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Oreo
   if items_code=='104':
      if money >= Blackwolfshot:
         money=money-Blackwolfshot

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Skittles
   if items_code=='105':
      if money >= Protienchips:
         money=money-Protienchips

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Kitkat
   if items_code=='106':
      if money >= Protiencookie:
         money=money-Protiencookie

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Dortitos
   if items_code=='107':
      if money >= Water:
         money=money-Water

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Mountain Dew
   if items_code=='108':
      if money >= Steriods:
         money=money-Steriods

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Fanta
   if items_code=='109':
      if money >= C4can:
         money=money-C4can

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Gatorade
   if items_code=='110':
      if money >= Banana:
         money=money-Banana

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Redbull
   if items_code=='111':
      if money >= Redbull:
         money=money-Redbull

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Pepsi
   if items_code=='112':
      if money >= Protienshake:
         money=money-Protienshake

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Barbican
   if items_code=='113':
      if money >= Greekyougurt:
         money=money-Greekyougurt

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Water
   if items_code=='114':
      if money >= Gatorade:
         money=money-Gatorade

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")

         



         #Calculating and Returning the Correct Change Of Sprite
   if items_code=='115':
      if money >= Beefjerky:
         money=money-Beefjerky

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")
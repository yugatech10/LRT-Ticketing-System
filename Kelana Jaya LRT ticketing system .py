print "                Welcome to Kelana Jaya LRT ticketing system            "
print ""
def stations():
    print "List of Stations"
    list_station = ["Taman Bahagia","Taman Paramount","Asia Jaya","Taman Jaya","Universiti","Kerinchi","Abdullah Hukum","Bangsar","KL Sentral","Pasar Seni","Masjid Jamek","Dang Wangi","Kampung Baru","KLCC","Ampang Park","Setiawangsa","Terminal Putra"]
    num = 0
    station = 1
    while num < 17:
        print station,"." ,list_station[num]
        num += 1
        station +=1
    print ""
    new_station = input("Please select station you willing to go by inserting the relevant number : ")
    print ""
    new_station -= 1
    print "You inserted number " ,new_station + 1, ",Station" ,list_station[new_station],"."
    return new_station



new_station = stations()
num_tickets=input("How many tickets you willing to purchase : ")

print ""
print "_______________________________Purchase details________________________________"
print ""
print "Station Name : ", new_station+1
print "Number of tickets : ", num_tickets
station_price=[0.70,1.00,1.30,1.30,1.30,1.40,1.40,1.40,2.10,2.10,2.30,2.30,2.30,2.40,2.40,2.50,2.50]
price = station_price[new_station]
print "Price(each) : RM",price
total = num_tickets * price  
print ""
print "Total amount you need to pay : ",total
payment = input("Please insert amount of payment(RM 1,RM 5,RM 10,RM 50,RM 100,RM0.10,RM0.20,RM0.50 ) : RM")
print ""
balance = total - payment

while balance > 0:
    print "____________________________Please continue your payment___________________________________"
    print ""
    print "Total amount you need to pay : RM",balance
    payment = input("Please insert amount of payment(RM 1,RM 5,RM 10,RM 50,RM 100,RM0.10,RM0.20,RM0.50 ) : ")
    balance = balance - payment
    print ""
    
if balance < 0:
    print "______________________________Payment completed_______________________________"
    print ""
    print "Balance returning : RM",abs(balance)
    print "Thank you for purchasing ticket from Kelana Jaya LRT ticketing system"

print "______________________________Payment completed_________________________________"
print ""
print "Thank you for purchasing ticket from Kelana Jaya LRT ticketing system"

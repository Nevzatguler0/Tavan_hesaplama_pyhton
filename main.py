price = float(input("Price: "))
limit = int(input("Limit: "))
number = int(input("How many: "))

limit1 = price + (price*10)/100
limit2 = limit1 + (limit1*10)/100
limit3 = limit2 + (limit2*10)/100
limit4 = limit3 + (limit3*10)/100
limit5 = limit4 + (limit4*10)/100
limit6 = limit5 + (limit5*10)/100
limit7 = limit6 + (limit6*10)/100
limit8 = limit7 + (limit7*10)/100
limit9 = limit8 + (limit8*10)/100
limit10 = limit9 + (limit9*10)/100

if limit == 1:
    print("Tavan1:",limit1)
    print("Kar:",(limit1-price)*number)

elif limit == 2:
    print("Tavan2:",limit2)
    print("Kar:",(limit2-price)*number)

elif limit == 3:
    print("Tavan3:",limit3)
    print("Kar:",(limit3-price)*number)

elif limit == 4:
    print("Tavan4:",limit4)
    print("Kar:",(limit4-price)*number)

elif limit == 5:
    print("Tavan5:",limit5)
    print("Kar:",(limit5-price)*number)

elif limit == 6:
    print("Tavan6:",limit6)
    print("Kar:",(limit6-price)*number)

elif limit == 7:
    print("Tavan7:",limit7)
    print("Kar:",(limit7-price)*number)

elif limit == 8:
    print("Tavan8:",limit8)
    print("Kar:",(limit8-price)*number)

elif limit == 9:
    print("Tavan9:",limit9)
    print("Kar:",(limit9-price)*number)

elif limit == 10:
    print("Tavan10:",limit10)
    print("Kar:",(limit10-price)*number)

else:
    print("ERROR")
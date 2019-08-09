GrShip = "By standard ground shipping:"
PGrShip = "By premium ground shipping:"
Drone_ship = "By drone shipping:"

# Type something between 0-20 lb into "w_float"
w_float = 13

def ground_shipping_price(weight):
  print("Your shipment weight: "+str(weight)+" lb. will charge you:")
  Premium_gprice = 125
  if weight <= 2:
    gprice = (weight * 1.50) + 20
    print(str(GrShip) +" $"+ str(gprice) +",-")
    print(str(PGrShip) +" $"+ str(Premium_gprice) +",-")
    return Premium_gprice, gprice
  elif weight > 2 and weight <= 6:
    gprice = (weight * 3) + 20
    print(str(GrShip) +" $"+ str(gprice) +",-")
    print(str(PGrShip) +" $"+ str(Premium_gprice) +",-")
    return Premium_gprice, gprice
  elif weight > 6 and weight <= 10:
    gprice = (weight * 4) + 20
    print(str(GrShip) +" $"+ str(gprice) +",-")
    print(str(PGrShip) +" $"+ str(Premium_gprice) +",-")
    return Premium_gprice, gprice
  elif weight > 10:
    gprice = (weight * 4.75) + 20
    print(str(GrShip) +" $"+ str(gprice) +",-")
    print(str(PGrShip) +" $"+ str(Premium_gprice) +",-")
    return Premium_gprice, gprice
  else:
    return "How?"

def drone_shipping_price(weight):
  if weight <= 2 :
    drone_price = weight * 4.50
    print(Drone_ship +" $"+ str(drone_price)+",-")
    return drone_price
  elif weight > 2 and weight <= 6 :
    drone_price = weight * 9
    print(Drone_ship +" $"+ str(drone_price)+",-")
    return drone_price
  elif weight > 6 and weight <= 10 :
    drone_price = weight * 12
    print(Drone_ship +" $"+ str(drone_price)+",-")
    return drone_price
  elif weight > 10 :
    drone_price = weight * 14.25
    print(Drone_ship +" $"+ str(drone_price)+",-")
    return drone_price
  else:
    return "How?"

def shipping(weight):
  premium_gprice,gprice = ground_shipping_price(weight)
  drone_price = drone_shipping_price(weight)
  if drone_price < gprice and drone_price < premium_gprice :
    print("")
    print("The cheapest shipping method is by drone.")
    print(str(weight)+" Pounds will therefore cost you: $"+ str(drone_price)+",-")
    return
  elif gprice < drone_price and gprice < premium_gprice :
    print("")
    print("The cheapest shipping method is standard ground shipping.")
    print(str(weight)+" Pounds will therefore cost you: $"+ str(gprice)+",-")
    return
  else:
    print("")
    print("The cheapest shipping method is premium ground shipping.")
    print(str(weight)+" Pounds will therefore cost you: $"+ str(premium_gprice)+",-")
    return

shipping(w_float)


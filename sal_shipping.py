weight = 0
flat_charge = 20.00

# weight = 8.4
# weight = 4.8
weight = 41.5

# Ground Shipping
if weight <= 2:
  ground_cost = (weight*1.50) + flat_charge
elif weight > 2 and weight <= 6:
  ground_cost = (weight*3.00) + flat_charge
elif weight > 6 and weight <= 10:
  ground_cost = (weight*4.00) + flat_charge
else:
  ground_cost = (weight*4.75) + flat_charge

# print(ground_cost)

premium_cost = 125.00
# print(premium_cost)

# weight = 1.5

# Drone Shipping
if weight <= 2:
  drone_cost = (weight*4.50)
elif weight > 2 and weight <= 6:
  drone_cost = (weight*9.00)
elif weight > 6 and weight <= 10:
  drone_cost = (weight*12.00)
else:
  drone_cost = (weight*14.25)

# print(drone_cost)


if ground_cost<premium_cost and ground_cost<drone_cost:
  print("Ground Shipping is the cheapest and costs " + str(ground_cost))

if premium_cost<ground_cost and premium_cost<drone_cost:
  print("Ground Shipping Premium is the cheapest and costs " + str(premium_cost))

if drone_cost<premium_cost and drone_cost<ground_cost:
  print("Drone shipping is the cheapest and costs " + str(ground_cost))  

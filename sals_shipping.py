# Sal's Shipping
# Use the values from the project as flat_charge_ground = 20, flat_charge_premium = 125, flat_charge_drone = 0

weight = float(input("weight: "))
flat_charge_ground = float(input("flat charge ground shipping: "))
flat_charge_premium = float(input("flat charge ground premium shipping: "))
flat_charge_drone = float(input("flat charge ground drone shipping: "))

# Ground shipping

if weight <= 2:
  cost_ground = 1.5*weight + flat_charge_ground 
elif weight <= 6:
  cost_ground = 3*weight + flat_charge_ground 
elif weight <= 10:
  cost_ground = 4*weight + flat_charge_ground 
else:
  cost_ground = 4.75*weight + flat_charge_ground
print("The cost of ground shipping:",cost_ground)

# Ground shipping premium

cost_ground_premium = flat_charge_premium 
print("The cost of ground shipping premium:",cost_ground_premium )


# Ground shipping Drone

if weight <= 2:
  cost_ground_drone = 4.5*weight + flat_charge_drone
elif weight <= 6:
  cost_ground_drone = 9*weight + flat_charge_drone
elif weight <= 10:
  cost_ground_drone = 12*weight + flat_charge_drone
else:
  cost_ground_drone = 14.25*weight + flat_charge_drone
print("The cost of drone shipping :",cost_ground_drone)


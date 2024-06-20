package_weight = float(input("What is the weight of your package (lbs)? ")) #FC1

if (package_weight < 0): #FC2
    print("ERROR!\nWeight should be a positive value\n(What are you shipping? Air?!)") #FC7

elif (package_weight <= 2): #FC3
    shipping_rate = 1.50 #FC8
    total_cost = package_weight * shipping_rate 
    print(f"Shipping Rate: ${shipping_rate:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
elif (package_weight > 2 and package_weight <= 6): #FC4
    shipping_rate = 3.00 #FC9
    total_cost = package_weight * shipping_rate #FC12
    print(f"Shipping Rate: ${shipping_rate:.2f}") #FC13
    print(f"Total Cost: ${total_cost:.2f}") #FC14
elif (package_weight > 6 and package_weight <= 10): #FC5
    shipping_rate = 4.00 #FC10
    total_cost = package_weight * shipping_rate 
    print(f"Shipping Rate: ${shipping_rate:.2f}")
    print(f"Total Cost: ${total_cost:.2f}") 
else: #FC6
    shipping_rate = 4.75 #FC11
    total_cost = package_weight * shipping_rate 
    print(f"Shipping Rate: ${shipping_rate:.2f}") 
    print(f"Total Cost: ${total_cost:.2f}") 
  
# Bread prices
hamburger = 65
sandwich = 45
Baguette = 30

# Noodle prices
fried_noodle = 65
beef_rice_noodle = 70
stir_fried_noodle = 75

# Beverage prices
black_tea = 15
Milk_tea = 20
soybean_milk = 15

# Print menu
print()
print(" {:->91}".format(""))
print("|{:^91}|".format("Breakfast Menu"))

print("|{:->91}|".format(""))
print("|{:^30}|{:^29}|{:^30}|".format("Bread", "Noodle", "Beverage"))
print("|{:->91}|".format(""))

print("| 1.Hamburger {:.>16} | 1.Pork fried noodle {:.>7} | 1.Black tea {:.>16} |".format(hamburger, fried_noodle,
                                                                                          black_tea))
print("| 2.Club sandwich {:.>12} | 2.Beef rice noodle {:.>8} | 2.Milk tea {:.>17} |".format(sandwich, beef_rice_noodle,
                                                                                            Milk_tea))
print("| 3.Baguette {:.>17} | 3.Stir fried noodle {:.>7} | 3.Soybean milk {:.>13} |".format(Baguette,
                                                                                            stir_fried_noodle,
                                                                                            soybean_milk))
print(" {:->91}".format(""))
print("\nPlease enter your choice: ")

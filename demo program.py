#Name: George Sono
#Class: CSE20 (Assignment 10.1 DEMO PROGRAM)
#Prof: Harikishna Kuttivelil
#Description:
  #A quick demo program to show case my Car classes from asgn10_1.py. I will recreate a typical fast and furious movie 

from asgn10_1 import *

def main(): 
  #we have to make our protagonist first!
  protagonist = "Brian O' Connor"
  #the protagonist's car!
  protagonist_car = CombustionEngineCar("Godzilla", "R-34 Skyline", protagonist, "Nissan", cylinders = 6, engine_layout = "inline", octane_rating = 90) #creating the CombustionEngineCar instance
  print(f"Description of {protagonist}'s Car:\n{str(protagonist_car)}\n") #string casting the instance to get an obj description

  #lets create the dragstrip where our protagonist is going to race!
  dragstrip = DragStrip()
  #lets make the antagonist!
  antagonist = "Evil Dom Torreto"
  antagonist_car = CombustionEngineCar("Hellcat", "Challenger", antagonist, "Dodge", cylinders = 8, engine_layout = "v", octane_rating = 90) #creating the CombustionEngineCar instance

  #brian is going to go on first race (he will most-likely lose for story purposes)
  print(f"{protagonist}'s FIRST RACE!!\n")
  print(f"Opponent Vehicle Description: \n\n{str(antagonist_car)}\n") #string casting the instance to get an obj description (__str__ magic method)
  
  print(dragstrip.race_cars(protagonist_car, antagonist_car))

  #Wow it turns out he lost! What a shock! Looks like he has to add some upgrades
  print(f"\nUPGRADING {protagonist_car.get_owner()}'s CAR...")
  print(f"THE CAR IS FULLY UPGRADED!")
  protagonist_car.add_turbo() #TURBO UPGRADE! HP UPGRADE! updating the air_intake
  protagonist_car.upgrade_fuel_injection() #FUEL INJECTION UPGRADE! HP UPGRADE! setting the fuel_injection attribute to "aftermarket"
  protagonist_car.upgrade_exhaust() #EXHAUST UPGRADE! HP UPGRADE! setting the exhaust attribute to "aftermarket"
  protagonist_car.quick_stats() #LETS VIEW HIS STATS ON HIS NEW CAR!! we dont need to print because the method prints and doesn't returny anything

  #WOW he's going to race his rival now (in the dragstrip)! Who will win??
  print(f"\n{protagonist}'s SECOND RACE!!\n")
  print(dragstrip.race_cars(protagonist_car, antagonist_car)) #using the race_car method to race the protagnist and antagonist car


if __name__ == "__main__":
  main()
#Name: George Sono
#Class: CSE20 (Assignment 10.1)
#Prof: Harikishna Kuttivelil
#Description:
#Class Car
  #This is a basic parent class which has the basic outline of a car. This means that its data variables are the car’s name (self.__car_name), the model of the car (self.__model), the owner of the car (self.__car_name) and the manufacturer of the car (self.__manufacturer). (see README for more info)

#Class CombustionEngineCar(Car):
  #As CombustionEngineCar Class is a child class of the parent class Car, it inherits the data variables of car_name, model, owner and manufacturer. With the super() function, it’s able to use the get methods mentioned in the Car class method description. The new parameters to create an instance of this class are: cylinders, engine_layout, octane_rating, air_intake, exhaust, fuel_injection. However, these extra parameters are by default set to an average vehicle (specifically a Honda Civic). (see README for more info)

#Class ElectricCar(Car):
  #The Electric Car class - a child of class Car - inherits the car_name, model, owner and manufacturer parameters and methods with super(). Regarding the other attributes, motors, motor wattage and battery range, these are set to a default value of a Nissan Leaf if not defined when creating the instance. As electric vehicles compared to gasoline vehicles have considerably less moving parts and have less parts, I thought it would be fitting if it had less parameters compared to the CombustionEngine class. (see README for more info)

import random as r

class Car:

  #Constructor: required parameters needed are: car_name, model, owner, manufacturer
  def __init__(self,car_name, model, owner, manufacturer):
    self.__car_name = car_name
    self.__model = model
    self.__owner = owner
    self.__manufacturer = manufacturer
  #Get methods:
  def get_car_name(self):
    return self.__car_name
  def get_model(self):
    return self.__model
  def get_owner(self):
    return self.__owner
  def get_manufacturer(self):
    return self.__manufacturer
  #Str magic method
  def __str__(self):
    return f"{self.__car_name} is owned by {self.__owner}. {self.__car_name} is manufactured by {self.__manufacturer} and its model is the {self.__model}."

class CombustionEngineCar(Car):
  #class attribute
  uses_gas = True
  #Constructor (default values are set to a Honda Civic)
  def __init__(self, car_name, model, owner, manufacturer, cylinders = 4, engine_layout = "inline", octane_rating = 85, air_intake = "stock", exhaust = "stock", fuel_injection = "stock"):
    #Inherit Car class parameters with super()
    super().__init__(car_name,model,owner,manufacturer)
    self.__cylinders = cylinders
    self.__engine_layout = engine_layout
    self.__octane_rating = octane_rating
    self.__air_intake = air_intake
    self.__exhaust = exhaust
    self.__fuel_injection = fuel_injection

  #Add air_intake mods
  def add_turbo(self):
    self.__air_intake = "turbo-charger"

  def add_supercharger(self):
    self.__air_intake = "super-charger"    

  #Add fuel injection and exhaust systems to "after market"
  def upgrade_fuel_injection(self):
    self.__fuel_injection = "aftermarket"
  
  def upgrade_exhaust(self):
    self.__exhaust = "aftermarket"

  #returns a dictionary regarding engine stats
  def engine(self):
    return {"layout": self.__engine_layout, "cylinders": self.__cylinders}

  #if air_intake, exhaust and fuel injection is stock it'll return True, otherwise False
  def is_it_stock(self):
    if self.__air_intake == "stock" and self.__fuel_injection == "stock" and self.__exhaust == "stock":
      return True
    else:
      return False


  #calculates the horsepower of the instance if some of the attributes are/are not stock, this will increase the horsepower rating.
  def get_horsepower(self):
    hp = 0
    #for loop adding 35 hp per cylinder
    for power in range(self.__cylinders):
      hp += 35
    if self.__air_intake != "stock":
      if self.__air_intake == "turbo-charger" or self.__air_intake == "supercharger":
        hp += 75
    if self.__octane_rating > 90:
      hp += 5
    if self.__exhaust != "stock":
      hp += 20
    if self.__fuel_injection != "stock":
      hp += 20 
    return hp

  #method uses get_wheel_horsepower and reduces the hp value by 20 to account for losses in the transfer of energy
  def get_wheel_horsepower(self):
    hp = self.get_horsepower()
    energy_loss_to_the_differential = 20
    whp = hp - energy_loss_to_the_differential
    return whp

  #This method prints an overview of the car’s important stats:
  def quick_stats(self):
    print(f"---CAR---")
    print(f"Name: {self.get_car_name()}")
    print(f"HP: {self.get_horsepower()}")
    print(f"Wheel HP: {self.get_wheel_horsepower()}")
    print(f"Stock?: {self.is_it_stock()}")
  
  #Magic method that returns a description of the car when string casting the instance
  def __str__(self):
    return f"{self.get_car_name()} has an internal combustion engine and is owned by {self.get_owner()}. {self.get_car_name()} is manufactured by {self.get_manufacturer()} and its model is the {self.get_model()}. Its engine has {self.__cylinders} cylinder(s) in a '{self.__engine_layout}' configuration. At the crankshaft of {self.get_car_name()}'s engine, it outputs {self.get_horsepower()} horsepower and at the wheels outputs {self.get_wheel_horsepower()} horsepower."
  
class ElectricCar(Car):
  #class attribute: since the car is electric it doesnt use gas so the runs_gas attribute is always False, regardless of instance
  runs_gas = False
  
  #Constructor: the default parameters are of a nissan leaf
  def __init__(self, car_name, model, owner, manufacturer, motors = 1, motor_wattage = 110, battery_range = 151):
    super().__init__(car_name,model,owner,manufacturer)
    self.__motors = motors
    self.__battery_range = battery_range
    self.__motor_wattage = motor_wattage

  #Replacing the motor (new motor requires how many motors and the wattage of the motors being added)
  def replace_motor(self, motor_tuple):
    #iterating through the tuple by index
    self.__motors = motor_tuple[0]
    self.__motor_wattage = motor_tuple[1]
  
  #Method uses a for loop to add 100 hp per motor and 2.5 hp per motorwattage/2. It returns the horsepowe value as a integer
  def get_horsepower(self):
    hp = 0
    for power in range(self.__motors):
      hp += 100

    for power in range(int(self.__motor_wattage/2)):
      hp += 1.5
    
    return hp

  #Method prints a quick overview of the Car's vital stats
  def quick_stats(self):
    print(f"---CAR---")
    print(f"Name: {self.get_car_name()}")
    print(f"HP: {self.get_horsepower()}")
    print(f"Motors: {self.__motors}")
    print(f"Wattage: {self.__motor_wattage} kW")
    print(f"Battery Range: {self.__battery_range} miles")
    
  #Method returns a dictonary regarding the amount of motors, motor wattage and battery range
  def powertrain(self):
    return {"motors":self.__motors, "wattage": self.__motor_wattage, "battery range": self.__battery_range}

  #Magic method provides a description of the car's attributes 
  def __str__(self):
    return f"{self.get_car_name()} is an electric vehicle owned by {self.get_owner()}. {self.get_car_name()} is manufactured by {self.get_manufacturer()} and its model is the {self.get_model()}. It has {self.__motors} motor(s) which outputs {self.get_horsepower()} horsepower."

class DragStrip:
  #class attribute: the dragstrip made of is tarmac
  material = "tarmac"
  
  #Method takes in a car's horsepower rating and converts it into a quarter mile time 
  def run_quarter_mile(self, car):
    #these times are determined by the car's horsepower
    if car.get_horsepower() < 100 and car.get_horsepower() >= 50:
      return round(r.uniform(17,21),2)
    if car.get_horsepower() < 150 and car.get_horsepower() >= 100:
      return round(r.uniform(15,17),2)
    if car.get_horsepower() < 200 and car.get_horsepower() >= 150 :
      return round(r.uniform(13,15),2)
    if car.get_horsepower() < 250 and car.get_horsepower() >= 200 :
      return round(r.uniform(11,13),2)
    if car.get_horsepower() < 300 and car.get_horsepower() >= 250 :
      return round(r.uniform(10,13),2)
    if car.get_horsepower() < 350 and car.get_horsepower() >= 300 :
      return round(r.uniform(9,11),2)
    if car.get_horsepower() < 400 and car.get_horsepower() >= 350 :
      return round(r.uniform(8,10),2)
    if car.get_horsepower() < 450 and car.get_horsepower() >= 400 :
      return round(r.uniform(7,8),2)
    if car.get_horsepower() < 500 and car.get_horsepower() >=  450 :
      return round(r.uniform(7,8),2)
    if car.get_horsepower() > 500: 
      return round(r.uniform(5,7),2)

  #Method takes in a car's horsepower rating and converts it into a quarter mile time 
  def run_0_60(self,car):
    return round(self.run_quarter_mile(car) * (r.uniform(0.3,0.4)),2)

  #Method takes in two cars and races them on a drag strip. First car to cross a quarter mile wins. It outputs the winner and loser times for 0-60mph and 1/4 mile.
  def race_cars(self,car_1,car_2):
    #if car 1 wins
    if (self.run_quarter_mile(car_1)) < (self.run_quarter_mile(car_2)):
      return f"---RACE RESULTS---\nWINNER: {car_1.get_owner()}\n\t1/4 mile: {self.run_quarter_mile(car_1)} seconds\n\t0-60: {self.run_0_60(car_1)} seconds\nLOSER: {car_2.get_owner()}\n\t1/4 mile: {self.run_quarter_mile(car_2)} seconds\n\t0-60: {self.run_0_60(car_2)} seconds"
    #if car 2 wins
    else:
      return f"---RACE RESULTS---\nWINNER: {car_2.get_owner()}\n\t1/4 mile: {self.run_quarter_mile(car_2)} seconds\n\t0-60: {self.run_0_60(car_2)} seconds\nLOSER: {car_1.get_owner()}\n\t1/4 mile: {self.run_quarter_mile(car_1)} seconds\n\t0-60: {self.run_0_60(car_1)} seconds"
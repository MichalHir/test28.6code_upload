# list, add, delete, search
from cars.actions import add_car, delete_car, list_cars, search_car
from json_functions import read_json, save_json
from problems.problems import total_sum_of_garage


cars=[{"car_number":9284759, "problems":["Engine","Break"]},{"car_number":3754891, "problems":["Engine","Break"]}]
def menu():
    while True:
        # cars=read_json()
        print("welcome to the garage")
        print("write 1 if you want to print all of the cars")
        print("write 2 if you want to add a car")
        print("write 3 if you want to delete a car")
        print("write 4 if you want to search the list")
        print("write 5 if you want to sum of all cars treatments")
        print("write 6 if you want to exit the menu")
        choice = input("enter your choice\n")
        if choice == "1":
            print_txt=list_cars(cars)
            if print_txt=="":
                print ("no cars in the garage")
            else:
                print (print_txt)
        if choice == "2":
            add_car(cars)
        if choice == "3":
            delete_car(cars)
        if choice == "4":
            search_car_txt=search_car(cars)
            if search_car_txt=="":
                print ("no search results")
            else:
                print (search_car_txt)
        if choice == "5":
            total_sum_of_garage(cars)
        if choice == "6":
            print("goodbye")
            break
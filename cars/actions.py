# list, add, delete, search
# from json_functions import save_json
from json_functions import save_json
from problems.problem_menu import add_problems
from problems.problems import calculate_total_price
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def list_cars(cars_array):
    clear_terminal()
    cars_str=""
    for index, car in enumerate(cars_array):
        cars_str +=f"{index+1} car number: {car["car_number"]} car problems: {car["problems"]}\n"
    return cars_str


def add_car(cars_array):
    clear_terminal()
    problems = add_problems()
    sum = calculate_total_price(problems)
    permission=input(print (f"the price of this fix is {sum} do you wish to proceed? write yes/no:"))
    if permission =="yes":
        car_number = input("what is the car number?\n")
        new_car = {"car_number": car_number, "problems": problems}
        cars_array.append(new_car)
        save_json(cars_array)
        return print("that car has been added")
    else:
        return print("that car has not been added")


def delete_car(cars_array):
    clear_terminal()
    if len(cars_array) == 0:
        return print("no cars in the garage")
    print(list_cars(cars_array))
    choice=int(input(f"write the number 1-{len(cars_array)} of the car to want to delete\n"))
    cars_array.remove(cars_array[choice-1])
    save_json(cars_array)
    return print("that car has been deleted")



def search_car(cars_array):
    clear_terminal()
    search_str=""
    search_txt=str(input("What is the search term\n"))
    for index, car in enumerate(cars_array):
        if search_txt in str(car["car_number"]):
            search_str +=f"{index+1} car number: {car["car_number"]} car problems: {car["problems"]}\n"
    return search_str

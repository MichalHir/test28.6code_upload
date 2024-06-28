problems_list = [
    "Engine",
    "Breaks",
    "5000_km_treatment",
    "10,000 km treatment",
    "Filters+ Oil",
    "Gear",
]


def add_problems():
    from cars.actions import clear_terminal

    # creates list of problems of the car
    car_problems_list = []
    clear_terminal()
    while True:
        print("please select the car's problems:")
        print(f"1-{problems_list[0]}")
        print(f"2-{problems_list[1]}")
        print(f"3-{problems_list[2]}")
        print(f"4-{problems_list[3]}")
        print(f"5-{problems_list[4]}")
        print(f"6-{problems_list[5]}")
        print("write 7 if you finished adding car problems")
        choice = int(input("enter your choice\n"))
        if choice == 7:
            return car_problems_list
        else:
            if problems_list[choice - 1] in car_problems_list:
                print("this problem has been added before")
            else:
                car_problems_list.append(problems_list[choice - 1])

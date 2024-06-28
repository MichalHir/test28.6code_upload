cost = [
    ("Engine", 2000),
    ("Breaks", 1000),
    ("5000_km_treatment", 500),
    ("10,000 km treatment", 1000),
    ("Filters+ Oil", 250),
    ("Gear", 1000),
]


def calculate_total_price(problem_array):
    # calaulates price to fix one car
    sum = 0
    for price in cost:
        if price[0] in problem_array:
            sum += int(price[1])
    return sum


def total_sum_of_garage(cars_array):
    from cars.actions import clear_terminal

    clear_terminal()
    # calaulates price to fix of all cars
    sum = 0
    for car in cars_array:
        sum += calculate_total_price(car["problems"])
    print(f"Currently there are {len(cars_array)} cars . The current profit is: {sum}")

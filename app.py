import json

cars = []
my_file= "mydata.json"

def print_all_cars():
    for car in cars:
        print(f'Your car: {car}')

def save_cars_to_json():
    with open("mydata.json", 'w') as file:
        json.dump(cars, file)

def load_cars_from_json():
    global cars
    try:
        with open(my_file, 'r') as file:
            cars = json.load(file)
        print("data loaded")
    except: 
        print("data file not found")
    

def main():
    load_cars_from_json()
    while True:
        print("a - add a car")
        print("p - print all cars")
        print("x - exit")
        user_selection = input("Your selection: ")
        
        if user_selection == 'a':
            cars.append('red')  # For the sake of example, adding 'red' as a placeholder
        elif user_selection == 'x':
            save_cars_to_json()
            print(f'All cars saved to {my_file}')
            exit()
        elif user_selection == 'p':
            print_all_cars()
        else:
            print("Select from menu only")

if __name__ == '__main__':
    main()

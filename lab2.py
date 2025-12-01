def display_main_menu():
    print("Enter Some Numbers Separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")

    number_list = []
    for x in string_list:
        number_list.append(int(x))
    return number_list

def cal_average(num):
    print("Calculated Average Temperature")

    total = 0

    for x in num:
        total += int(x)
    
    avg = total/len(num)
    print (" Average TEmperature", avg)

    

def fine_min_max(num):
    print("Minimum and Maximum")

    

    maximum = max(num)
    minimum = min(num)

    print ("Maximum", maximum)
    print ("Minimum", minimum)

def sort_temperature():
    print("Sort Teemperature")

def cal_median_temp():
    print("Median Temperature")

def main():
    display_main_menu()
    numbers = get_user_input()
    print ("YOU ENTERED", numbers)
    cal_average(numbers)
    fine_min_max(numbers)

if __name__ == "__main__":
    main()
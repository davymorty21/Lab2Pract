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

def sort_temperature(num):
    print("Sort Teemperature")

    sorted_list = sorted(num)
    print (sorted_list)
    return sorted_list


def cal_median_temp(num):
    print("Median Temperature")
    sorted_list = sort_temperature(num)

    length = len(sorted_list)

    if length % 2 == 0:
        mid1 = length // 2 -1
        mid2 = length // 2
        median = (sorted_list[mid1]+sorted_list[mid2])//2
    else:
        mid = length // 2
        median = sorted_list[mid]
    
    print (median)

def main():
    display_main_menu()
    numbers = get_user_input()
    print ("YOU ENTERED", numbers)
    cal_average(numbers)
    fine_min_max(numbers)
    sort_temperature(numbers)
    cal_median_temp(numbers)

if __name__ == "__main__":
    main()
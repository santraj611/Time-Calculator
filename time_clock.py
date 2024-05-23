import time

def get_final_time():
    """Get the Final time till user want to count time"""

    print("What is final time? (HH:MM)")
    final_time = input()
    if ":" in final_time:
        final_time = [int(i) for i in final_time.split(":")]
    elif "-" in final_time:
        final_time = [int(i) for i in final_time.split("-")]
    else:
        print("Please enter a valid time")
        get_final_time()
    
    return final_time

def get_time():
    """Gets time that user wants to add or subtract"""

    print("What is the time that you want add or subtract? (HH:MM)")
    final_time = input()
    if ":" in final_time:
        final_time = [int(i) for i in final_time.split(":")]
    elif "-" in final_time:
        final_time = [int(i) for i in final_time.split("-")]
    else:
        print("Please enter a valid time")
        get_final_time()
    
    return final_time

def add_time(opperator, time_for_addition):
    """For adding and subtracting time"""

    current_time = time.strftime("%H:%M:%S")
    hours, minutes, seconds = current_time.split(":")
    hours, minutes, seconds= int(hours), int(minutes), int(seconds)
    future_time = []
    if opperator == "+":
        future_hours = hours + time_for_addition[0]
        future_min = minutes + time_for_addition[1]
        future_time = [future_hours, future_min]
    elif opperator == "-":
        future_hours = hours - time_for_addition[0]
        future_min = minutes - time_for_addition[1]
        future_time = [future_hours, future_min]
    else:
        print("opperator is invalid")

    if future_time[1] > 60:
        future_time[0] += 1
        future_time[1] -= 60
    elif future_time[1] < 0:
        future_time[0] -= 1
        future_time[1] += 60
    else:
        print("Somthing went wrong")

    return f"Future time will be {future_time[0]}:{future_time[1]}"

def rem_time(final_time):
    current_time = time.strftime("%H:%M:%S")
    hours, minutes, seconds = current_time.split(":")
    rem_hours = final_time[0] - int(hours)
    rem_min = final_time[1] - int(minutes)
    if rem_min < 0:
        rem_min += 60
        rem_hours -= 1
    elif rem_hours < 0:
        print("Please Input time in correct formate")
    
    return f"Remaing time is {rem_hours}:{rem_min}"

def main():
    run = True
    while run:
        print()
        print("1. Do you want to add or subtract time?")
        print("2. Do you want to calculate tile the time?")
        print("3. Do you want to get the current time?")
        print("4. Do you want to get the current full time?")
        print("5. Do you want to exit?")
        print()

        choice = int(input("Enter your choice: "))
        if choice == 1:
            ask = input("What you want to do add (+) or subtract (-) \n type sign: ")
            if ask.strip() == "+":
                time_for_addition = get_time()
                print(add_time("+", time_for_addition))
            elif ask.strip() == "-":
                time_for_addition = get_time()
                print(add_time("-", time_for_addition))

        elif choice == 2:
            final_time = get_final_time()
            print(rem_time(final_time))
        elif choice == 3:
            print("Current time is", time.strftime("%H:%M"))
        elif choice == 4:
            print("Current time is", time.strftime("%H:%M:%S"))
        elif choice == 5:
            run = False

if __name__ == "__main__":
    main()

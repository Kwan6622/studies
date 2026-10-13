#15/07/2026
#Imagine that you live in a country where you have breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
#Make a program to tell you what to eat at a certain time
#1. Prompts for a time 
#2. divide the time into 2 parts
#3. check whether the time is within a time frame for a meal or not
#4. Return the meal name if is within time frame, else return none

def main():
    time = input("What time is it? ")
    print(convert(time))


def convert(time):
    time = time.strip().lower()

    if time.endswith("am"):
        time = time.removesuffix("am").strip()
        if hour == 12:
            hour = 0
    elif time.endswith("pm"):
        time = time.removesuffix("pm").strip()
        hour, minute = map(int, time.split(":"))
        if hour != 12:
            hour += 12
        time = f"{hour}:{minute}"

    f_time = format_time(time)

    if 7 <= f_time <= 8:
        return "breakfast time"
    elif 12 <= f_time <= 13:  
        return "lunch time"
    elif 18 <= f_time <= 19:
        return "dinner time"
    else:
        return "it's not time for any meal yet"

def format_time(time):
    hour, minute = map(int, time.split(":"))
    return hour + (minute / 60)

if __name__ == "__main__":
    main()
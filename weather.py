import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """    
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    import calendar
    
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #datetime()
    #fromisoformat < use this one
    #weekday() is a FUNCTION!!!
    raw_datetime = iso_string
    nice_date = datetime.fromisoformat(raw_datetime)

    year = nice_date.year
    month = nice_date.strftime("%B") #get month as word
    day = str(nice_date.day).zfill(2) #get day and make minimum 2 digits long ie. add 0 to single digit numbers
    day_index = nice_date.weekday() #use weekday() to return day of week as integer
    # print(day_index)

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    
    day_of_week = days[day_index] #using the weekday() result, index name of day in list

    # print(f"---- {day_of_week} {day} {month} {year} ----")
    return (f"{day_of_week} {day} {month} {year}")

# raw_datetime = "2021-10-31T07:00:00+08:00"
# expected_result = "Sunday 31 October 2021"
# result = convert_date(raw_datetime)
# print(result, "||", expected_result)





def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * (5/9)
    temp_in_celsius_round = round((temp_in_celsius),1)
    return temp_in_celsius_round

# temp_in_f = 90
# expected_result = 32.2
# result = convert_f_to_c(temp_in_f)
# print(result, expected_result)

# temp_in_f = "77"
# expected_result = 25.0
# result = convert_f_to_c(temp_in_f)
# print(result, expected_result)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # weather_data_min = weather_data #min column[]
    # weather_data_max = [max_list]
    # total_min = sum(weather_data_min)
    # total_max = sum(weather_data_max)

    if all(isinstance(item, str) for item in weather_data): #checks if all values in list are string
        #weather_data_list = [int(value) for value in weather_data]
        weather_data_list = [float(value) for value in weather_data]

        #float(weather_data_list) - this does not work because it is a list of values 
        float_list = []
        for val in weather_data_list:
            float_list.append(float(val))

            
        float_list = [float(val) for val in weather_data_list]

    else:
        weather_data_list = weather_data

    num_elements = len(weather_data_list) #count number of elements in list
    
    sum_weather_data = sum(weather_data_list) #sum all elements in list

    mean_weather = float(sum_weather_data / num_elements) #calc mean

    return mean_weather
   
# weather_data = [49, 57, 56, 55, 53]
# expected_result = 54
# result = calculate_mean(weather_data)
# print(result, expected_result)

# weather_data = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
# expected_result = 52.90375
# result = calculate_mean(weather_data)
# print(result, expected_result)

# weather_data = ["51", "58", "59", "52", "52", "48", "47", "53"]
# expected_result = 52.5
# result = calculate_mean(weather_data)
# print(result, expected_result)

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    
    with open(csv_file, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data) 
        next(csv_reader) #need to skip row header

        #make new list to store the csv data as per David's example
        raw_weather_data = []
            # for val in csv_reader:
            #     weather_data.append(float(val))

        for row in csv_reader:
            if row != []: #catch empty rows
                # for val in row[1] and row[2]:
                #     return float(val)
                raw_weather_data.append(row)
        # print(raw_weather_data)

    int_weather_data = []
    for row in raw_weather_data:
        row[0] = (row[0]) #CONVERT TO ISO FORMAT DATETIME!? OR FORMAT INTO "TABLE"?!
        row[1] = int(row[1])
        row[2] = int(row[2])
        int_weather_data.append(row)

    # print(int_weather_data)
    return int_weather_data

    # for row in int_weather_data:
    #     if row != []:
    #         print(row)

              
        
    #print([date, min , max])

# result = load_data_from_csv("tests/data/example_one.csv")
# print(result)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0:
        return ()

    else:

        min_temp = float(min(weather_data)) #find minimum using min() and then change to float
        index_min_temp = len(weather_data) - weather_data[::-1].index(min(weather_data)) - 1 #(count elements in list) - (invert list, then return index of min number) - (minus 1 because list flipped)
        return min_temp, index_min_temp
     


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if len(weather_data) == 0:
        return ()
    
    else:
        max_temp = float(max(weather_data))
        index_max_temp = len(weather_data) - weather_data[::-1].index(max(weather_data)) - 1
        return max_temp, index_max_temp
    
# temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
# expected_result = (14.5, 1)
# result = find_max(temperatures)
# print(result, expected_result)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    date_list = []
    min_list = []
    max_list = []

    for row in weather_data:
        date_list.append(row[0])
        min_list.append(row[1])
        max_list.append(row[2])

    number_of_days = len(min_list)

    daily_min = min(min_list)
    daily_max = max(max_list)

    index_min = min_list.index(daily_min)
    date_of_mintemp = date_list[index_min]
    day_of_mintemp = convert_date(date_of_mintemp)
    
    index_max = max_list.index(daily_max)
    date_of_maxtemp = date_list[index_max]
    day_of_maxtemp = convert_date(date_of_maxtemp)
    
    daily_min_degc = format_temperature(convert_f_to_c(daily_min))
    daily_max_degc = format_temperature(convert_f_to_c(daily_max))

    print(daily_min_degc, day_of_mintemp) #1
    print(daily_max_degc, day_of_maxtemp) #2

    mean_min = calculate_mean(min_list)
    mean_max = calculate_mean(max_list)

    mean_min_degc = format_temperature(convert_f_to_c(mean_min)) #3
    mean_max_degc = format_temperature(convert_f_to_c(mean_max)) #4

    print(mean_min_degc, mean_max_degc)

    summary = ""

    summary += (f"{number_of_days} Day Overview\n")
    summary += (f"  The lowest temperature will be {daily_min_degc}, and will occur on {day_of_mintemp}.\n")
    summary += (f"  The highest temperature will be {daily_max_degc}, and will occur on {day_of_maxtemp}.\n")
    summary += (f"  The average low this week is {mean_min_degc}.\n")
    summary += (f"  The average high this week is {mean_max_degc}.\n")

    # print(summary)
    return summary


# example_one = [
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]

# with open("tests/expected_output/example_one_summary.txt", encoding="utf8") as txt_file:
#     expected_result = txt_file.read()
# result = generate_summary(example_one)
# print(expected_result,result)


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = ""

    for row in weather_data:
        daily_summary += (f"---- {convert_date(row[0])} ----\n")
        daily_summary += (f"  Minimum Temperature: {format_temperature(convert_f_to_c(row[1]))}\n")
        daily_summary += (f"  Maximum Temperature: {format_temperature(convert_f_to_c(row[2]))}\n")
        daily_summary += ("\n")

    # print(daily_summary)
    return daily_summary

    
# with open("tests/expected_output/example_one_daily_summary.txt", encoding="utf8") as txt_file:
#     expected_result = txt_file.read()
# result = generate_daily_summary(example_one)
# print(expected_result, result)


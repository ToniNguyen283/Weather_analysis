# Instructions:
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.

def read_weather_data(name):
    '''Reads weather data from a file and return a list of tuple'''
    data_list = []
    with open (name,'r') as f:
        for i in f.readlines():
            '''Strip any tab/space on the two ends of each line'''
            i = i.strip()
            '''Split the string in each line by the comacoma'''
            parts = i.split(',')
            '''Create a new tuple'''
            thistuple = (parts[0],float(parts[1]),float(parts[2]))

            data_list.append(thistuple)
    return data_list

def calculate_average_temperature(data):
    '''Calculates the average temperature from the weather data.'''
    sum_temp = 0
    for i in data:
        sum_temp+=i[1]
    return float(f'{sum_temp/len(data):.1f}')

def calculate_total_rainfall(data):
    '''Calculates the total rainfall from the weather data.'''
    sum_rainfall = 0
    for i in data:
        sum_rainfall+=i[2]
    return float(f'{sum_rainfall:.1f}')

def find_highest_temperature(data):
    '''Finds the highest temperature and the corresponding date from the weather data.'''
    highest_temp = data[1][1]
    for i in data:
        if i[1]>highest_temp:
            highest_temp = i[1]
            date = i[0]
    return (date,highest_temp)

def find_lowest_temperature(data):
    '''Finds the lowest temperature and the corresponding date from the weather data.'''
    lowest_temp = data[1][1]
    for i in data:
        if i[1]<lowest_temp:
            lowest_temp = i[1]
            date = i[0]
    return (date, lowest_temp)

def find_day_with_most_rainfall(data):
    '''Finds the day with the most rainfall from the weather data.'''
    most_rainfall = data[1][2]
    for i in data:
        if i[2]>most_rainfall:
            most_rainfall=i[2]
            date = i[0]
    return (date,most_rainfall)

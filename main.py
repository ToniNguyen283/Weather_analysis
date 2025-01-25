# main.py
from weather_analysis import*

def weather_analyze(file_path):
    '''Analyzes weather data from a file and prints the results.'''
    weather_data = read_weather_data(file_path)
    results = {'average temperature': calculate_average_temperature(weather_data), 'total rainfall': calculate_total_rainfall(weather_data), 
               'highest temperature': {'date':find_highest_temperature(weather_data)[0],'temperature':find_highest_temperature(weather_data)[1]},
               'lowest temperature': {'date': find_lowest_temperature(weather_data)[0],'temperature':find_lowest_temperature(weather_data)[1]},
               'most rainfall':{'date':find_day_with_most_rainfall(weather_data)[0],'rainfall': find_day_with_most_rainfall(weather_data)[1]}}
    return results
    

if __name__ == "__main__":
    file_path = 'weather.txt'
    results = weather_analyze(file_path) #or the path to the file
    print(results)

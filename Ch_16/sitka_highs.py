import csv 
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'death_valley_2018_simple.csv'
with open(filename) as f: 
    reader = csv.reader(f)
    header_row = next(reader)
     

    #get high temperatures, and dates from this file. 
    dates, highs, lows = [], [], []
    for row in reader: 
        current_date = datetime.strptime(row[2], '%Y-%m-%d') 
        try: 
            high = int(row[5]) 
            low = int(row[6]) 
        except ValueError: 
            print(f"Missing value for {current_date}") 
        else: 
            dates.append(current_date)
            highs.append(high)
            lows.append(low) 

   
#plot the high temperatures 
plt.style.use('seaborn') 
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red') 
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)

#Format the plot 
ax.set_title("Sitka, Alaska - High and low Temps for 2018", fontsize = 24) 
ax.set_xlabel('', fontsize=16) 
ax.set_ylabel("Temperature(F)", fontsize = 16)
fig.autofmt_xdate()
ax.tick_params(axis='both', which = 'major', labelsize = 16) 
plt.show()

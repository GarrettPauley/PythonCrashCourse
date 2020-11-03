from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#create a D6
die = Die()
#And another.
die_2 = Die(10)

#make some rolls, and store the results in this list 
results = [] #I'm the list 
for roll_num in range(50_000): 
    result = die.roll() + die_2.roll()
    results.append(result)

#Track the results
frequencies = []
max_result = die.num_sides + die_2.num_sides
#1 - 6 by default
for value in range(2, max_result + 1): 
    #count the number of 1's, 2's, 3's, 4's ... 
    occurance = results.count(value)
    frequencies.append(occurance)
print(frequencies)

#Histogram to view the results 

x_values = list(range(1,max_result + 1))
data = [Bar(x=x_values,y=frequencies)]
x_axis_config ={'title':'Results', 'dtick': 1}
y_axis_config ={'title':'Frequency of Results'}
graph_layout = Layout(title = "Rolling two  6 sided die 1000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout': graph_layout}, filename='D6_D6.html')
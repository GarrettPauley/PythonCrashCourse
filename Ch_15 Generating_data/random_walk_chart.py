import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True: 
    #Generate 5000 random steps. 
    rw = RandomWalk(50000)
    rw.fill_walk()

    #plot these points
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,edgecolors='none', s=2)
    #Emphasize the starting and stopping point
    ax.scatter(0,0, c='blue', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s = 50)
    #Get rid of the axes, the are distracting 

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("It's a nice evening for random walks, shall we take another? (y/n)")
    if keep_running == 'n': 
        break

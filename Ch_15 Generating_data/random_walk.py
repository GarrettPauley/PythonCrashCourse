from random import choice

class RandomWalk: 
    """ A class to generate a random walk. """
    def __init__(self, num_points = 5000): 
        self.num_points = num_points
        #The walk starts at (0,0) 

        self.x_values=[0] 
        self.y_values=[0] 
    def get_step_x(self): 
        #Get the step along the x axis, its direction and distance 
        x_direction = choice([1,-1])
        x_distance = choice([0,1,2,3,4])
        x_step = x_direction * x_distance
        return x_step
    def get_step_y(self): 
        #Get the step along the y axis, its direction and distance
        y_direction = choice([1,-1])
        y_distance = choice([0,1,2,3,4])
        y_step = y_direction * y_distance
        return y_step

    def fill_walk(self): 
        """CAlculate all the points in the walk."""


        #Keep walking until we have reached 5000 steps. 
        while len(self.x_values) < self.num_points: 
            #Decide which direction to go, and how far to walk. 
            x_step = self.get_step_x()
            y_step = self.get_step_y()

            #Check if the step goes nowhere. We wouldnt want that. 
            if x_step and y_step == 0: 
                continue
        
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            
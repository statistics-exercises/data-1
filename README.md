# Plotting data 

In this series of tasks, we are going to use what you have learned about variables, functions and logic to start investigating ideas from statistics.

In performing an investigation we will do a series of experiments and collect some data.  These experiments might be done in a lab or we might do a survey to determine the attitudes of individuals.  Our task as a statistician is to make sense of this data.  We must find out what the data is telling us about our experiment.

To give you a sense of what the task of statisticians looks like I have created some fake data.  If you click on the `data.dat` file you can look at this data.  What you will see is a single column of numbers.  Each of these numbers then corresponds to the outcome of an experiment. 

If you were called upon to analyse this data you would likely first try to plot the data to see if you can spot a pattern.  You are unlikely to spot the pattern by staring at the numbers but there is a chance that you might see the pattern in a plot.  

To complete this exercise I would, therefore, like you to use the python you have learned to generate a plot of the data in the `data.dat` file.   I have already created a numpy array called `x`.  This array contains the values contained in the `data.dat` file, which will be the y-coordinates of the points in your graph.  You should need to create an array holding the x coordinates.  These x-coordinates of points will be the integers from 1 up to 200 (the number of points in the file).  The first point in your graph will thus be plotted at `(1,x[0])`, the second will be at `(2,x[1])`, the third at `(3,x[2])` and so on.

You can set the variable npoints equal to the the number of elements in the numpy array `x` by using the command:

```
npoints = len( x ) 
````

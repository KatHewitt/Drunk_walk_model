# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:14:21 2019

@author: kath
"""

# Import modules required for model creation

import matplotlib
import matplotlib.pyplot
import agentframework2
import csv
import matplotlib.animation
import tkinter
import matplotlib.backends.backend_tkagg
import requests
import operator
import tkinter


environment = []
agents = []
Stored_moves = []
num_of_agents = 25


#plot size
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])



# open and read town.plan.txt (environment data)
f=open ("town.plan.txt")
reader=csv. reader (f, quoting = csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
    

#density map output, same size as environment
for i in range(300):
    rowlist = []
    for j in range(300):
        rowlist.append(0)
    Stored_moves.append(rowlist)
    

#locate the pub using environment data which as been assigned a value of 1 
for y, row in enumerate(environment):
    for x, value in enumerate (row):
        if value==1:
            startx=x
            starty=y
            
# Assign each agent a house number
#append the agents starting point to the pubs location 
for j in range(num_of_agents):
    number = (j+1)*10
    agents.append(agentframework2.Agent(environment, agents, number, startx, starty))

#plot of the agents start location - to make sure they start at the pub 
#the agents will appear as one dot as all agents are on top of each other  
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()

#get the agents home and store each of the moves    
for i in range (num_of_agents):
    while agents[i].arrived==False:
        agents[i].random_move()
        Stored_moves[agents[i]._y][agents[i]._x]+=1           
        if agents[i].environment[agents[i]._y][agents[i]._x]==agents[i].number: 
            agents[i].arrived=True
            #print finish to test is agents have made it home 
            print ("Finished")
 
#new axes for new plot
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])
               
#Plot to show all agents have made it home
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
   matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()

# writing the stored moves into the new_environment
f2= open ('new_enviroment_output.csv', 'w', newline= '')
writer = csv.writer (f2, delimiter = ',')
for row in Stored_moves:
    writer.writerow(row)
f2.close

#list
Stored_moves_output = []


# Read the new environment file which contains all the stored moves
f=open ("new_enviroment_output.csv")
reader=csv. reader (f, quoting = csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    Stored_moves_output.append(rowlist)
    

#new figure size
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])

#plot desnity map of stored moves to see where all the agents went 
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(Stored_moves_output)
matplotlib.pyplot.show()


    
#set up GUI using tkinter
#root = tkinter.Tk() #main window
#root.wm_title("Model")
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#
#tkinter.mainloop()

#matplotlib.pyplot.xlim=len(environment)
#matplotlib.pyplot.ylim=len(environment)
#matplotlib.pyplot.imshow(stored_moves_output)
#matplotlib.pyplot.show()
#
#fig = matplotlib,pyplot.figure(figsize=(7,7))
#ax = fig.add_axes([0,0,1,1])
#
#for row in reader:
#    rowlist = []
#    for item in row:
#        rowlist.append(item)
#    stored_moves_output.append(rowlist)
#
#f=open ("new_environement_output.csv)
#reader = csv.reader (f, quoting = csv.quote_nonnumeric)
#
#fig = matplotlib.pyplot.figure



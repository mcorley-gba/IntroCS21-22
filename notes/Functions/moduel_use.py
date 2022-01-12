#module_use.py
#Import the whole module:
#import modules as mods #General form:
                #import filename

#Import only one function (with nicknames):
#from modules import count_to_n as count
#from modules import make_pizza as pizza_time
#from filename import functionname
#from filename import func1, func2, func3...

#Import all the functions:
from modules import *

count_to_n(10)
#Since we specifically grabbed
#this function, we don't need
#the modules. prefix

#Now any function in modules.py
#is available for us to use.
make_pizza(12, "pepperoni", "cheese")
#preface the function with the
#module filename so that python
#knows where to get the function.
make_pizza(8, "cheese")

import modules #Allows this script to access the functions in the
                #modules.py script.
modules.make_pizza(1,'a') 

from modules import *           #Imports all functions/data 
#                               directly to this file

from modules import make_pizza  #Imports specified function

import modules as mods #same as "import modules", but
                        #now we prefix with "mods."
mods.make_pizza(3,'w')

from modules import make_pizza as mp

mp(5,'e')
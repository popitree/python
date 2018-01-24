# useful when importing only specific things
from turtle import forward, right, done

# * will import everything not starting with _
# but not a good practice
# from turtle import *
# another issue is if we have variable with name "done"
# it will give conflict with done() method in the imported module

import turtle

forward(150)
right(250)
forward(150)
turtle.circle(75)
done()

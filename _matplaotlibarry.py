# creating array using numpy
import numpy as np
import matplotlib.pyplot as pl


# basic way of creating arry
li=[1,2,3,4,5,6]
l2=[2,3,4,4,5,6]
a1=np.array(li)
a6=np.array(l2)

# print(a1)
# print(type(a1))

# using a range
a2=np.arange(2,9,2,float)
# print(a2)

# using linspace
a3=np.linspace(2,9,5)
# print(a3)

a4=np.cos(a3)
# print(a4)
a5=np.sin(a3)

# now plotting starts
# plot use for getting line graph output
# pl.plot(a3,a4)
# pl.xlabel("me")  #name of x axis
# pl.ylabel("you")   #name of y axis
# pl.show()

# chaing line style, colour width in line chart
# to change colour of line use colour code after plot
# pl.plot(a3,a4,"y")  #y=yello
# pl.plot(a3,a5,"r")   #for sec line in same graph
# pl.xlabel("me")  #name of x axis
# pl.ylabel("you")   #name of y axis
# pl.show()


# to change the linewridth
# pl.plot(a3,a4,"y",linewidth=2)
# pl.plot(a3,a5,"r", linewidth=5)
# pl.xlabel("me")
# pl.ylabel("you")
# pl.show()
#
# # to change style
# # linestyle or ls=[solid,dashed,dashdot,dotted]
#
# pl.plot(a3,a4,"y",linewidth=2,ls="dashdot")
# pl.plot(a3,a5,"r", linewidth=5, ls="dashed")
# pl.xlabel("me")
# pl.ylabel("you")
# pl.show()


# changing marker type,size,colour
# datapoins=marker
# this change sis also given in plot
# like , (marker=markertype,markersize=size,markeredgecolor=colour)
# see table on book page 264
#
# pl.plot(a3,a4,marker="p",markersize=5,markeredgecolor="g")
# pl.plot(a3,a5,marker="^",markersize=5,markeredgecolor="k")
# pl.xlabel("me")
# pl.ylabel("you")
# pl.show()



# bar graphs
# .bar() used

# pl.bar(a1,a6)
# pl.xlabel("this")
# pl.ylabel("that")

# for changing wridth to same for diif
# pl.bar(a1,a6,width=4.0)
# pl.bar(a1,a6,width=[1,2,2,1,1,1])
# pl.xlabel("this")
# pl.ylabel("that")
# pl.show()

# for changing colours
# pl.bar(a1,a6 ,color="red")
# pl.bar(a1,a6,color=["red","blue","yellow","green","red","blue"])
# pl.xlabel("this")
# pl.ylabel("that")
# pl.show()
#

# for creating multiple bar charts
# pl.bar(a1,a6 ,color="red",width=0.35)
# pl.bar(a1-0.4,a6,color="blue",width=0.35)
# pl.xlabel("this")
# pl.ylabel("that")
# pl.show()

# for horizontal bar use barh
# pl.barh(a1,a6 ,color="red")
# pl.barh(a1-0.4,a6,color="blue")
# pl.xlabel("this")
# pl.ylabel("that")
# pl.show()



# pie chart use .pie()
# here we give arry containg contry

# pl.pie(a1)
# pl.show()

# labeling contry
# give a list of lable along with it
# disease=["cholera","dengue","chikengunia","rabbis","goiter","aids"]
# pl.pie(a1,labels=disease)
# pl.show()

# adding formatted slices percent to pie
# disease=["cholera","dengue","chikengunia","rabbis","goiter","aids"]
# pl.pie(a1,labels=disease,autopct="%1.1f%%")
# pl.show()

# chainging color of pie
# give color list with it
# color=["red","blue","yellow","green","red","blue"]
# disease=["cholera","dengue","chikengunia","rabbis","goiter","aids"]
# pl.pie(a1,labels=disease,colors=color,autopct="%1.f%%")
# pl.show()

# explodind a slice
# give a explod list containg exploding distance

# exp=[0,0.5,0,00.4,0,0.3]   #here i exploding 2,4,6 slice
# color=["red","blue","yellow","green","red","blue"]
# disease=["cholera","dengue","chikengunia","rabbis","goiter","aids"]
# pl.pie(a1,labels=disease,colors=color,explode=exp,autopct="%1.f%%")
# pl.show()


# please see ouput of each parts


# customising the plotting
# adding title of graph using title()

# pl.plot(a3,a4,marker="p",markersize=5,markeredgecolor="g")
# pl.plot(a3,a5,marker="^",markersize=5,markeredgecolor="k")
# pl.xlabel("me")
# pl.ylabel("you")
#
pl.title("my line graph")
# pl.show()

# adding limits
# use .xlim( xmin,xmax)
# use .ylim( ymin,ymax)
# pl.xlim(-1,10)
# pl.ylim(-2,10)
# pl.plot(a3,a4,marker="p",markersize=5,markeredgecolor="g")
# pl.plot(a3,a5,marker="^",markersize=5,markeredgecolor="k")
# pl.xlabel("me")
# pl.ylabel("you")
#
# pl.title("my line graph")
# pl.show()

# if you use max as min and min as max (limits) ploting is changed
# addimg ticks
#  .xticks(lst)
# .yticks(lst)
# pl.plot(a3,a4,marker="p",markersize=5,markeredgecolor="g")
# pl.plot(a3,a5,marker="^",markersize=5,markeredgecolor="k")
# pl.xlabel("me")
# pl.ylabel("you")
# pl.xticks([1,2,3,4,5,6])
# pl.yticks([1,2,3,4,5,6])
#
# pl.title("my line graph")
# pl.show()

# adding a legends
# step1 give lebel in plot
#step2use .legend(pos) to lock it 1=upright 2=uplef 3=lowrig 4=lowlef
# pl.xlim(-1,10)
# pl.ylim(-2,10)
# pl.plot(a3,a4,marker="p",markersize=5,markeredgecolor="g",label="range2")
# pl.plot(a3,a5,marker="^",markersize=5,markeredgecolor="k" ,label="range1")
# pl.xticks([1,2,3,4,5,6])
# pl.legend(loc=1)  #see output
# pl.title("my line graph")
#
# pl.xlabel("me")
# pl.ylabel("you")
#
# pl.title("my line graph")
# pl.show()


# saving a figure
# .savefig(filename and path)

# pl.savefig("myplot.pdf")





col=[8000,12000,9800,11200,15500,7300]
x=["mon","tue","wed",'thurs',"fri","sat"]
pl.bar(x,col,width =.21,color="r")
# pl.yticks([1,2,3,4,5,6])
pl.show()

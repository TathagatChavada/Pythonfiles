# 1 Graph
from matplotlib import pyplot as plt

plt.plot([1,2,3,1,1],[4,5,1,1,4],linewidth = 5, color = "r")

plt.show()


# 2 Graph
X = [5,8,10]
Y = [12,16,6]

A = [6,9,11]
B = [6,15,7]

plt.plot(X,Y, linewidth = 5,label ="First ", color = "g")
plt.plot(A,B, linewidth = 5,label ="Second ", color = "purple")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.legend()

plt.show()


# 3 Bar Graph
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="PC Gamers")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Mobile Gamers", color="g")
plt.legend()
plt.xlabel("Months")
plt.ylabel("No. of gamers")
plt.title("Graph of gamers")

plt.show()

# 4 Stack Plot
Days = [1,2,3,4,5]

Sleeping = [7,8,6,11,17]
Eating = [2,3,4,3,2]
Working = [7,8,7,2,2]
Playing = [8,5,7,8,13]

plt.plot([],color="m", label="Sleeping",linewidth=5)
plt.plot([],color="c", label="Eating",linewidth=5)
plt.plot([], color="r", label="Working",linewidth=5)
plt.plot([],color="k", label="Playing",linewidth=5)

plt.stackplot(Days, Sleeping, Eating, Working, Playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Plot')
plt.legend()

plt.show()

#5 Pie Chart
Slices = [85,87,91,84,81]
Subjects = ["English","Sanskrit","Maths","Science", "Social Science"]
Colours = ["c","y","c","r","g"]

plt.pie(Slices,
        labels= Subjects,
        colors= Colours,
        startangle= 90,
        shadow= True,
        explode= (0,0,0.1,0,0),
        autopct= '%1.1f%%',
        )
plt.title('Pie Plot')

plt.show()


plt.plot([-1,-2],[-3,-6])

plt.show()














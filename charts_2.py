import matplotlib.pyplot as plt
import numpy as np

# linear_plot
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

plt.plot(x, y, color="Red", linestyle="dashed", marker="*")
plt.title("Numbers multiple 2")
plt.xlabel("Numbersa")
plt.ylabel("2x Multiples")
plt.grid(True)
plt.show()


# bar-plot
city = ["Tehran", "Gorgan", "Shiraz", "Bandar Abbas"]
accisent = [21000, 6000, 19000, 9000]

city = np.array(city)
accisent = np.array(accisent)

sorted_index = np.argsort(accisent)

plt.bar(city[sorted_index], accisent[sorted_index], width=0.4, color="skyblue")
plt.title("Accident in each city")
plt.xlabel("City")
plt.ylabel("Accident")
plt.show()


# pie-chart
product = ["Tablet", "Laptop", "Phone", "Smart Watch"]
cost = [15, 55, 20, 10]

explode = [0.1, 0, 0, 0]

plt.pie(cost, labels=product, autopct="%1.1f%%", explode=explode)
plt.title("Bugget")
plt.show()


# scatter-plot
weight = [46, 73, 89, 90, 120, 65]
height = [159, 170, 182, 184, 178, 173]

plt.scatter(weight, height, s=200, alpha=0.5, color="red", edgecolors="black")
plt.title("Body situation")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.show()

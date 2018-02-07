x = np.arange(0.0, 1.0, 0.5)
y1 = 0.2-x
y2= x-1 
x3=0.1
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x3)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plotting Equation y=x*x+2')
plt.grid(True)
plt.show()
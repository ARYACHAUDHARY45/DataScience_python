#  Create a plot comparing Kohli, Rohit Sharma, and Sehwag across 10 years of hypothetical runs.
#   Use:
# Labels
# Legends
# Colors
# Line styles
# One custom style 
import matplotlib.pyplot as plt
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
Rohit =[100,300,150,264,760,100,1500,2000,1900,2100]
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
plt.plot(years,Rohit,'bs-',label="Rohit Sharma")
plt.plot(years,kohli,'r*:',label="Virat Kohli")
plt.plot(years,sehwag,'kv--',label="Virendra Sehwag")
plt.grid(True)
plt.style.use('seaborn-v0_8-dark')
plt.legend()
plt.show()



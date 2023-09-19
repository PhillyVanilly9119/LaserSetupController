import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seabreeze # import order matters
seabreeze.use('pyseabreeze') 
from seabreeze.spectrometers import Spectrometer,list_devices

# TODO: Add display window for prints from backend

# Add error handling here
a = list_devices()
print(a)
spec = Spectrometer(a[0])
print(spec)

# up until here it is setup

wavelengths = spec.wavelengths()

intTime = int(input("integration time in microsec:")) # add from text box as signal
spec.integration_time_micros(intTime)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)



#initialize

def animate(i):
	intensities = spec.intensities()
	ax1.clear()
	ax1.plot(wavelengths,intensities)

ani = animation.FuncAnimation(fig , animate , interval = intTime/1000) # ms/µs conversion is important
plt.show()

#live plot


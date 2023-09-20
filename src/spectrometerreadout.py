

# import order matters
import seabreeze 
seabreeze.use('pyseabreeze') 
from seabreeze.spectrometers import Spectrometer, list_devices

# TODO: Add display window for prints from backend
# TODO: think of including a log file class

class SpectrometerReadOuts():
    
    def __init__(self) -> None:
          self.setup_spectrometer()
          self.update_integration_time()
      
    def setup_spectrometer(self):
        device_list = list_devices() # a = list_devices()
        if device_list is None:
            print("[ERROR:] Did not find a device (Specrometer)")
        if len(device_list) > 1:
            print("[INFO:] Found more than one connected device")
        self.handle_spectrometer = Spectrometer(device_list[0]) # spec = Spectrometer(a[0])
        
    def update_integration_time(self, int_time: int=100) -> None:
        # Think of useful assertions
        self.handle_spectrometer.integration_time_micros(int_time) # spec.integration_time_micros(intTime)
        print(f"[INFO:] Integration time for spectrometer set to {int_time} ms") # TODO: make this a debug message
        
    def read_out_spectrometer_data(self):
        wavelengths = self.handle_spectrometer.wavelengths() # wavelengths = spec.wavelengths()
        intensities = self.handle_spectrometer.intensities() # intensities = spec.intensities()
        return wavelengths, intensities
        

#### ---- ####s
# wavelengths = spec.wavelengths()

# intTime = int(input("integration time in microsec:")) # add from text box as signal
# spec.integration_time_micros(intTime)

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# #initialize

# def animate(i):
# 	intensities = spec.intensities()
# 	ax1.clear()
# 	ax1.plot(wavelengths,intensities)

# ani = animation.FuncAnimation(fig , animate , interval = intTime/1000) # ms/µs conversion is important
# plt.show()

#live plot

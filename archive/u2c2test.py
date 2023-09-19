from smbus2 import SMBus, i2c_msg
from math   import floor


def outVoltToBin(Volt):
	#map 0-5V to 12 bit binary
	maxOutVolt = 5
	if Volt <= maxOutVolt and Volt>=0:
		Bin = floor(Volt*0xFFF/maxOutVolt) 
		#print(Bin)
		return Bin
	
def inBinToVolt(num):
	#map 12bit binary to 0-5V
	maxInVolt = 5
	voltIn = num*maxInVolt/0xFFF
	return voltIn

device_adress = 0x10       #use 'i2cdetect -y 1' in the cmd to find the i2c device
reg_pwr_dwn   = 0b00001011 #power down/ref control register
reg_set_dac   = 0b00000101 #DAC pin config register
reg_set_adc   = 0b00000100 #ADC pin config register
reg_gp_ctrl	  = 0b00000011 #DAC & ADC control registers
reg_cnf_adc   = 0b00000010 #ADC sequence config register

reg_wrt_dac   = 0b00010000 #DAC pin  0  output register
#reg_red_adc  = 		   #ADC pins 1-4 input register

#set the Vref to internal
with SMBus(1) as bus:
	#16 bits message: set the Vref to internal ref = 2.5V
    msg_msb =0b00000010
    msg_lsb =0b00000000
    # build the message
    msg = i2c_msg.write(device_adress, [reg_pwr_dwn, msg_msb, msg_lsb])
    # write into the bus
    bus.i2c_rdwr(msg)

#set I/O 0 as DAC output
with SMBus(1) as bus:
	#16 bits message:set I/O 0 as DAC output
    msg_msb =0b00000000
    msg_lsb =0b00000001
    # build the message
    msg = i2c_msg.write(device_adress, [reg_set_dac, msg_msb, msg_lsb])
    # write into the bus
    bus.i2c_rdwr(msg)
	
	
#set I/O 1,2,3,4 as ADC input
with SMBus(1) as bus:
	#16 bits message:set I/0 1 to 4 as ADC input
	msg_msb =0b00000000
	msg_lsb =0b00011110
	#build the message
	msg = i2c_msg.write(device_adress, [reg_set_adc, msg_msb, msg_lsb])
	#write into the bus
	bus.i2c_rdwr(msg)
	
#set I/0 DAC and ADC configuration
with SMBus(1) as bus:
	#16 bits message: set the range of ADC and DAC to 2xVref = 5V
    msg_msb =0b00000000
    msg_lsb =0b00110000
    #build the message
    msg = i2c_msg.write(device_adress, [reg_gp_ctrl, msg_msb, msg_lsb])
    #write into the bus
    bus.i2c_rdwr(msg)
    
with SMBus(1) as bus:
	#write in the ADC sequence register to include i/os 1 to 4
	msg_msb =0b00000000 #set the temp and rep bits to 0
	msg_lsb =0b00011110 #add the channels 1 to 4 to the ADC conversion
	#build the message
	msg = i2c_msg.write(device_adress,[reg_cnf_adc,msg_msb,msg_lsb])
	#write into the bus
	bus.i2c_rdwr(msg)

#let's try to output some stuff


voltOut = float(input('voltage output:'))
voltOut = outVoltToBin(voltOut)    

out4firstDigits = voltOut>>8
#print(bin(out4firstDigits))
mask_last_8dgt  = 0b000011111111
out8lastDigits  = voltOut & mask_last_8dgt

#set I/0 DAC and ADC configuration
with SMBus(1) as bus:
     #16 bits message: set the voltage output of pin I/O 0 DAC to voltOut volts	
	msg_msb 		= 0b10000000 + out4firstDigits
	#print(bin(msg_msb))
	msg_lsb			= out8lastDigits
	#print(bin(msg_lsb))
	#build the message
	msg = i2c_msg.write(device_adress, [reg_wrt_dac, msg_msb, msg_lsb])
	#write into the bus
	bus.i2c_rdwr(msg)

#writing works!

#let's try reading the ADCs

with SMBus(1) as bus:
	a = bus.read_i2c_block_data(device_adress,0b01000000,2*4)	
	for i in a:	
		print(bin(i))

#reading works!
#let's parse in decimal
mask_last_4digits = 0b00001111
most_significant_bytes 	= []
least_significant_bytes = []
num_12_bits 			= []

for k in range(0,len(a)):
	if k%2:	#odd numbered elements
		least_significant_bytes.append(a[k])
		print(bin(a[k]))
	else :	#even numbered elements, starting with 0
		b = (a[k] & mask_last_4digits)<<8
		most_significant_bytes.append(b)
		print(bin(b))

for l in range(0,len(most_significant_bytes)):
	num_12_bits.append(most_significant_bytes[l]+least_significant_bytes[l])

print(num_12_bits)

for l in num_12_bits:
	print(inBinToVolt(l))

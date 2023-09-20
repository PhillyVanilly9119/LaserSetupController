from smbus2 import SMBus, i2c_msg


def volt_out_2bin(voltage: float):
    """Map 0-5V to 12-bit binary for GPIO pin on Raspberry Pi 4.
    
    Args:
        voltage (float): Desired voltage to be mapped to 12-bit output.

    Raises:
        ValueError: If voltage is outside the valid range [0, 5].

    Returns:
        int: 12-bit binary representation of the voltage.
    """
    max_out_voltage = 5
    if 0 <= voltage <= max_out_voltage:
        return int(voltage * 0xFFF / max_out_voltage)
    else:
        raise ValueError(f"Input voltage {voltage} is outside the valid range [0, {max_out_voltage}].")

 
def bin_in_2volt(num):
    """Map 12-bit binary to voltage in the range of 0-5V.

    Args:
        num (int): 12-bit binary value.

    Raises:
        ValueError: If the binary value is outside the valid range [0, 0xFFF].

    Returns:
        float: Voltage in the range of 0-5V.
    """
    maxInVolt = 5
    if 0 <= num <= 0xFFF:
        voltIn = num * maxInVolt / 0xFFF
        return voltIn
    else:
        raise ValueError(f"Input binary value {num} is outside the valid range [0, 0xFFF].")


class SMBusWrapper():
    
    def __init__(self) -> None:
          self._setup()
    
    
    def _setup(self) -> None:
        """Initialize the configuration of an I2C device for DAC and ADC control.

        This method sets up the I2C communication with a specific device, configuring
        various registers for controlling Digital-to-Analog Conversion (DAC) and Analog-to-Digital
        Conversion (ADC) operations. It defines ENUMs for pin instructions as class variables,
        initializes device parameters, and communicates with the I2C device to configure its settings.

        Args:
            None

        Returns:
            None
        """
        # define ENUMs for pin instructions as class variables
        self.device_adress = 0x10   # use 'i2cdetect -y 1' in the cmd to find the i2c device
        self.reg_pwr_dwn   = 0b00001011  # power down/ref control register
        self.reg_set_dac   = 0b00000101  # DAC pin config register
        self.reg_set_adc   = 0b00000100  # ADC pin config register
        self.reg_gp_ctrl   = 0b00000011  # DAC & ADC control registers
        self.reg_cnf_adc   = 0b00000010  # ADC sequence config register
        self.reg_wrt_dac   = 0b00010000  # DAC pin  0  output register
        #reg_red_adc  = 		    # ADC pins 1-4 input register

        # i) set the Vref to internal -> # 16 bits message: set the Vref to internal ref = 2.5V
        with SMBus(1) as bus:
            msg_msb =0b00000010
            msg_lsb =0b00000000
            msg = i2c_msg.write(self.device_adress, [self.reg_pwr_dwn, msg_msb, msg_lsb]) # create message
            bus.i2c_rdwr(msg) # write into the bus

        # ii) set I/O pin 0 as DAC output -> # 16 bits message: set I/O 0 as DAC output
        with SMBus(1) as bus:
            msg_msb =0b00000000
            msg_lsb =0b00000001
            msg = i2c_msg.write(self.device_adress, [self.reg_set_dac, msg_msb, msg_lsb])
            bus.i2c_rdwr(msg)
	
        # iii) set I/O 1,2,3,4 as ADC input -> # 16 bits message:set I/0 1 to 4 as ADC input
        with SMBus(1) as bus:
            msg_msb =0b00000000
            msg_lsb =0b00011110
            msg = i2c_msg.write(self.device_adress, [self.reg_set_adc, msg_msb, msg_lsb])
            bus.i2c_rdwr(msg)
	
        #set I/0 DAC and ADC configuration -> # 16 bits message: set the range of ADC and DAC to 2 x Vref = 5V
        with SMBus(1) as bus:
            msg_msb =0b00000000
            msg_lsb =0b00110000
            msg = i2c_msg.write(self.device_adress, [self.reg_gp_ctrl, msg_msb, msg_lsb])
            bus.i2c_rdwr(msg)
    
        # write in the ADC sequence register to include i/os 1 to 4
        with SMBus(1) as bus:
            msg_msb = 0b00000000 #set the temp and rep bits to 0
            msg_lsb = 0b00011110 #add the channels 1 to 4 to the ADC conversion
            msg = i2c_msg.write(self.device_adress, [self.reg_cnf_adc, msg_msb, msg_lsb])
            bus.i2c_rdwr(msg)


    def write_voltage_2adcs(self, voltage: float) -> None:
        voltage_b = volt_out_2bin(voltage)    
        out_first_4digits = voltage_b >> 8
        mask_last_8digits = 0b000011111111
        out_last_8digits  = voltage_b & mask_last_8digits

        # set I/0 DAC and ADC configuration
        with SMBus(1) as bus:
            msg_msb = 0b10000000 + out_first_4digits # 16 bits message to set the voltage output of I/O pin 0 DAC to voltage_b
            msg_lsb	= out_last_8digits
            msg = i2c_msg.write(self.device_adress, [self.reg_wrt_dac, msg_msb, msg_lsb])
            bus.i2c_rdwr(msg)


    def read_voltage_from_adcs(self, print_readout: bool=False) -> list:
        with SMBus(1) as bus:
            data_readout = []
            readout = bus.read_i2c_block_data(self.device_adress, 0b01000000, 2*4)	
            for i in readout:	
                data_readout.append(bin(i))
                if print_readout:
                    print(bin(i))
        return data_readout
    

#### -> WHAT THE FUCK DO YOU WANT HERE????

#let's parse in decimal
mask_last_4digits = 0b00001111
most_significant_bytes 	= []
least_significant_bytes = []
num_12_bits 			= []

# a = data_readout

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
	print(bin_in_2volt(l))

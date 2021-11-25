import smbus, time
device_add =  0x23
poweroff = 0x00
poweron = 0x01
reset = 0x07

high_res_mode = 0x20
ibus = smbus.SMBus(1)

def read_light_value():
    val = ibus.read_i2c_block_data(device_add, high_res_mode)
    return Convert(val)

def Convert(data):
    return ((data[1] + (256*data[0]))/1.2)

while True:
     print(" Light Intensity: "+ str(read_light_value())+ " Lux")
     time.sleep(1)

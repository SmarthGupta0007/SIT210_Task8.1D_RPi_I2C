import smbus, time
device_add =  0x23
poweroff = 0x00
poweron = 0x01
reset = 0x07

high_res_mode = 0x20
ibus = smbus.SMBus(1)

def light_value():
    val = ibus.i2c_block_data(device_add, high_res_mode)
    return Convert(val)

def Convert(data):
    return ((data[1] + (256*data[0]))/1.2)

while True:
     value = light_value();     
     print(" Light Intensity: "+ str(light_value())+ " Lux")
     time.sleep(1)
     if (value > 200):
         print("Too Bright")
     elif (value > 150 and value < 200):
         print("Bright")
     elif (value > 100 and value < 150):
         print("Medium")
     elif (value > 50 and value < 100):
         print("Dark")
     elif (value < 50):
         print("Too Dark")

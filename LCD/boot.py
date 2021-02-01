from pico_i2c_lcd import I2cLcd
from machine import I2C
from machine import Pin
import utime as time

# i2c = I2C(scl=Pin(22),sda=Pin(21),freq=100000)
# lcd = I2cLcd(i2c, 0x27, 2, 16)
# lcd.clear()
# lcd.putstr('Uncle Engineer\nMicroPython')

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16) # LCD 16x2

#lcd.putchar(chr(247))

korkai = bytearray([0x0E,0x11,0x09,0x11,0x11,0x11,0x11,0x11])
khorkhai = bytearray([0x1A,0x1A,0x0A,0x0A,0x0A,0x0A,0x0A,0x0E])

loo = bytearray([ 0x1E,
  0x12,
  0x02,
  0x1E,
  0x12,
  0x10,
  0x02,
  0x02])

ngorngoo = bytearray([ 0x00,
  0x03,
  0x03,
  0x01,
  0x09,
  0x05,
  0x03,
  0x01])

angry = bytearray([ 0x00,
  0x11,
  0x0A,
  0x00,
  0x00,
  0x0E,
  0x11,
  0x11])


#lcd.custom_char(0, korkai)
#lcd.putchar(chr(0))

#lcd.custom_char(1, khorkhai)
#lcd.putchar(chr(1))

lcd.putstr('Hello ')

lcd.custom_char(0, loo)
lcd.putchar(chr(0))
lcd.custom_char(1, ngorngoo)
lcd.putchar(chr(1))
  

'''
# set char to location
lcd.putchar('U')
lcd.move_to(2,0)
lcd.putchar('N')
lcd.move_to(4,0)
lcd.putchar('C')
lcd.move_to(6,0)
lcd.putchar('L')
lcd.move_to(8,0)
lcd.putchar('E')
lcd.move_to(10,0)

lcd.move_to(4,1)
lcd.putchar('E')
lcd.move_to(6,1)
lcd.putchar('N')
lcd.move_to(8,1)
lcd.putchar('G')
lcd.move_to(10,1)
lcd.putchar('I')
lcd.move_to(12,1)
lcd.putchar('N')
'''

'''
# blinking with number
for i in range(10):
    lcd.putstr('No. {}'.format(i+1))
    lcd.backlight_on()
    time.sleep(0.5)
    lcd.backlight_off()
    lcd.clear()
    time.sleep(0.5)
    
lcd.backlight_on()
'''

#lcd.backlight_on()
#time.sleep(3)
#lcd.backlight_off()
#time.sleep(3)
#lcd.backlight_on()



#lcd.putstr('Uncle Engineer')
#time.sleep(3)
#lcd.display_off()
#lcd.move_to(3,1)
#lcd.putstr('RPi PICO')
#time.sleep(3)
#lcd.display_on()



#lcd.blink_cursor_on()
#time.sleep(5)
#lcd.blink_cursor_off()


#lcd.show_cursor()
#time.sleep(2)
#lcd.hide_cursor()


#lcd.putstr('Uncle Engineer')
#lcd.move_to(3,1) # First Character and Line 2
#lcd.putstr('RPi Pico')

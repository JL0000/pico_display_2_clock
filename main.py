import machine
import utime
import gc
import picodisplay2 as display 

# Initialise display with a bytearray display buffer
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(0.5)

#initialize the time 
rtc = machine.RTC()
rtc.datetime((2022, 12, 12, 4, 0, 6, 50, 0))

def main():
    while True:
        if display.is_pressed(display.BUTTON_A):         
            clear()                                          
            display.set_pen(255, 255, 255)                
            therm()                        
        elif display.is_pressed(display.BUTTON_B):
            clear()
            display.set_pen(0, 255, 255)
            display.text("You're an asshole", 10, 10, 240, 4)
            display.update()
            utime.sleep(1)
            clear()
        elif display.is_pressed(display.BUTTON_X):
            clear()
            display.set_pen(255, 0, 255)
            display.text("Button does nothing", 10, 10, 240, 4)
            display.update()
            utime.sleep(1)
            clear()
        elif display.is_pressed(display.BUTTON_Y):
            clear()
            display.set_pen(255, 255, 0)
            display.text("No much to do in Pico", 10, 10, 240, 4)
            display.update()
            utime.sleep(1)
            clear()
        else:
            year, month, day, weekday, hour, minute, second, microsecond = rtc.datetime()
            if second == 0 and microsecond < 1:
                clear()
            time(hour, minute)
        utime.sleep(0.1) 
    


def clear():
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()
    
def therm():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    display.text("{:.2f}".format(temperature) + "c", 30, 80, 0,  10)
    display.update()
    utime.sleep(5)
    clear()

def time(hour, min):
    display.set_pen(124, 252, 0)
    if hour < 10:
        new_hour = str(0) + str(hour)
    if min < 10:
        new_min = str(0) + str(min)
    display.text(str(new_hour) + ":" + str(new_min), 40, 80, 200, 10)
    display.update()

    
if __name__ == "__main__":
    main()


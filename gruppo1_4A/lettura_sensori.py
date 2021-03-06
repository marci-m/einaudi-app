import serial

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    while True:
        if ser.in_waiting > 0:

            temperature = ser.readline().decode('utf-8').rstrip()
            file = open("/var/www/html/temperature.txt", "w")
            file.write(temperature)
            file.close()
            
            print("temperatura letta: "+ str(temperature))


from gpiozero import PWMLED
from scd30_i2c import SCD30
from time import sleep

# Opret LED'er
red = PWMLED(17)
green = PWMLED(27)

# Opret sensor
sensor = SCD30()
sensor.start_periodic_measurement()

# DEFINÉR FUNKTIONEN FØRST
def set_color(red_val, green_val):
    red.value = red_val
    green.value = green_val
    print(f"LED -> Rød: {green_val}, Grøn: {red_val}")

# SÅ brug funktionen i while-loop
while True:
    if sensor.get_data_ready():
        co2, temp, rh = sensor.read_measurement()
        print(f"CO2: {co2:.1f} ppm")

        if co2 < 1000:
            print("Grøn zone")
            set_color(1, 0)
        elif 1000 <= co2 <= 1499:
            print("Gul zone")
            set_color(0.5, 0.8)
        else:
            print("Rød zone")
            set_color(0, 1)

    sleep(1)

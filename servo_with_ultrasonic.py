from machine import Pin, PWM, ADC, time_pulse_us
import time

led = Pin("LED", Pin.OUT) # Test the PICO LED
pwm = PWM(Pin(0))
trig_pin = Pin(16, Pin.OUT) 
echo_pin = Pin(15, Pin.IN) 

pwm.freq(50) # Set the PWM frequency 


SOUND_SPEED=340 # Speed ​​of sound in air
TRIG_PULSE_DURATION_US=10


while True:
    # Prepare the signal
    trig_pin.value(0)
    time.sleep_us(5)
    # Create a 10 µs pulse
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # Returns the wave propagation time (in µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000 # Convert to cm (1 cm = 2 * 10^-6 s)
    print(f"Distance : {distance_cm} cm")
    # If the distance is between 5 and 35 cm, the servo will turn to 90 degrees
    if distance_cm > 5 and distance_cm < 35:
        led.high()
        print("Obstacle detected!")
        pwm.duty_u16(6000)
    else:
        pwm.duty_u16(2700)
        led.low()
        print("LED Off")
    time.sleep_ms(500)

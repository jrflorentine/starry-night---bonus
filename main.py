def Advanced2():
    while True:
        led.toggle(randint(0, 4), randint(0, 4))
        for index in range(11):
            led.set_brightness(25.5 * index)
            basic.pause(100)
        for index2 in range(11):
            led.set_brightness(255 - 25.5 * index2)
            basic.pause(100)
        basic.pause(randint(0, 2000))
        basic.clear_screen()
def Basic():
    basic.show_leds("""
        # . # . #
                . # # # .
                # # # # #
                . # # # .
                # . # . #
    """)

def on_button_pressed_a():
    Advanced2()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Advanced1():
    led.set_brightness(0)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    while True:
        for index3 in range(11):
            led.set_brightness(25.5 * index3)
            basic.pause(100)
        for index4 in range(11):
            led.set_brightness(255 - 25.5 * index4)
            basic.pause(100)
        basic.pause(randint(0, 2000))
def Moderate1():
    while True:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . #
                        . # # # .
                        . # # # .
                        . # # # .
                        # . . . #
        """)
        basic.show_leds("""
            # . # . #
                        . # # # .
                        # # # # #
                        . # # # .
                        # . # . #
        """)
        basic.show_leds("""
            # . . . #
                        . # # # .
                        . # # # .
                        . # # # .
                        # . . . #
        """)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)

def on_forever():
    if input.light_level() < 1:
        pass
basic.forever(on_forever)

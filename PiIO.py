"""
Methods to work specifcally with the custom made board that attaches atop the
RPi to provide 4 Spike Relays outputs and 6 input switches.  

Example usage  (GPIO requires you run code with 'sudo python'):
    import PiIO

    try:
        winch = PiIO.Spike(1)
        upperLimit = PiIO.Switch(1)
        lowerLimit = PiIO.Switch(2)
        
        # Run winch to upper limit
        while upperLimit.Open():
            winch.fwd()
        winch.stop()
        
        # Run winch to lower limit
        while lowerLimit.Open():
            winch.rev()
        winch.stop()
        
    except:
        raise

    finally:
    # Release IO lines
    PiIO.close()

"""

import RPi.GPIO as IO

# INITIALIZE HARDWARE
 
# Setup GPIO to map to physical board pin numbers (Model B V2)
IO.setmode(IO.BOARD)

    
# Setup input pins for Switches
SWITCHES=[12,16,18,22,24,26]
for pin in SWITCHES:
    # Inputs will be held high (1) unless shorted to ground (0)
    IO.setup(pin,IO.IN,pull_up_down=IO.PUD_UP)


def close():
    IO.cleanup()



# CLASSES

# There are 4 spike relays, each capable of forward, reverse and off states.
#
class Spike():

    # Init a Spike relay.  Pass number 1 to 4.
    # Reverse relay control, reverses polarity of motor output.
    def __init__(self,fwd,rev):
            self.pinFwd = fwd
            self.pinRev = rev

    
        
    def stop(self):
        self.left(False)
        self.right(False)
           
    def left(self,state):
        IO.output(self.pinFwd,state)
        
    def right(self,state):
        IO.output(self.pinRev,state)

    def forward(self):
        self.left(True)
        self.right(False)

    def reverse(self):
        self.left(False)
        self.right(True)

    def on(self):
        self.left(True)
        self.right(True)



# Switch class provides open/closed state for switch inputs.
# Pass switch number to  either the 'open' or 'closed' method to get logical state.
#
class Switch():

    # Init a switch for input.  Pass #1 to 6.
    def __init__(self,switch):
        if switch >= 1 and switch <= 6:
            self.pin = SWITCHES[switch-1]
        else:
            raise ValueError("Switch number must be between 1 and 6")

    def open(self):
        if IO.input(self.pin) == 1:
            return True
        else:
            return False

    def closed(self):
        if IO.input(self.pin) == 0:
            return True
        else:
            return False

    

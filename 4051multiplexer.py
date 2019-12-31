import random

def inputs(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                output = 'A0'
            elif c == 1:
                output = 'A1'
        elif b == 1:
            if c == 0:
                output = 'A2'
            elif c == 1:
                output = 'A3'
    elif a == 1:
        if b == 0:
            if c == 0:
                output = 'A4'
            elif c == 1:
                output = 'A5'
        elif b == 1:
            if c == 0:
                output = 'A6'
            elif c == 1:
                output = 'A7'        
    return output

lasta = 0
lastb = 0
lastc = 0

while(1):
    #step thru 1-8 / 0-7:
    print(lasta,lastb,lastc)
    print(inputs(lasta,lastb,lastc))
    
    if lasta == 1 and lastb == 1 and lastc == 1:
        lasta = 0
        lastb = 0
        lastc = 0
    elif lastb == 1 and lastc == 1:
        lasta = 1
        lastb = 0
        lastc = 0
    elif lastc == 1:
        lastb = 1
        lastc = 0
    
    elif lastc == 0:
        lastc = 1
'''
random mode:
randomizing all three inputs to a multiplexer seems to get interesting patterns, that's doable with 3 inverters from a 40106 chip
randomsteps = [random.randrange(0,2),random.randrange(0,2),random.randrange(0,2)]
print(randomsteps[0],randomsteps[1],randomsteps[2])
print(inputs(randomsteps[0],randomsteps[1],randomsteps[2]))
'''

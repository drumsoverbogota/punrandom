import time
import random
import pygame.midi

pygame.midi.init()
player= pygame.midi.Output(0)
player.set_instrument(114,1)

C4  = 60
CS4 = 61
D4  = 62
DS4 = 63
E4  = 64
F4  = 65
FS4 = 66
G4  = 67
GS4 = 68
A4  = 69
AS4 = 70
B4  = 71

states = ['r','b','n','c','s','sr','sb','sn','sc','ss']

equi_matrix = {'r': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'b': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'n': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'c': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               's': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'sr': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'sb': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'sn': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'sc': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1},
               'ss': {'r':0.1,'b':0.1,'n':0.1,'c':0.1,'s':0.1,'sr':0.1,'sb':0.1,'sn':0.1,'sc':0.1,'ss':0.1}}

cust_matrix = {'r': {'r':0.3,'b':0.5,'n':0,'c':0,'s':0,'sr':0.2,'sb':0,'sn':0,'sc':0,'ss':0},
               'b': {'r':0,'b':0.3,'n':0.5,'c':0,'s':0,'sr':0,'sb':0.2,'sn':0,'sc':0,'ss':0},
               'n': {'r':0,'b':0,'n':0.3,'c':0.5,'s':0,'sr':0,'sb':0,'sn':0.2,'sc':0,'ss':0},
               'c': {'r':0,'b':0,'n':0,'c':0.5,'s':0.3,'sr':0.2,'sb':0,'sn':0,'sc':0,'ss':0},
               's': {'r':0,'b':0,'n':0,'c':0.5,'s':0.3,'sr':0.2,'sb':0,'sn':0,'sc':0,'ss':0},
               'sr': {'r':0.5,'b':0,'n':0,'c':0,'s':0,'sr':0.3,'sb':0.2,'sn':0,'sc':0,'ss':0},
               'sb': {'r':0,'b':0.5,'n':0,'c':0,'s':0,'sr':0,'sb':0.3,'sn':0.2,'sc':0,'ss':0},
               'sn': {'r':0,'b':0,'n':0.5,'c':0,'s':0,'sr':0,'sb':0,'sn':0.3,'sc':0.2,'ss':0},
               'sc': {'r':0,'b':0,'n':0,'c':0.5,'s':0,'sr':0,'sb':0,'sn':0,'sc':0.3,'ss':0.2},
               'ss': {'r':0.5,'b':0,'n':0,'c':0,'s':0,'sr':0,'sb':0,'sn':0,'sc':0.3,'ss':0.2}}


equiss_matrix = {'r': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'b': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'n': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'c': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               's': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'sr': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'sb': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'sn': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'sc': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0},
               'ss': {'r':0.2,'b':0.2,'n':0.2,'c':0.2,'s':0.2,'sr':0,'sb':0,'sn':0,'sc':0,'ss':0}}

def run(bpm,mat,ins):
    player.set_instrument(ins,1)    
    matrix = []
    if(mat == '1'):
        matrix = cust_matrix
    if(mat == '2'):
        matrix = equiss_matrix        
    else:
        matrix = equi_matrix        
    m_set = init()
    current_state = random.choice(states)
    current_note = 0
    while (current_note < len(m_set)):
        print (current_state),
        print current_note
        if(states.index(current_state) <= 4):
            play_note(m_set[current_note],current_state,bpm)
        else:
            play_note(-1,current_state,bpm)
        rand = random.random()
        suma = 0
        for i in range(0,len(states)):
            suma += matrix[current_state][states[i]]
            if(rand < suma):
                current_state = states[i]         
                break
        if(states.index(current_state) <= 4):
            current_note+=1


def init():

    base = range(0,12)
    melody = []
    random.shuffle(base)
    melody.extend(base)    
    melody.extend(inv(base))
    melody.extend(ret(base))
    melody.extend(inv(ret(base)))

    return melody

def play(note,tim):
    player.note_on(note, 127,1)
    time.sleep(tim)
    player.note_off(note,127,1)

def play_note(note,value,tempo):
    time = 0
    if (value == 'r') or (value == 'sr'):
        time = (4 * 60) /tempo
    elif (value == 'b') or (value == 'sb'):
        time = (2 * 60) /tempo        
    elif (value == 'n') or (value == 'sn'):
        time = (1 * 60) /tempo        
    elif (value == 'c') or (value == 'sc'):
        time = (0.5 * 60) /tempo        
    elif (value == 's') or (value == 'ss'):
        time = (0.5 * 60) /tempo
    if(note != -1):
        play(note+60,time)
    else:
        play(note,time)

def play_set(array):
    midi = set_to_midi(array)
    print midi
    play_array(midi)
    
def play_array(array):
    for note in array:
        play(note,0.5)
        
def set_to_midi(array):
    return [60 + note for note in array]    

def inv(array):
    return [(12 - note) % 12 for note in array]

def ret(array):
    retu = array[:]
    return retu[::-1]



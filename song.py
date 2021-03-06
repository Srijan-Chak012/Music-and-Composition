import numpy as np
from scipy.io import wavfile
import requirements

right_hand_notes = ['D5', 'C#5', 'B4', 'A4', 'G4', 'F#4', 'G4', 'E4',
                   'D4', 'F#4', 'A4', 'G4',  'F#4', 'D4', 'F#4', 'E4',
                   'D4', 'B3', 'D4', 'A4',  'G4', 'B4', 'A4', 'G4',
                   'F#4', 'D4', 'E4', 'C#5',  'D5', 'F#5', 'A5', 'A4',
                   'B4', 'G4', 'A4', 'F#4',  'D4', 'D5', 'D5', 'C#4',
                   'A5', 'F#5', 'G5', 'A5',  'F#5', 'G5', 'A5', 'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G5',
                   'F#5', 'D5', 'E5', 'F#5',  'F#4', 'G4', 'A4', 'B4', 'A4','G4', 'F#4', 'E4', 'D4', 'E4',
                   'G4', 'B4', 'A4', 'G4',  'F#4', 'E4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'G4', 'A4', 'B4',
                   'G4', 'B4', 'A4', 'B4',  'C#5', 'D5', 'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G5', 'A5',
                   'F#5', 'D5', 'E5', 'F#5',  'E5', 'D5', 'E5', 'C#5', 'D5', 'E5', 'F#5', 'E5', 'D5', 'C#5',
                   'D5', 'B4', 'C#5', 'D5',  'D4', 'E4', 'F#4', 'G4', 'F#4','E4', 'F#4', 'D5', 'C#5', 'D5',
                   'B4', 'D5', 'C#5', 'B4',  'A4', 'G4', 'A4', 'G4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'D5',
                   'B4', 'D5', 'C#5', 'D5',  'C#5', 'B4', 'C#5', 'D5', 'E5', 'D5', 'C#5', 'D5', 'B4', 'C#5',
                   'D5'
                   ]
right_hand_duration = [1, 1, 1, 1, 1, 1, 1, 1, 
                       0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                       0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                       0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                       0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.25,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                       2
                      ]

left_hand_notes = ['F#5', 'E5', 'D5', 'C#5', 'B4', 'A4', 'B4', 'C#5',
                   'D5', 'C#5', 'B4', 'A4', 'G4', 'F#4', 'G4', 'E4',
                   'D4', 'F#4', 'A4', 'G4',  'F#4', 'D4', 'F#4', 'E4',
                   'D4', 'B3', 'D4', 'A4',  'G4', 'B4', 'A4', 'G4',
                   'D5', 'D5', 'C#5', 'C#5', 'B4', 'D5', 
                   'D5', 'D5',  
                   'D5', 'G5', 'E5', 'A5',
                   'A5', 'F#5', 'G5', 'A5',  'F#5', 'G5', 'A5', 'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G5',
                   'F#5', 'D5', 'E5', 'F#5',  'F#4', 'G4', 'A4', 'B4', 'A4','G4', 'F#4', 'E4', 'D4', 'E4',
                   'G4', 'B4', 'A4', 'G4',  'F#4', 'E4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'G4', 'A4', 'B4',
                   'G4', 'B4', 'A4', 'B4',  'C#5', 'D5', 'A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G5', 'A5',
                   'D4'
                  ]
left_hand_duration = [1, 1, 1, 1, 1, 1, 1, 1, 
                      1, 1, 1, 1, 1, 1, 1, 1, 
                      0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                      0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                      0.5, 0.5, 1, 0.5, 0.5, 1, 
                      1.5, 0.5, 
                      0.5, 0.5, 0.5, 0.5,
                      0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                      0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                      0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                      0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
                      2
                     ]

factor = [2]
length = [0]
decay = [0]
sustain_level = 0.2
right_hand = requirements.get_song_data(right_hand_notes, right_hand_duration, 2, factor, length, decay, sustain_level)

factor = [0.5]
sustain_level = 0.0
left_hand = requirements.get_song_data(left_hand_notes, left_hand_duration, 2, factor, length, decay, sustain_level)
data = left_hand+right_hand
data = data * (4096/np.max(data))
wavfile.write('wav/canon_produced.wav', 44100, data.astype(np.int16))
print("Successful!")
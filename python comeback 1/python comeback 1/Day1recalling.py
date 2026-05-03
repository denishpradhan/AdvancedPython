# # Moode to chord Generator
# available_moods = ["dark", "happy","sad","chill"]
# print("Select from")
# for i in available_moods:
#     print(i)
# mood = input("Enter your mood ")

# if mood == "dark":
#     print("here are some dark chords:\nAm-Em-Dm")
# elif mood == "happy":
#     print("here are some happy chords:\nC-G-Am-F")
# elif mood == "sad":
#     print("here are some sad chords:\nAm-F-C-G")
# elif mood == "chill":
#     print("here are some chill chords:\nDm7-G7-Cmaj7")

# notes=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
# scaleinguitar=["E", "A", "D", "G", "B", "E"]
# scale=input("Enter the scale you want to find the notes for ")
# scalefinder={scales:}

notes = ['C', 'C#', 'D', 'D#', 'E', 'F',
         'F#', 'G', 'G#', 'A', 'A#', 'B']

# Standard tuning (low to high)
strings = ['E', 'A', 'D', 'G', 'B', 'E']

# Example scale: D minor
scale_notes = ['D', 'E', 'F', 'G', 'A', 'A#', 'C']

# hello world
def get_note(open_note, fret):
    index = notes.index(open_note)
    return notes[(index + fret) % 12]


# Print fretboard (0–12 frets)
for string in strings:
    line = []
    for fret in range(13):
        note = get_note(string, fret)
        if note in scale_notes:
            line.append(f"*{note}*")
        else:
            line.append(note)
    print(" | ".join(line))
get_note("D", 3)

print("🎹 Chord Progression Generator")

notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

root_note = input("Enter root note (C, D#, F): ").upper()
scale_type = input("Scale type (maj/min): ").lower()

# Scale intervals
if scale_type == "maj":
    intervals = [2,2,1,2,2,2,1]
    pattern = ["major", "minor", "minor", "major", "major", "minor", "dim"]
    roman = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
else:
    intervals = [2,1,2,2,1,2,2]
    pattern = ["minor", "dim", "major", "minor", "minor", "major", "major"]
    roman = ["i", "ii°", "III", "iv", "v", "VI", "VII"]

# Build scale
root_index = notes.index(root_note)
scale = [root_note]

for step in intervals:
    root_index = (root_index + step) % 12
    scale.append(notes[root_index])

print("\n🎼 Scale Notes:")
print(" ".join(scale[:-1]))  # remove duplicate last note

# Build chords
print("\n🎹 Chords in this scale:")
chords = []

for i in range(7):
    note = scale[i]
    
    if pattern[i] == "major":
        chord = note
    elif pattern[i] == "minor":
        chord = note + "m"
    else:
        chord = note + "dim"
    
    chords.append(chord)
    print(f"{roman[i]} → {chord}")

# Suggested progressions
print("\n🔥 Suggested Progressions:")

if scale_type == "maj":
    print(f"1. {chords[0]} - {chords[4]} - {chords[5]} - {chords[3]}")  # I-V-vi-IV
    print(f"2. {chords[5]} - {chords[3]} - {chords[0]} - {chords[4]}")  # vi-IV-I-V
else:
    print(f"1. {chords[0]} - {chords[3]} - {chords[4]} - {chords[0]}")  # i-iv-v-i
    print(f"2. {chords[5]} - {chords[6]} - {chords[0]}")  # VI-VII-i
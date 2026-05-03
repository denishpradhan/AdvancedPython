print("Find the best chord progression for your song!")
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
root_note = input("Enter the root note (e.g., C, D#, F): ").upper()
scale_type = input("Enter the scale type (Maj/Min): ").lower()

if scale_type == "maj":
    intervals=[2,2,1,2,2,2,1]
else:
    intervals=[2,1,2,2,1,2,2]

root_note_index = notes.index(root_note)
scale = [root_note]

for i in intervals:
    root_note_index=(root_note_index + i) % 12
    scale.append(notes[root_note_index])

print("\nYour notes in the",root_note, scale_type, "scale are:")
print(" ".join(scale))

pattern = ["major", "minor", "minor", "major", "major", "minor", "dim"]
for i in range(7):
    print(f"{i+1} Chord = {scale[i]} {pattern[i]}")
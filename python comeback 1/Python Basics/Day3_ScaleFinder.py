print("Welcome to the Scale Finder!")

notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

root_note = input("Enter the root note (e.g., C, D#, F): ").upper()
scale_type = input("Enter the scale type (Maj/Min): ").lower()

if scale_type == "maj":
    intervals = [2,2,1,2,2,2,1]
else:
    intervals = [2,1,2,2,1,2,2]

root_index = notes.index(root_note)

scale = [root_note]
current_index = root_index

for step in intervals:
    current_index = (current_index + step) % 12
    scale.append(notes[current_index])

print("\nYour notes in the",root_note, scale_type, "scale are:")
print(" ".join(scale))
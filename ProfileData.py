import json
from Day6_AI_DemoVersion import create_profile

profile=create_profile()
with open("profile.json", "w") as file:
    json.dump(profile, file,indent=4)
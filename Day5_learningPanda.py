import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Gym_Hours": [1, 1.5, 1, 2, 1, 1.5, 1],
    "Music_Hours": [0.5, 1, 1.5, 1, 2, 1, 1.5]
}

df = pd.DataFrame(data)
print(df)

df.plot(x="Day", y=["Gym_Hours", "Music_Hours"], kind="bar")
plt.title("Daily hours spent on Gym and Music")
plt.show()

import numpy as np
import sounddevice as sd

def main():

    mysound=sine_tone()
    sd.play(mysound)
    sd.wait()

def sine_tone(
        frequency=440.0,
        duration=1.0,
        amplitude=0.5,
        sample_rate=44100
    ) -> np.ndarray:

    #Calculate the number of samples needed
    n_samples = int(duration * sample_rate)  

    #Create an array of time points
    time_points=np.linspace(0, duration, n_samples, endpoint=False)

    #Generate the sine wave and scale by amplitude
    sine = amplitude * np.sin(2 * np.pi * frequency * time_points)
    return sine


def white_noise(
        duration=1.0,
        amplitude=0.5,
        sample_rate=44100
    ) -> np.ndarray:
    """
    Generate white noise.
    """
    #Calculate the number of samples needed
    n_samples = int(duration * sample_rate)

    #Generate white noise with values between -1.0 and 1.0
    noise = np.random.uniform(low=-1.0, high=1.0, size=n_samples)

    #Scale the noise by the amplitude
    noise *= amplitude
    return noise


if __name__ == "__main__":
    main()

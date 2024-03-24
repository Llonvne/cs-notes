from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    """Encode float x between -1 and 1 as two bytes."""
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name="song.wav", seconds=2):
    """Write the output of a sampler function as a wav file."""
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1
    out.close()

def tri(frequency, amplitude=0.3):
    """ a continous triangle wave"""
    period = frame_rate // frequency
    def sampler(t):
        saw_wav = t / period - floor(t / period + 0.5)
        tri_wav = 2 * abs(2 * saw_wav) - 1
        return amplitude * tri_wav
    return sampler

c_freq = 261.63
e_freq = 329.63
g_freq = 392.00

def both(f, g):
    return lambda x:f(x) + g(x)

def note(f, start, end, fade=0.1):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

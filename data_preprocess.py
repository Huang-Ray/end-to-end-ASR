"""
Creat by SH Huang.
"""
import librosa

from keras.layers import Dense

class fbank:
    def __init__(self, x=None, sr=22500, melfilter=128, banknum=79):
        
        self.x = x
        self.sr = sr
        self.melfilter = melfilter
        self.banknum = banknum
    
    def go(self):

        print("go")





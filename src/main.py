from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

string = input("Input what you wish to beep/boop:\n")

for byte in bytearray(string, "utf8"):
    binary_str = bin(byte)
    binary_str = binary_str[2::]
    for binary in binary_str:
        if binary == "1":
            playsound("sounds/beep.mp3")
        else:
            playsound("sounds/boop.mp3")  

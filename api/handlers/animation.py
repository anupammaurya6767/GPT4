# animation.py

from colorama import Fore, Style
import time

# Function to print text in an animated way with colors
def animated_print(text, delay=1, end='\n', flush=False):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end=end, flush=flush)  # print the end parameter with flush if needed

# Function for designing animation
def animated_design(text, delay=0.1, end='\n', flush=False):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end=end, flush=flush)  # print the end parameter with flush if needed

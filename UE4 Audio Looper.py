import tkinter as tk
from tkinter import filedialog

import soundfile
import numpy as np

# variables you can change
seconds_of_loop_to_append_to_intro = 1.0
# end of variables you can change; Don't touch anything below!

"""
Notes:
The numpy arrays representing audio have channels on the x axis (shape[1]) and samples on the y axis (shape[0]).
Make sure that the two files you select have the same sample rate (you can view this in Adobe Audition)! (I haven't tested what will happen if they are different.)
"""

user_choice = "n"
while user_choice != "y":
  intro_filepath = ""
  loop_filepath = ""
  root = tk.Tk() # just stuff needed to open the file dialogue box
  root.withdraw() # just stuff needed to open the file dialogue box
  intro_filepath = filedialog.askopenfilename(title="Please select the intro .wav file:")
  loop_filepath = filedialog.askopenfilename(title="Please select the loop .wav file:")
  root.destroy()
  print("The two files you selected are:")
  print("Intro filepath:", intro_filepath)
  print("Loop filepath:", loop_filepath)
  user_choice = input("Are you sure you want to overwrite these files with the UE4 formatted versions (y for yes, q to quit, else select files again)? ")
  if user_choice == "q":
    quit()

if(intro_filepath.endswith(".wav") and loop_filepath.endswith(".wav")):
  intro, intro_samp = soundfile.read(intro_filepath)
  loop, loop_samp = soundfile.read(loop_filepath)
else:
  input("Error, selected files aren't .wavs! Press enter or click the X to exit...")
  quit()
 
while intro.shape[0] >= loop.shape[0]:
  print("Intro is too long, so doubled loop segment length (original loop .wav file is unchanged)!")
  loop = np.concatenate((loop, loop), axis=0) # https://stackoverflow.com/a/54389501

sample_cut_num = loop.shape[0] - intro.shape[0]

loop_segment_1 = loop[:sample_cut_num]
loop_segment_2 = loop[sample_cut_num:]

sample_cutoff = int(loop_samp*seconds_of_loop_to_append_to_intro) # calculate the sample number the loop (appeneded to the intro) ends at
new_intro_segment = np.concatenate((intro, loop_segment_1[:sample_cutoff]), axis=0)
new_loop_segment = np.concatenate((loop_segment_2, loop_segment_1), axis=0)

soundfile.write(intro_filepath, new_intro_segment, samplerate = intro_samp, format = "WAV")
soundfile.write(loop_filepath, new_loop_segment, samplerate = loop_samp, format = "WAV")

input("Press enter or click the X to continue...")

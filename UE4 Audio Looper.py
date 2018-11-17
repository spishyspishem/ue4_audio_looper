import tkinter as tk
from tkinter import filedialog

import pydub
from pydub import AudioSegment

# variables you can change
milliseconds_of_loop_to_append_to_intro = 1000 # 1000 milliseconds is one second
# end of variables you can change; Don't touch anything below!

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
  intro = AudioSegment.from_wav(intro_filepath)
  loop = AudioSegment.from_wav(loop_filepath)
else:
  input("Error, selected files aren't .wavs! Press enter or click the X to exit...")
  quit()

while intro.frame_count() >= loop.frame_count():
  print("Intro is too long, so doubled loop segment length (original loop .wav file is unchanged)!")
  loop = loop.append(loop, crossfade=0)

loop_sample_array = loop.get_array_of_samples()
if loop.channels == 1:
  sample_cut_num = int(loop.frame_count()) - int(intro.frame_count())
elif loop.channels == 2:
  sample_cut_num = 2*(int(loop.frame_count()) - int(intro.frame_count()))
else:
  input("Error, looping segment has more than 2 channels! Press enter or click the X to exit...")
  quit()

loop_samp_array_1 = loop_sample_array[:sample_cut_num]
loop_samp_array_2 = loop_sample_array[sample_cut_num:]

loop_segment_1 = loop._spawn(loop_samp_array_1)
loop_segment_2 = loop._spawn(loop_samp_array_2)

new_intro_segment = intro + loop_segment_1[:milliseconds_of_loop_to_append_to_intro]
new_loop_segment = loop_segment_2.append(loop_segment_1, crossfade=0)

new_intro_segment.export(intro_filepath, format="wav")
new_loop_segment.export(loop_filepath, format="wav")

input("Press enter or click the X to continue...")

# Music Visualizer In Python Using Pygame

An attempt at a music visualizer done in `Python 3.8.2`.  Using Pygame to render the visualization and numpy for calculations including `fft` and various data transformations.

*STILL A WORK IN PROGRESS*

## TODO

- bin fft power output logarithmically so its not low end heavy on spectrum
- fix sampling time window to exactly match sound output

## To Run

Forgive the current working state of the program, still working on the math. BUT to run as-is:

Install prereqs -> 

```shell
sudo apt-get install python3-pygame
python3 -m pip install numpy
```

Modify code to pass a `.wav` file with a `44.1 kHz` sampling rate.

Then, run -> 

```shell
python3 main.py
```

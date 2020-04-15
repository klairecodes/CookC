# CookC
A cli-based game ~~written in C~~ about being a concessions worker.
This branch is written in Python, it will later be ported to C once I actually learn the language.
The game is part of a series of mini games that will be written to work on a ThinkPad x230 Cyberdeck build, for fun.


The game is a little cursed, as it is entirely stored in an array. And I mean entirely. Not just the game board and the player, but also the UI(HUD™). This makes for some interesting cases to deal with, such as making sure the character can't step into the UI, and numerical digits being inserted character by character.

Why would I implement this in an impractical way? Well, it makes it easy to display to inexpensive character LCD displays. Each element in the array maps to a character on the screen, and the cursor can be moved to where a value would need to be changed, or act as the player of the game itself. The game could run on extremely low power no matter what, making it great for an apocalypse. 

I was inspired by [Collapse OS](https://itsfoss.com/collapse-os/), an OS designed to run on a z80 chip found extremely commonly in consumer electronics. The idea is that due to their ubiquity, these processors could be scavenged and used to run a kernel and operating system to be able to develop software. Seeing this, I thought of other components that are that common, and character LCD screens came to mind. They are plentiful, durable, and long lasting, so why not try to make them do something in the event of an emergency? Natrually what I thought they should do is play games. 

To see the ThinkPad Cyberdeck that this game will be running on, and its build process, go [HERE](https://imgur.com/a/ExLBzjo)

Now on to the project specifically:

## Dependencies
+ Python 3.7
+ Python [Keyboard Module](https://pypi.org/project/keyboard/) for keyboard input*
+ Python [RPLCD API](https://rplcd.readthedocs.io/en/stable/index.html) for LCD display

Note that in Linux, the script must be run as root for keyboard input to work. I imagine this is for security reasons as keyloggers could use the API for malicious purposes.

## Installation
+ Make sure dependencies are installed with
``` 
pip install keyboard RPLCD
```
+ Then clone the repo, navigate to the CookCP directory, and run
```
./CookC.py
```
or
```
python CookC.py
```

## Screenshots
![Gameboard](Screenshot.png?raw=true "Screenshot")

![Keyboard Input](/relative/path/to/img.jpg?raw=true "Screenshot1")

![Exit condition and quitting](/relative/path/to/img.jpg?raw=true "Screenshot2")

##### This game is still in early development.

# guessing game
## How to open a terminal
First Open your terminal (windows default is cmd)
<br><br>
To do this: press ```ctrl``` + ```r``` and type "cmd"
<br><br>
Or
<br><br>
Press ```win``` then search "cmd"

## How to download
#### First create a new directory
### In <b>windows</b> use:
```
mkdir <DirectoryName>
```
Then use ```cd <DirectoryName>```
<br><br>
Check the new directory was added throught the use of the ```dir``` command
<br><br>
### In <b>Linux</b> use:
```
mkdir <DirectoryName>
```
Then use ```cd <DirectoryName>```
<br><br>
Check the new directory was added throught the use of the ```ls``` command
<br><br>
### To retrieve the python file either use:
```
Wget https://raw.githubusercontent.com/JakkuPingu/guessing-game/main/game.py (Linux only)
```
Or
```
Curl https://raw.githubusercontent.com/JakkuPingu/guessing-game/main/game.py
```
Output a file by using: ```> <Newfilename>``` after ```Wget``` or ```Curl```
<br>
<br>
Or use ```-o <Newfilename>``` after ```Curl```

## How to run the game
To run the game use the command:
```
python <filename>
```
or 
```
python3 <filename>
```

## How the game works
<br>The guessing game is simple</br>
### First
<p>Player one will put in what they would like the answer to be (any digit, don't be too harsh ;))</p>

### Second
<p>Player two will guess what the number is</p>

### Third
<p>player two has up to three guesses to guess the correct answer</p>

### Finally
<p>If player two has not guessed the answer you will be presented with the text telling you that you have failed...</p>
<p> <s>(WIP)</s> you will then be shown the correct answer</p>
<p>If player two guesses the answer within 3 guesses you will be congratulated</p>

### Would like help on how to hide the orginal answer when typed in

<h3>Feel free to use any code and please give me feedback on how I could improve this game</h3>

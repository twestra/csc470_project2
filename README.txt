README file for:

Project 2
CSC 470-01
Jack Taylor & Thomas


Our programs were written in python.



As for our program deliverables, the naming scheme is as follows:

D1 is named "d1.py".
D2 is named "d2.py".
D3 is named "d3.py".





We have two machines that can be used to test our programs.


The first machine lies in the directory named "Machine1", and is used to describe the sheep language.

The files included in this directory describe this first machine.  They are named "alphabet.txt", "finalStates.txt", "startState.txt", "transitionTable.txt", and "states.txt".

Machine1 describes the following regular expression: /baaa*!/


The second machine lies in the directory named "Machine2", and is used to describe the language which accepts the words "car" and "cars".

The files included in this directory describe this first machine.  They are also named "alphabet.txt", "finalStates.txt", "startState.txt", "transitionTable.txt", and "states.txt".

Machine2 describes the following regular expression: /cars?/





INSTRUCTIONS FOR EXECUTION IN TERMINAL:

Two arguments must be provided in order to properly specify both the machine you are testing as well as the tape you are using.
The machine number will be the first argument (a single digit), and the string you would like to use as tape will be the second argument (a series of characters with no spaces).

The following directions will guide you through it:

1. Open up terminal on your device.
2. Use the cd command to get to the working directory named "csc470_project2"
3. Use the following syntax when you would like to run the program:

	python program_name machine# tape

For example, if you would like to test the second deliverable program on the first machine with the string "baaa!", you would enter the following command into terminal: python d2.py 1 baaa!


The program will print either "accept" or "reject", and execution will halt.
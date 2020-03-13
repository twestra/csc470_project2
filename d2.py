import sys
import os

def D_Recognize2(tape, startState, finalStates, transitionTable):
    
    #initialize various necessary variables before beginning loop
    tapeIndex = 0
    index = tape[tapeIndex]
    current_state = startState
    remainingTape = len(tape)
    startStateValues = []
    indexIsStartState = False
    
    
    #make a list of all values that allow us to transition from our start state
    #this is helpful so we can just ignore values that won't lead us into d-recognize algorithm
    for i in range(len(transitionTable)):
        if transitionTable[i][0] == startState and transitionTable[i][2] != "NULL":
            startStateValues.append(transitionTable[i][1])
    
    #we have to cycle through entire tape
    while remainingTape >=0:
        #check if we can transition
        indexIsStartState = False
        for value in startStateValues:
            if index == value:
                indexIsStartState = True
        
        #if our index does allow us to transition, we can move to our D_Recognize Function
        if indexIsStartState:
            while remainingTape >=0:
                #first, check if we are in a final state
                in_final = False
                for i in range(len(finalStates)):
                    if current_state == finalStates[i]:
                        in_final = True
                #now check if we are at the end of the tape
                if remainingTape == 0:
                    if in_final == True:
                        return("accept")
                    else:
                        return("reject")
                
                #now see what our next transition will be by cycling through transition table and looking at all transtitions
                transition_found = False
                null_transition = False
                
                for i in range(len(transitionTable)):
                    #if we are going to transition to a null value, we can just basically reset our machine to the start state
                    if transitionTable[i][0] == current_state and transitionTable[i][1] == index and transitionTable[i][2] == "NULL":
                        null_transition = True
                        transition_found = True
                        current_state = startState
                    #if we're not transitioning to a null value, we can just set the next value
                    elif transitionTable[i][0] == current_state and transitionTable[i][1] == index:
                        next_state = transitionTable[i][2]
                        transition_found = True
                
                #if after cycling through the entire table, and we don't find any possible transitions (because it's not in our alphabet), we can just ignore the symbol and continue
                if  not transition_found:
                    tapeIndex+=1
                    if tapeIndex< len(tape):
                        index = tape[tapeIndex]
                    remainingTape-=1
                    current_state = startState
                    break
                
                #now we will move to the next symbol and the state defined by the previous transition
                
                #if we go to null, basically just reset and break from d_recognize algorithm
                if null_transition:
                    current_state = startState
                    break
                #otherwise, move to next symbol and change our values
                else:
                    current_state = next_state
                    tapeIndex+=1
                    if(tapeIndex<len(tape)):
                        index = tape[tapeIndex]
                    remainingTape -= 1
        #this happens if we are not at a value that lets us transition from start state: basically, just move forward and check again
        else:
            tapeIndex+=1
            if tapeIndex < len(tape):
                index = tape[tapeIndex]
            remainingTape-=1
    #if, at the end of our tape, we have not had a match, we can return "reject"
    return "reject"
            
    
    
#for parsing transition table into 2d array of lists, where each row represents a transition
def transitionparser(lines):
    strings = []
    parsedstrings = [['']*3]*lines
    i = 0
    f = open("transitionTable.txt", "r")
    strings = f.readlines()
    f.close()
    for string in strings:
        newstring = string.replace('\n', '')
        newnewstring = newstring.replace('\"', '')
        parsedstrings[i] = newnewstring.split(', ')
        i+=1
    return parsedstrings
#for parsing end states into list
def finalstatesparser():
    strings = []
    i = 0
    f = open("finalStates.txt", "r")
    strings = f.readlines()
    f.close()
    for string in strings:
        strings[i] = string.replace('\n', '')
        i+=1
    return strings
        

if __name__ == "__main__":
   #change working directory depending on argument specified by user
    arg1 = int(sys.argv[1])
    
    if (arg1 == 1):
        os.chdir("Machine1")
    elif (arg1 == 2):
        os.chdir("Machine2")
    else:
        print("Incorrect syntax for machine specification. Exiting.")
        sys.exit()
    
    
    #tape
    arg2 = sys.argv[2]
    #print args
    tape = arg2
    
    #start state:
    fss = open("startState.txt")
    startstate = fss.read()
    fss.close()
    #print "This is the startstate: "
    #print startstate
    
    #final states
    #print "These are the final states: "
    finalStates = finalstatesparser()
    #print finalStates
    
    #transition table:
    #print "These are the transitions"
    if (arg1 == 1):
        transition_table = transitionparser(15)
    elif (arg1 == 2):
        transition_table = transitionparser(20)
    #print(transition_table)

    #D-Recognize algorithm
    print(D_Recognize2(tape, startstate, finalStates, transition_table))

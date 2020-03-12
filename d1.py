import sys

#def D_Recognize(tape, machine):
#    index = #beginning of tape
#    current_state = #start state
#    while true:
#        if (end of input):
#            if current_state == #accept state:
#                return "accept"
#            else
#                return "reject"
#        else if(transitiontable[current_state, tape[index]] == NULL)
#            return "reject"
#        else
#            current_state = transitiontable[current_state, tape[index]]
#            index+=1
#    return 0
    
def D_Recognize(tape, startState, finalStates, transitionTable):
    #initialize various necessary variables before beginning loop
    tapeIndex = 0
    index = tape[tapeIndex]
    current_state = startState
    remainingTape = len(tape)
    
    while remainingTape >= 0:
        #look to see which conditionals will become true
        #first we check if the next state exists
        null_transition = False
        transition_found = False
        for i in range(len(transitionTable)):
            if transitionTable[i][0] == current_state and transitionTable[i][1] == index and transitionTable[i][2] == "NULL":
                null_transition = True
                transition_found = True
            elif transitionTable[i][0] == current_state and transitionTable[i][1] == index:
                next_state = transitionTable[i][2]
                transition_found = True
        if not transition_found:
            return("String contains character not in alphabet")
        #then we check if the current state is an accepting one
        in_final = False
        for i in range(len(finalStates)):
            if current_state == finalStates[i]:
                in_final = True
        
        #now we implement the D_Recognize algorithm:
        
        #case where end of input has been reached
        if remainingTape == 0:
            if in_final == True:
                return("accept")
            else:
                return("reject")
        
        #case where there is no transition for the current state and tape index
        elif null_transition == True:
            return("reject")
            
        #case where we advance to next state and try again
        else:
            current_state = next_state
            tapeIndex += 1
            if (tapeIndex < len(tape)):
                index = tape[tapeIndex]
            remainingTape -= 1
            
    
    
#for parsing transition table into 2d array of lists, where each row represents a transition
d
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
    #need - start states, end states, tape
    
    #tape
    args = sys.argv[1:]
    #print args
    tape = (" ".join(args))
    #print(tape)
    
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
    transition_table = transitionparser(15)
    #print(transition_table)

    #D-Recognize algorithm
    print(D_Recognize(tape, startstate, finalStates, transition_table))

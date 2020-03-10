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
        parsedstrings[i] = newstring.split(', ')
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
    #need - start states, end states, tape
    
    #tape
    args = sys.argv[1:]
    print(args)
    tape = (" ".join(args))
    print(tape)
    
    #start state:
    fss = open("startState.txt")
    startstate = fss.read()
    fss.close()
    print("This is the startstate: ")
    print(startstate)
    
    #final states
    print("These are the final states: ")
    print(finalstatesparser())
    
    #transition table:
    print("These are the transitions")
    print(transitionparser(3))

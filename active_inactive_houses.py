def stateHouses(states,days):
    final_states=[0]*len(states)

    while days>0:
        for i in range(len(states)):
            if i==0:
                a=0^states[i+1]
            elif i==(len(states)-1):
                a=0^states[i-1]
            else:
                a=states[i+1]^states[i-1]
            final_states[i]=a
        states=final_states
        final_states=[0]*len(states)
        days-=1
    return states

print(stateHouses([1,0,0,0,0,1,0,0],4))

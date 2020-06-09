import numpy as np
full_hosts=[0, 0, 0]
empty_hosts=[0, 0, 0]

#file to list
f = open('FleetState_clean.txt')
lines = f.readlines()
min_empty_slots = [10,10,10] # TODO improve init
min_empty_count = [0,0,0]

for i in range(len(lines)):
    line = lines[i].split(',')
    line[-1] = line[-1].rstrip("\n")
    line[2:] = list(map(int, line[2:]))
    host_type_index = int(line[1][-1])-1 # [M1,M2,M3]

    empty_slots=line[2]-sum(line[3:])

    if empty_slots == 0:
        full_hosts[host_type_index]+=1
    elif empty_slots == line[2]:
        empty_hosts[host_type_index]+=1

    if empty_slots < min_empty_slots[host_type_index]:
        min_empty_slots[host_type_index]= empty_slots
        min_empty_count[host_type_index] = 1
    elif empty_slots == min_empty_slots[host_type_index]:
        min_empty_count[host_type_index] += 1

print(f'EMPTY: M1={empty_hosts[0]}; M2={empty_hosts[1]}; M3={empty_hosts[2]};')
print(f'FULL: M1={full_hosts[0]}; M2={full_hosts[1]}; M3={full_hosts[2]};')
print(f'MOST FILLED: M1={min_empty_count[0]},{min_empty_slots[0]}; M2={min_empty_count[1]},{min_empty_slots[1]}; M3={min_empty_count[2]},{min_empty_slots[2]};')





#TODO error checking
# Read line, check for error, no error go through
# error print in output file:"line no ignored due to ERROR NAME:

# sum_ac()
# for i in range(3,n):




f.close()
full_hosts=[0, 0, 0]
empty_hosts=[0, 0, 0]
warnings = '\nWARNINGS \n\n'
#file to list
f = open('FleetState.txt')
lines = f.readlines()
lines[-1] = lines[-1]+'\n'

min_empty_slots = [10,10,10] # TODO improve init
min_empty_count = [0,0,0]
continue_flag = False
hostID = [0]*len(lines)

for i in range(len(lines)):
    line = lines[i].split(',')
    line[-1] = line[-1].rstrip("\n")

    # Warning for hostID not int
    if not(line[0].isdigit()):
        warnings += 'Warning: Unexpected line format (hostID not an int): \n' + lines[i] + 'Action: Line excluded from counts.\n\n'
        continue

    # Warnings for dublicate host ID
    if line[0] in hostID:
        warnings += 'Warning: Duplicate host ID in line:\n' + lines[i] + 'No action taken. Line counted as normal.\n\n'
    hostID[i] = line[0]

    # Warnings and break for non binary state
    for j in range(3, len(line)):
        if not((line[j] == '1') or (line[j] == '0')):
            warnings += 'Warning: Non binary value of slot state: \n' + lines[i] + 'Action: Line excluded from counts.\n\n'
            continue_flag = True
            break
    if continue_flag:
        continue_flag = False
        continue

    line[2:] = list(map(int, line[2:]))

    # Warning for number of slots
    if line[2] != len(line[3:]):
        warnings += 'Warning: amount of slot states provided different to the given amount of slots (N)' \
                    '\n' + lines[i] + 'Action: Adjusting N to reflect amount of slot states.\n\n'
        line[2]=len(line[3:])

    empty_slots = line[2] - sum(line[3:])

    host_type_index = int(line[1][-1])-1 # [M1,M2,M3]


    if empty_slots == 0:
        full_hosts[host_type_index]+=1
    elif empty_slots == line[2]:
        empty_hosts[host_type_index]+=1

    if empty_slots < min_empty_slots[host_type_index]:
        min_empty_slots[host_type_index]= empty_slots
        min_empty_count[host_type_index] = 1
    elif empty_slots == min_empty_slots[host_type_index]:
        min_empty_count[host_type_index] += 1

outF = open("Statistics.txt","w")
outF.write(f'EMPTY: M1={empty_hosts[0]}; M2={empty_hosts[1]}; M3={empty_hosts[2]};\n')
outF.write(f'FULL: M1={full_hosts[0]}; M2={full_hosts[1]}; M3={full_hosts[2]};\n')
outF.write(f'MOST FILLED: M1={min_empty_count[0]},{min_empty_slots[0]}; M2={min_empty_count[1]},{min_empty_slots[1]}; M3={min_empty_count[2]},{min_empty_slots[2]};\n')
outF.write(warnings)




#TODO error checking
# Read line, check for error, no error go through
# error print in output file:"line no ignored due to ERROR NAME:

# sum_ac()
# for i in range(3,n):




f.close()
import random
vehicles = {
# .co.uk
"fire engines": {
"Water Ladder",
"Light 4X4 Pump (L4P)",
"Rescue Pump"
},

"police cars": {
"Incident response vehicle (IRV)",
"Dog Support Unit (DSU)",
"Armed Response Vehicle (ARV)",
"Police helicopter"
},

"ambulance": {
"Ambulance"
},

"Misc" : {
"Aerial Appliance",
"Fire Officer",
"Rescue Support Unit (RSU)",
"Rescue Pump",
"Water Carrier",
"HazMat Unit",
"Breathing Apparatus Support Units (BASU)",
"Incident Command and Control Unit (ICCU)"
},
# .com
"firetrucks": {
"Type 1 fire engine",
"Type 2 fire engine",
"Quint",
"Rescue Engine"
}

}

def randomint():
 return random.randint(1, 30)




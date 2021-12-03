# forward/backward, up/down
position_1 = [0,0]
# forward/backward, up/down, aim
position_2 = [0,0,0]

def interpreter_1(pos, instruction):
	if instruction[0] == 'up':
		pos[1] += int(instruction[1])
	if instruction[0] == 'down':
		pos[1] -= int(instruction[1])
	if instruction[0] == 'forward':
		pos[0] += int(instruction[1])
def interpreter_2(pos, instruction):
	if instruction[0] == 'up':
		pos[2] -= int(instruction[1])
	if instruction[0] == 'down':
		pos[2] += int(instruction[1])
	if instruction[0] == 'forward':
		pos[0] += int(instruction[1])
		pos[1] -= pos[2]*int(instruction[1])

with open ('input.txt','r') as f:
	for index, line in enumerate((f.read().splitlines())):
		interpreter_1(position_1,line.split())
		interpreter_2(position_2,line.split())

print abs(position_1[0]*position_1[1])
print abs(position_2[0]*position_2[1])
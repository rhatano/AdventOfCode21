counter = 0
window = []
with open ('input.txt','r') as f:
	lines = list(enumerate((f.read().splitlines())))
	for index, line in lines:
		total = 0
		if index < len(lines)-2:
			for pos, entry in lines[index:index+3]:
				total += int(entry)
			window.append(total)
for index, entry in enumerate(window):
	if index < len(window)-1:
		if window[index] < window[index+1]:
			counter += 1
print counter
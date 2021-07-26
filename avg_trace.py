from os import listdir
from os.path import join

FOLDER = 'curves'
OUTPUT_FILE = 'all_avg.txt'

N = 2000
T = 29000

avg = [0]*T
count = 0

for file in listdir(FOLDER):
	if file == '.DS_Store':
		continue
	
	count += 1
	path = join(FOLDER, file)
	print(path)
	f = open(path, 'r')
	data = f.read()
	data = data.split('\n')
	data = [float(i) for i in data if i != '']

	for i in range(T):
		avg[i] += data[i]
	f.close()

assert count == N
avg = [i/N for i in avg]

f = open(OUTPUT_FILE, 'w')
for v in avg:
	line = str(v) + '\n'
	f.write(line)
f.close()

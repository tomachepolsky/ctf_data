f = open('sqli.txt')
flag = {}
for line in f.read().split('\n'):
	if 'FROM mysql.user WHERE user=' in line:
		x = line.split('user=CHAR(')[1]
		if 'LIMIT 0,1),' in line:
			print(x)
			n = x.split('LIMIT 0,1),')[1].split(',')[0]
			c = x.split('LIMIT 0,1),')[1].split(' > '[1].split(' ')[0]
			
			if n not in flag:
				flag[n] = []
			flag[n].append(c)
			print("{}. {} ({})".format(n, int(c), chr(int(c))))
		else:
			print(x)
for n in flag:
	a,b = flag[n][-2:]

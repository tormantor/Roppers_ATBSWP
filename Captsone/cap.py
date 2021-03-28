import pwn,json

def stdout(io):
	return io.recvline(timeout=1)[2:-1].decode('utf-8')

def configLoad(x):
	return json.load(open(f'bandit{x}.cfg','r'))

def pwReadOrWrite(f,i,out=''):
	if f:
		passwords=open('passwords.txt','a')
		passwords.write(f'{i} {out}\n')
	else:
		passwords=open('passwords.txt','r')
		return passwords.readlines()[i][2:-1]

def sshClient(config,i):
	sesh=pwn.ssh(config['Username'],config['Address'],password=pwReadOrWrite(0,i-1),port=config['Port'])
	io=sesh.process('sh')
	io.sendline(config['Commands'][0])
	pwReadOrWrite(1,i+1,stdout(io))
	sesh.close()

config=configLoad(1)	
sesh=pwn.ssh(config['Username'],config['Address'],password='bandit0',port=config['Port'])
io=sesh.process('sh')
io.sendline(config['Commands'][0])
pwReadOrWrite(1,1,stdout(io))
sesh.close()
for i in range(1,6):
	sshClient(configLoad(i+1),i)	
	
	
	

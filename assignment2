import os
name = "hello-world"
for nw in range(100):
	image = "sudo docker run --name dadhoc" + str(nw) + " -d  "+ str(name) + " --restart unless-stopped /bin/bash"

	if nw in range(25,49):
		name = "fedora"
	elif nw in range(50,74):
		name = "centos"
	elif nw > 74:
		name = "java"
	os.system(image)
os.system("sudo docker ps -a --format 'table {{.Names}}\t{{.Status}}' > log.txt")
os.system("sudo docker stats -a --no-stream --format 'table{{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}' > stats.txt")

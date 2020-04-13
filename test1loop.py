import time
import os

timeout = 10
timeout_start = time.time()
while time.time() < timeout_start + timeout:
	os.system('cal &>> SomeFile.txt');

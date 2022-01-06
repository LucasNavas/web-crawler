import time
timeout = 5 #segundos
timeout_start = time.time()

while time.time() < timeout_start + timeout:
    print(time.time())
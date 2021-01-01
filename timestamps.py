import time
import datetime


def send_email():
    for i in range(1000000):
        pass


start = time.time()
send_email()
end = time.time()
diff = end - start
print(diff)

from datetime import datetime
from datetime import timezone
import time


unix = int(time.time())

username = 'miko'

id = str(unix) + username

print(id)
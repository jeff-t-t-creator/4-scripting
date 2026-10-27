#!/usr/bin/env python3

import sys
from datetime import datetime
from zoneinfo import ZoneInfo

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <name>")
    sys.exit(1)

name = sys.argv[1]
current_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z %z")

print(f"Hello {name}, right now the time is {current_time}")

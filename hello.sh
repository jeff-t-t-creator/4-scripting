
#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

name="$1"
current_time=$(date '+%Y-%m-%d %H:%M:%S %Z %z')

echo "Hello $name, right now the time is $current_time"

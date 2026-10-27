# Task 4 - Scripting

This repository contains a Bash script and a Python script that greet a user by name and display the current date and time, including the system's timezone.

## Files

- `hello.sh` - Bash script
- `hello.py` - Python script

## 1. Bash Script

### How it works
The Bash script accepts a name as a command-line argument and prints a greeting with the current date, time, and timezone.

### Interpreted or compiled?
Bash is an **interpreted shell language**. The script is executed by the Bash interpreter rather than being compiled into a standalone executable.

### How to run

Make the script executable:

```bash
chmod +x hello.sh
```

Run it with a name:

```bash
./hello.sh John
```

You can also run it directly through Bash:

```bash
bash hello.sh John
```

## 2. Python Script

### How it works
The Python script accepts a name as a command-line argument and prints the same greeting with the current date, time, and timezone.

### Interpreted or compiled?
Python is generally considered an **interpreted language**. Python source code is executed by the Python interpreter. Python may also generate bytecode internally during execution.

### How to run

Run the script using Python 3:

```bash
python3 hello.py John
```

## Example Output

```text
Hello John, right now the time is 2026-10-27 10:56:36 IST +0530
```

The date and time in the actual output will vary depending on when the script runs and the system's configured timezone.

## Error Handling

Both scripts display a usage message if no name is provided.

Bash example:

```bash
./hello.sh
```

Python example:

```bash
python3 hello.py
```

Expected usage message:

```text
Usage: hello.sh <name>
Usage: hello.py <name>
```

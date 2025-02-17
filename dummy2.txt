import sqlite3
import os
import pickle
import subprocess

def insecure_login(username, password):
    # Hardcoded credentials (Security issue: CWE-798)
    if username == "admin" and password == "password123":
        print("Login successful!")
    else:
        print("Login failed!")

# SQL Injection vulnerability (CWE-89)
def vulnerable_query(user_input):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    cursor.execute(query)  # Dangerous practice
    result = cursor.fetchall()
    print(result)
    conn.close()

# Command Injection vulnerability (CWE-78)
def run_command(cmd):
    os.system(cmd)  # Unsanitized user input used in system command

# Deserialization of untrusted data (CWE-502)
def insecure_deserialization(data):
    return pickle.loads(data)  # Arbitrary code execution risk

# Use of subprocess with unsanitized input (CWE-78)
def dangerous_subprocess(command):
    subprocess.call(command, shell=True)  # Potential security risk

if __name__ == "__main__":
    insecure_login("admin", "password123")
    vulnerable_query("' OR '1'='1")  # Typical SQL injection payload
    run_command("ls")  # Potentially dangerous system command
    insecure_deserialization(b"cos
system
(S'ls'
tR.")  # Example pickle payload
    dangerous_subprocess("rm -rf /")  # Dangerous command execution

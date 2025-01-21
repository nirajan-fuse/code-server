#!/usr/bin/env python
import os
import shlex
import sys
import subprocess

# Entrypoint is start.sh
command = []

# If we want to survive restarts, launch the command using `run-one-constantly`
if os.environ.get("RESTARTABLE") == "yes":
    command.append("run-one-constantly")

# We always launch a jupyter subcommand from this script
command.append("code-server")

# Append any optional SERVER_ARGS we were passed in.
# This is supposed to be multiple args passed on to the code server command,
# so we split it correctly with shlex
if "SERVER_ARGS" in os.environ:
    command += shlex.split(os.environ["SERVER_ARGS"])

bind_addr = ["--bind-addr", "0.0.0.0:8080"]
command.extend(bind_addr)

subprocess.Popen(["/bin/bash", "/tmp/start-nginx.sh"])

# command = ["bash", "-c", " ".join(command) + " & /tmp/start-nginx.sh"]

# command.extend(["--abs-proxy-base-path","/user"])

# Pass through any other args we were passed on the command line
command += sys.argv[1:]

# Execute the command!
print("Executing: " + " ".join(command))
os.execvp(command[0], command)

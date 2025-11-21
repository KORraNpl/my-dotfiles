#!/usr/bin/env python3

# Script creates a Python venv under ~/opt/, installs desired packages, links binaries in ~/bin/ and adds this directory
# to $PATH.
# Why: to have some Python tools always at hand, without polluting global environment with packages.

import os
import subprocess

packages_to_install = ('pre-commit', 'flake8', 'pyupgrade')

# Set home directory path
home = os.path.expanduser('~')
opt_dir = os.path.join(home, "opt")
bin_dir = os.path.join(home, "bin")
venv_dir = os.path.join(opt_dir, "venv")


# Function to execute commands safely without shell=True
def run_command(command):
    print(f'Running: {' '.join(command)}')
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    print(result.stdout.strip())


# Step 1: Create ~/opt directory
print(f"Creating {opt_dir}...")
os.makedirs(opt_dir, exist_ok=True)

# Step 2: Create and set up virtual environment
if os.path.exists(venv_dir):
    raise FileExistsError(f"The directory '{venv_dir}' already exists. Aborting...")
run_command(['python3', "-m", "venv", venv_dir])

venv_python = os.path.join(venv_dir, "bin", "python")
venv_pip = os.path.join(venv_dir, "bin", "pip")

run_command([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
run_command([venv_pip, "install", *packages_to_install])

# Step 3: Link binaries to ~/bin
print(f"Linking binaries to {bin_dir}...")
os.makedirs(bin_dir, exist_ok=True)

for package in packages_to_install:
    package_bin = os.path.join(venv_dir, 'bin', package)
    symlink_path = os.path.join(bin_dir, package)
    if not os.path.exists(symlink_path):
        os.symlink(package_bin, os.path.join(bin_dir, package))

# Step 4: Update .zshrc to include ~/bin in PATH
zshrc_path = os.path.join(home, '.zshrc')
path_line = 'export PATH=${HOME}/bin:${PATH}\n'

with open(zshrc_path, 'r') as zshrc_file:
    zshrc_content = zshrc_file.readlines()

if path_line in zshrc_content:
    print(f"PATH already includes {bin_dir}, no changes made to .zshrc.")
else:
    with open(zshrc_path, 'a') as zshrc_file:
        zshrc_file.write(path_line)
        print(f"Appended PATH update to {zshrc_path}.")

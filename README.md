# smb-signing-not-required-poc

# SMBProtocol Python Library

## Overview

Welcome to the SMBProtocol Python library, a powerful tool for seamless integration with the Server Message Block (SMB) protocol. This library simplifies the process of establishing connections, sessions, and tree connects, allowing you to effortlessly work with SMB in your Python projects.

## Prerequisites

Before using the SMBProtocol library, make sure you have Python 3 and pip installed on your system. If not, follow the steps below:

### 1. Install Python 3

Download and install Python 3 from the official website: [Python Downloads](https://www.python.org/downloads/)

### 2. Install pip

Pip is the package installer for Python. If it's not included with your Python installation, you can install it using the following command:

```bash
# On Unix/macOS
python3 -m ensurepip --default-pip

# On Windows
python -m ensurepip --default-pip


PowerShell (Windows)
If you're using PowerShell on Windows, you can install Python and pip using the following commands:

powershell
# Install Python 3
choco install python

# Install pip
python -m ensurepip --default-pip



**Ubuntu**
On Ubuntu, you can use the package manager to install Python and pip:

bash
# Install Python 3
sudo apt-get update
sudo apt-get install python3

# Install pip
sudo apt-get install python3-pip


**macOS**
On macOS, you can use the package manager Homebrew to install Python and pip:

bash

# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python

# Install pip
python -m ensurepip --default-pip




**Install and Upgrade Package**

**Windows:**
Open the Command Prompt as an administrator and run:

bash
pip install --upgrade smbprotocol

**Ubuntu**:
Open the terminal and run:

bash
sudo pip install --upgrade smbprotocol

**macOS**:
Open the terminal and run:

bash
pip install --upgrade smbprotocol

#!/bin/bash
echo "****************************************"
echo " Setting up EV Charging Station Locator Microservice Environment"
echo "****************************************"

# Check if Python 3.12 is available, otherwise use the default Python
if command -v python3.12 &>/dev/null; then
    python_cmd="python3.12"
else
    python_cmd="python3"
fi

echo "Checking the Python version..."
$python_cmd --version

# Create a Python virtual environment for the EV Charging Station Locator Microservice
$python_cmd -m venv ~/ev-charging-venv || { echo "Error creating virtual environment."; exit 1; }

echo "Configuring the developer environment..."
# Check if the lines already exist in ~/.bashrc before appending them
if ! grep -q "EV Charging Station Locator Microservice additions" ~/.bashrc; then
    echo "# EV Charging Station Locator Microservice additions" >> ~/.bashrc
    echo "export GITHUB_ACCOUNT=\$GITHUB_ACCOUNT" >> ~/.bashrc
    echo 'export PS1="\[\e]0;\u:\W\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> ~/.bashrc
fi

echo "Installing Python dependencies for the EV Charging Station Locator Microservice..."
source ~/ev-charging-venv/bin/activate && python -m pip install --upgrade pip wheel
# Make sure to update the path to the requirements file of your new project
source ~/ev-charging-venv/bin/activate && pip install -r path/to/your/new/project/requirements.txt
echo "source ~/ev-charging-venv/bin/activate" >> ~/.bashrc

echo "****************************************"
echo " EV Charging Station Locator Microservice Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use 'exit' to close this terminal and open a new one to initialize the environment"
echo ""

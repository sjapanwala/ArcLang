#!/bin/bash
TARGET_PATH="/usr/local/bin/alang"
PYTHON_SCRIPT_URL="https://raw.githubusercontent.com/sjapanwala/ArcLang/refs/heads/main/alang.py"

# Check if the script is already installed
if [ -e "$TARGET_PATH" ]; then
    echo -e "\033[91mArcLang is already installed.\033[0m"
    read -p "Do you want to Remove Installation? (y/n): " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
        sudo rm "$TARGET_PATH"
        if [ $? -eq 0 ]; then
            echo -e "\033[32mInstallation Removed\033[0m"
            exit 0
        else
            echo -e "\033[91mRemoval Failed\033[0m"
            exit 1
        fi
    else
        echo -e "\033[91mRemoval Aborted\033[0m"
        exit 1
    fi
fi

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "\033[31mPython3 is not installed.\033[0m"
    echo -e "\033[90mC'mon, didn't you read that Python was part of the app?\033[0m"
    echo -e "\nWindows: winget install python3\nHomeBrew: brew install python3\nAPT: sudo apt install python3\nPacman: sudo pacman -S python3\nYum: sudo yum install python3\nZypper: sudo zypper install python3\nApk: sudo apk add python3\n"
    exit 1
fi

# Proceed with installation
echo -e "Welcome To ArcLang Installer,\nThis will install the language on your device.\nIf you wish to remove it, run this file again."
read -p "Do you wish to continue? (y/n): " answer
if ! [[ "$answer" =~ ^[Yy]$ ]]; then
    echo -e "\033[91mInstallation Aborted\033[0m"
    exit 1
fi

# Download and set permissions
sudo curl -s -o "$TARGET_PATH" "$PYTHON_SCRIPT_URL"
sudo chmod +x "$TARGET_PATH"

# Verify installation
if [[ -f "$TARGET_PATH" ]]; then
    echo -e "\033[32mInstallation successful! You can now run your script using 'py' from anywhere.\033[0m"
    echo -e "Successfully installed!\nType 'alang' to run the console\nOr run a file through an argument."
else
    echo -e "\033[91mInstallation failed.\033[0m"
    exit 1
fi

# Cleanup script
echo -e "\033[35mScript Finished\033[0m"
SCRIPT_NAME=$(basename "$0")
sudo rm -- "$SCRIPT_NAME"

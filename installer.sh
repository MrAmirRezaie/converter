#!/bin/bash

# Detect package manager
if command -v apt &> /dev/null; then
    PKG_MANAGER="apt"
    INSTALL_CMD="sudo apt update && sudo apt install -y"
elif command -v dnf &> /dev/null; then
    PKG_MANAGER="dnf"
    INSTALL_CMD="sudo dnf install -y"
elif command -v yum &> /dev/null; then
    PKG_MANAGER="yum"
    INSTALL_CMD="sudo yum install -y"
elif command -v pacman &> /dev/null; then
    PKG_MANAGER="pacman"
    INSTALL_CMD="sudo pacman -Syu --noconfirm"
else
    echo "Unsupported package manager. Install dependencies manually."
    exit 1
fi

# Install dependencies
$INSTALL_CMD python3 python3-pip ffmpeg wkhtmltopdf

# Upgrade pip and install required Python packages
python3 -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "Failed to upgrade pip. Trying alternative method..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    rm get-pip.py
fi

pip3 install --no-cache-dir pillow markdown2 pydub pdfkit pypdf2 docx2pdf pandas gtts moviepy imgkit comtypes
if [ $? -ne 0 ]; then
    echo "Error installing Python packages. Please check your Python and pip installation."
    exit 1
fi

# Make script executable
chmod +x converter.py

echo "Installation completed successfully! You can now run ./converter.py"
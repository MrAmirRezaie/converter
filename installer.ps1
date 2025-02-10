Write-Host "Checking for Python installation..."
$pythonCheck = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCheck) {
    Write-Host "Python not found. Installing..."
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe" -OutFile "python-installer.exe"
    Start-Process -FilePath "python-installer.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item "python-installer.exe"
}

Write-Host "Upgrading pip..."
python -m ensurepip --default-pip
python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to upgrade pip. Attempting alternative method..."
    Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "get-pip.py"
    python get-pip.py
    Remove-Item "get-pip.py"
}

Write-Host "Installing required Python packages..."
$packages = "pillow", "markdown2", "pydub", "pdfkit", "pypdf2", "docx2pdf", "pandas", "gtts", "moviepy", "imgkit", "comtypes"
foreach ($package in $packages) {
    python -m pip install --no-cache-dir $package
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install $package. Please check your Python and pip installation."
        exit 1
    }
}

Write-Host "Installation completed successfully! Run the script using: python converter.py"
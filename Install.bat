cd %SystemDrive%\python34
pip install -r "%~dp0\requirements.txt"
pip install virtualenv
"%~dp0\needed_with_python_install_these\install.bat"

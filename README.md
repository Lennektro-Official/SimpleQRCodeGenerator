# SimpleQRCodeGenerator

## Overview
This is just a little program that allows you to generate QR-Codes using Python. 
>**Note:** The temp.png is needed and will be generated in the current directory the program is executed in.

## References
**Used Libraries:**
>Pillow: https://pypi.org/project/Pillow/  
>QRCode: https://pypi.org/project/qrcode/

If you don't want to install the modules you can use the executable that was created
using Auto-Py-To-Exe. And don't worry, it's a false positive virus, a common problem with
Auto-Py-To-Exe.
>Auto-Py-To-Exe: https://pypi.org/project/auto-py-to-exe/

## Install
**Windows:**

Setup:
```
git clone https://github.com/Lennektro-Official/SimpleQRCodeGenerator
cd SimpleQRCodeGenerator
pip install -r requirements.txt
```
Run the programm:
```
python qrcode_gen.py
```


**Linux:**

Setup:
```
sudo apt update
sudo apt-get install python3-tk
git clone https://github.com/Lennektro-Official/SimpleQRCodeGenerator
cd SimpleQRCodeGenerator
sudo pip3 install -r requirements.txt
```
Run the programm:
```
sudo python3 qrcode_gen.py
```

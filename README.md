# Altair-MADIZ SRIM Calculation
This repo uses pysrim to calculate the particle energy required to pass through the MADIZ instrument body
## Installation
### Linux
#### Reqs
* Wine
* Git
* Python >= 3.8
#### Algoritm
1. Clone repo ```git clone https://github.com/stifild/Altair```
2. Change directory to Altair ```cd ./Altair```
3. Create virtual enviroment ```python3 -m venv venv```
4. Activate enviroment ```source ./venv/bin/activate```
5. Install requirements ```pip install -r reqs.txt```
6. Fix pysrim library
   You need to change method from load to safe_load in 10 line at ./venv/lib64/python3.X/site-packages/srim/core/elementdb.py
7. Install reqs dlls in wine ```wine ./tmp/srim/SRIM-Setup/sr-s.bat```
#### Easy install
```shell
python3 -m venv venv && source ./venv/bin/activate && pip install -r reqs.txt && wine ./tmp/srim/SRIM-Setup/sr-s.bat
```
And do 6th point of algoritm
##### That`s all! Now you can change config file and run TRIM

### Windows


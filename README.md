# ukr

## usage

1. Clone this repo wherever you'd like it to run.
```
git clone https://github.com/AEAMcNett/ukr.git
```

2. Create a virtual environment using your favorite method. To do so using the `venv` module and create a virtual environment within your project directory:
```
python3 -m venv venv
```

3. Activate your virtual environment. If you followed the instructions above using the `venv` module, execute the following command in your project directory:
```
source venv/bin/activate
```


4. Install the requirements:
```
pip install -r requirements.txt
```

5. Mark the script as executable:
```
chmod +x ukr.py
```

6. Run the script from its directory, supplying the filename (including extension) for the image you want to alter as the sole argument. The image file must be in the script directory.
```
./ukr.py <filename.jpg>
```

## example

From: ![A picture of Kamianets-Podilskyi Castle from Wikipedia](https://github.com/AEAMcNett/ukr/blob/main/kpc.jpg)

To: ![A picture of Kamianets-Podilskyi Castle altered by this script](https://github.com/AEAMcNett/ukr/blob/main/ukr_kpc.png)
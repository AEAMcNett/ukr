# ukr

## usage

1. Create a virtual environment using your favorite method. To do so using the `venv` module:
```
python3 -m venv /path/to/new/virtual/environment
```

2. Install the requirements:
```
pip install -r requirements.txt
```

3. Mark the script as executable:
```
chmod +x ukr.py
```

4. Run the script from its directory, supplying the filename (including extension) for the image you want to alter as the sole argument. The image file must be in the script directory.
```
./ukr.py <filename.jpg>
```

## example

- From: ~[A picture of Kamianets-Podilskyi Castle from Wikipedia](https://github.com/AEAMcNett/ukr/blob/main/kpc.jpg)
- To: ~[A picture of Kamianets-Podilskyi Castle altered by this script](https://github.com/AEAMcNett/ukr/blob/main/ukr_kpc.png)
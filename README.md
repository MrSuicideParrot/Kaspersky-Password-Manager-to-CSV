# Kaspersky Password Manager to CSV

When you want to give up from Kaspersky Password Manager, you have a problem. You can export your passwords, but they are not on a standard format. This program is your solution, a converter from the Kaspersky Password Manager export format to a CSV.

## Features
This program is capable of convert the passwords from the *Websites* and *Applications* section. 
The *Notes* section is not exported.

## How to use it
```
$ python3 KPM_to_CSV.py --help
usage: KPM_to_CSV.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE]

Kaspersky Password Manager conveter to CSV

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Kaspersky Password Manager export file
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Custom CSV file name
```


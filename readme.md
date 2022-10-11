# Plain Text to Braille

This simple Python3 project converts plain text (from command line or text file) to PDF Braille format.

The result is composed by 2 output files (one left to right writted and another right to left writted).

This project uses a third party font family Braille1. Its readme.txt and lisezmoi.txt are included. 

## Required libraries:
- PyPDF2
- FPDF

## Usage

Convert stdin input to Braille PDF (press 2 times <Return> to finish)
```
python3 main.py output.pdf
```

or


Convert a plain text file do Braille PDF.
```
python3 main.py input.txt output.pdf
```

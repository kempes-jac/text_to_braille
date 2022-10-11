from fpdf import FPDF
import PyPDF2
import textwrap
import sys

LINE_WIDTH = 30
FONT_SIZE=20

def pdfWithFont(texts,font,fileName):
  pdf = FPDF()

  pdf.add_font('Braille1', '', 'BRAILLE1.ttf', uni=True)
  pdf.add_page()
  pdf.set_font(font,size=FONT_SIZE)
  for text in texts:
    pdf.cell(200, 10, txt = text,
            ln = 1, align = 'J')
  pdf.output(fileName)  

def flipFile(fileName, outputFileName):
  pdf_in = open(fileName, 'rb')
  pdf_reader = PyPDF2.PdfFileReader(pdf_in)
  pdf_writer = PyPDF2.PdfFileWriter()

  for pagenum in range(pdf_reader.numPages):
      page = pdf_reader.getPage(pagenum)
      box = page.mediaBox
      page.addTransformation([-1,0,0,1,box[2],0])
      pdf_writer.addPage(page)

  pdf_out = open(outputFileName, 'wb')
  pdf_writer.write(pdf_out)
  pdf_out.close()
  pdf_in.close()


def convertFile(inputFile,pdfFileName):
  tmpFileName = 'tmp' + pdfFileName
  arial = 'arial'+pdfFileName
  flipedArial = 'arial_f'+pdfFileName
    
  file1 = open(inputFile, 'r')
  Lines = file1.readlines()
  
  text=[]
  for line in Lines:
    a = textwrap.wrap(line,width=LINE_WIDTH)
    text = text + a

  
  # pdfWithFont(text,'Arial',arial)
  pdfWithFont(text,'Braille1',tmpFileName)

  flipFile(arial,flipedArial)
  flipFile(tmpFileName,pdfFileName)

def convert(pdfFileName):
  tmpFileName = 'tmp' + pdfFileName
  arial = 'arial'+pdfFileName
  flipedArial = 'arial_f'+pdfFileName

  def captura():
    lines=[]

    for line in sys.stdin:
      if '' == line.rstrip():
        break
      lines = lines + textwrap.wrap(line,width=LINE_WIDTH)
    return lines

  text = captura()
  
  # pdfWithFont(text,'Arial',arial)
  pdfWithFont(text,'Braille1',tmpFileName)

  flipFile(arial,flipedArial)
  flipFile(tmpFileName,pdfFileName)


import sys

from lib.pdf import convert, convertFile
import sys

def printUsage():
  print("Para converter um arquivo texto em um PDF use:")
  print("  python3 main.py entrada.txt saida.pdf")
  print("")
  print("Onde:")
  print("- entrada.txt é o nome do arquivo texto com extensão .txt")
  print("- saida.pdf é o nome do arquivo PDF a ser gerado")
  print("")
  print("")
  print("Para receber uma entrada de texto e gerar um PDF use:")
  print("  pyhon3 main.py saida.pdf")
  print("")
  print("Onde:")
  print("- saida.pdf é o nome do arquivo PDF a ser gerado")
  print("")
  print("")

argsSize = len(sys.argv)
if(argsSize!=2 and argsSize!=3):
  printUsage()
else:
  if(argsSize==2):
    if(not sys.argv[1][-4:]=='.pdf'):
      printUsage()
    else:
      convert(sys.argv[1])
  else:
    if(not (sys.argv[1][-4:]=='.txt' and sys.argv[2][-4:]=='.pdf')):
      printUsage()
    else:
      convertFile(sys.argv[1],sys.argv[2])



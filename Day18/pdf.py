import PyPDF2

with open('DSML.pdf','r') as file:
    reader=PyPDF2.PDFReader(file)
    print(reader.numPages)
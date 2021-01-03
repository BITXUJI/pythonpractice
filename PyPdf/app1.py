import PyPDF2
merger = PyPDF2.PdfFileMerger()
file_names = ["pdf1.pdf", "rotated.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("pdf2.pdf")

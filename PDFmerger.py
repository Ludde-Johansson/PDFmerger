from PyPDF2 import PdfReader, PdfWriter
import os

# Function to merge PDFs
def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for i in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[i])

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

# Specify the PDFs to merge
path1 = 'C:\\Users\\LudvigLillebyJohanss\\Documents\\FrontlineOktober.pdf'
path2 = 'C:\\Users\\LudvigLillebyJohanss\\Documents\\FrontlineNovember.pdf'
path3 = 'C:\\Users\\LudvigLillebyJohanss\\Documents\\verketKlipp.pdf'
path4 = 'C:\\Users\\LudvigLillebyJohanss\\Documents\\ArkoseMndskort.pdf'
pdfs = [path1, path2, path3, path4]

output_filename = 'merged.pdf'

# Combine the directory of the first PDF with the new output file name
output_path = os.path.join(os.path.dirname(path1), output_filename)

# Call the function with the list of PDFs to merge and the desired output file name
merge_pdfs(pdfs, output_path)
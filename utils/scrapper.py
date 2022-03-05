import argparse
import re
import PyPDF2

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("output_folder", default=".", )
args = parser.parse_args()

folder = args.output_folder + "/"

print(f"Parsing file: {args.file} to folder: {folder}")
pdf_file=open(args.file,'rb')
 
pdf_reader=PyPDF2.PdfFileReader(pdf_file)
full_text = ""
for i in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(i)
    full_text += page.extractText()

print(f"Total pages:{i}")

head_clean = re.sub("^.*?Artículo", "Artículo ", full_text, count=2, flags=re.DOTALL)
clean_text = re.sub("Sin otro particular, .*", "", head_clean, flags=re.DOTALL)

for article in clean_text.split("Artículo "):
    article = article.strip()
    weight = re.match("(\d*)", article).expand(r"\1")
    
    article = re.sub("^\d*", "", article).strip(".- \n")
    article = article.strip(".- \n")
    article = re.sub("\d+\Z", "", article).strip(" \n")
    print (article)
    title = article.split(".")[0]
    print(title)
    if not weight:
        continue
    
    with open (folder+weight+".md","w") as file:
        file.write("---\n")
        file.write(f"title: \"Art. {weight}\"\n")
        file.write(f"long-title: \"{title}\"\n")
        file.write(f"weight: {weight}\n")
        file.write("type: \"articulo\"\n")
        file.write("bookHidden: true\n")
        file.write("---\n")
        file.write(article)
        
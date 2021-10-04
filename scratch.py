from PyPDF2 import PdfFileReader, PdfFileWriter
import re
import pdfplumber
import pandas as pd
from collections import namedtuple
from io import StringIO
from collections import namedtuple
import os

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

Line = namedtuple('Line', 'Country Title C1 C2 C3 C4 C5 C6')

column0 = re.compile(r'(B[A-Z]*\d{3}\.?\d?\s?\(P.*:)(.*)(\(.*)?')
title0 = re.compile(r'^(\d+)\s?(-?\s?\d*.*)\s?(Issues|Design|Cheques)')
title1 = re.compile(r'^(Cargill Cotton Group) (2004 Bearer Cheque Issues)')
paragraph2 = re.compile(r'((Violet-red|Greenish|Multicolor|Reddish|Brownish|Lilac|Yellow|Mauve|Red|Pink|Grayish|Green|Blue|Brown|Purple|Gray|Dark|Black|Rust|Olive|Violet|Teal|Gold|Tan|Orange|Light)?(.*)?Front(\s\(vertical\))?:(.*\n){4})')
VGG = re.compile(r'VG')
VFF = re.compile(r'VF')
UNCC = re.compile(r'UNC')


for path, dirs, files in os.walk("C:\\Users\\aatis\\OneDrive\\Desktop\\PDF_crash"):
    for f in files:
        filename = os.path.join(path, f)

        C4 = None
        C5 = None
        C6 = None
        listt = []
        lines = []
        count2 = 0
        output_string = StringIO()
        with open(filename, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            count = 0
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        Country = (os.path.splitext(os.path.basename(filename))[0])
        text = output_string.getvalue()
        for line in text.split('\n'):
            #             print(line)
            col0 = column0.finditer(line)
            titl_1 = title1.search(line)
            titl_0 = title0.search(line)
            VG_0 = VGG.search(line)
            VF_0 = VFF.search(line)
            UNC_0 = UNCC.search(line)

            if VG_0:
                C4 = VG_0.group()
            if VF_0:
                C5 = VF_0.group()
            if UNC_0:
                C6 = UNC_0.group()

            if titl_0:
                Title = titl_0.group()
            elif titl_1:
                Title = titl_1.group(2)

            for match in col0:
                C1 = match.group(1)
                C2 = match.group(2)
                C3 = match.group(3)
                lines.append(Line(Country, Title, C1, C2, C3, C4, C5, C6))

        para2 = paragraph2.finditer(text)
        for match in para2:
            Paragraph = match.group()
            listt.append(Paragraph)
            count2 = count2 +1
        #         print(count2)

        df = pd.DataFrame(lines)
        #         df.drop_duplicates(inplace = True)
        #         df = df.sort_values('C1')

        print(len(listt))
        print("***************************************************************************************************")

        empty_lines = []
        Country = None
        Title = None
        C1 = None
        C2 = None
        C3 = None
        C4 = None
        C5 = None
        C6 = None

        if len(df.index) == len(listt):
            df['Paragraph'] = listt[:]
        elif len(df.index) < len(listt):
            count_diff = len(listt) - len(df.index)
            for i in range(count_diff):
                empty_lines.append(Line(Country, Title, C1, C2, C3, C4, C5, C6))
            empty_df = pd.DataFrame(empty_lines)
            df = df.append(empty_df)
            df['Paragraph'] = listt[:]
        else:
            count_diff = len(df.index) - len(listt)
            for i in range(count_diff):
                listt.append(None)
            df['Paragraph'] = listt[:]
        print(df.head())

#         df.to_csv('pdf_Y.csv', mode = 'a', header = False)
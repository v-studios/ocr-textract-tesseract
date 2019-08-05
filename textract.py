#!/usr/bin/env python3
"""Demonstrate how to call AWS Textract synchronously.

Textract can OCR a single page if called synchronously, and is reasonably
quick.

(It can also do multipage docs up to 3000 pages asynchronously with SNS
notificatino but that's not the goal of this demo.)
"""

import sys

import boto3

from pdf2jpg import extract_jpg_from_pdf


def textract_text(pdf_path):
    """Use AWS Textract to extract unstructured text."""
    print('# Extracting JPG from PDF...')
    img = extract_jpg_from_pdf(pdf_path)
    textract = boto3.client('textract')
    print('# Getting text from image with textract...')
    res = textract.detect_document_text(Document={'Bytes': img})
    txt = ''
    print('# Getting text from OCR blocks and lines...')
    for block in res['Blocks']:
        btype = block['BlockType']
        if btype == 'LINE':
            txt += '\n' + block['Text']
    return txt


def main():
    print(textract_text(sys.argv[1]))


if __name__ == '__main__':
    main()

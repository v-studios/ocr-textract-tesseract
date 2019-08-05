===============================
 README ocr-tesseract-textract
===============================


Goal
====

This code shows how easy it is to use AWS Textract to synchronously
OCR a single page. By "synchonous", we mean we submit a page to
Textract and wait for the result.

Operation
=========

Textract expects an image format, JPG or PNG.  Scanned PDF docs have
the image embedded in JPG format, so we first extract that binary data
then send it to Textract. We parse the BLOCKs and LINEs and build the
text output. This is then printed.

Creating a "scanned" image
==========================

To get a fake "scan" PDF, I created a one-page doc of text, converted
it to a JPG, then converted that to a PDF.

Since our original text is something we know, we should be able to
compare the accuracy of our extracted text with the original to
determine accuracy. That's for later. 

Invoke
======

Invoke like::

  ./textract.py palefire.jpg.pdf


Developer environment setup
===========================

I used ``pyenv`` to select python version 3.7.2 then created and
activated a virtual environment, then installed ``boto3``::

  pyenv local 3.7.2
  python -mvenv .venv
  pip install -r requirements.txt

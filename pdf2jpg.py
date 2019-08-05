#!/usr/bin/env python3
# Adapted from https://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
"""Extract jpg's from pdf's. Quick and dirty."""

import sys

STARTMARK = b"\xff\xd8"
STARTFIX = 0
ENDMARK = b"\xff\xd9"
ENDFIX = 2


def extract_jpg_from_pdf(pdf_path):
    """Extract JPG from single-page PDF scan, return as bytes.

    No coversion involved so faster than GhostScript or ImageMagick,
    and also no loss due to conversion.

    This mutation of Batchelder's work only handles a single page.

    Only works with scanned PDF images, not text PDFs.
    May not always be reliable
    Past peformance is no guarantee of future results.
    Use only under a doctor's supervision.
    """
    pdf = open(pdf_path, "rb").read()
    i = 0
    while True:
        istream = pdf.find(b"stream", i)
        if istream < 0:
            break
        istart = pdf.find(STARTMARK, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find(b"endstream", istart)
        if iend < 0:
            raise Exception("Did not find end of stream!")
        iend = pdf.find(ENDMARK, iend - 20)
        if iend < 0:
            raise Exception("Did not find end of JPG!")
        istart += STARTFIX
        iend += ENDFIX
        # print("JPG from %d to %d" % (istart, iend))
        jpg = pdf[istart:iend]
        return jpg
    raise Exception(f"Could not extract JPG from PDF={pdf_path}")


def main():
    """Test it out."""
    jpg = extract_jpg_from_pdf(sys.argv[1])
    jpgfile = open("jpgextracted.jpg", "wb")
    jpgfile.write(jpg)
    jpgfile.close()


if __name__ == "__main__":
    main()

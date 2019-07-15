# About

This is a simple wrapper for img2pdf packages written using Python. It allows converting all images in a folder into one pdf file.

https://pypi.org/project/img2pdf/

# Usage

Install required packages 

    pip install -r requirements.txt

Create wrapper object

    from img2pdf_wrapper import Img2PdfWrapper
    wrapper = Img2PdfWrapper()

Specified path to images folder, path to output pdf file and run conversion method. Make sure that images folder only contains images.

    input_folder = 'C:/Image/'
    output_folder = 'C:/Output/File.pdf'
    wrapper.do_convert(input_folder, output_folder)

Alternatively, you can run img2pdf_wrapper.py script directly from commandline

    python img2pdf_wrapper.py --input="C:/Image/" --output="C:/Output/File.pdf"


# License

MIT License

https://opensource.org/licenses/MIT
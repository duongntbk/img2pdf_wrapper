# -*- coding: utf-8 -*-

'''
A simple wrapper for img2pdf, allows converting all images in a folder into one pdf file.
'''

import argparse
import os

import img2pdf


class Img2PdfWrapper:
    '''
    Wrapper class for img2pdf.
    '''

    def load_img_list(self, img_path):
        '''
        Get and add the full path of all files in input folder to list.
        '''

        img_list = []
        try:
            for img in os.listdir(img_path):
                img_list.append(os.path.join(img_path, img))
        except Exception as e:
            print('An error occurred while reading images from input folder: {0}'.format(format(e)))
            raise

        return img_list

    def do_convert(self, img_path, output_path):
        '''
        Convert all images in input folder into one pdf file.
        It is assumed that all files in input folder are image.
        '''

        try:
            img_list = self.load_img_list(img_path)
            pdf_bytes = img2pdf.convert(img_list)
            
            with open(output_path, 'wb') as f:
                f.write(pdf_bytes)

        except Exception as e:
            print('An error occurred while coverting images to pdf: {0}'.format(format(e)))
            raise

def main():
    '''
    Entry point when executing from commandline.
    '''

    parser=argparse.ArgumentParser()
    parser.add_argument('--input', help='Path to images folder (required).')
    parser.add_argument('--output', help='Folder export to pdf file into (required).')
    args=parser.parse_args()

    # Verify that both path to image folder and path to export pdf file are specified
    if not args.input or not args.output:
        help_msg = '\n' + \
            'Input parameter is incorrect\n' + \
            'Display help: \'python converter.py -h\''
        print(help_msg)
        return

    print('Please wait...')
    try:
        wrapper = Img2PdfWrapper()
        wrapper.do_convert(args.input, args.output)
        print('Done.')
    except Exception:
        print('Conversion failed.')

if __name__ == '__main__':
    main()

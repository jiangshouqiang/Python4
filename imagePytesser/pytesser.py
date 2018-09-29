"""OCR in Python using the Tesseract engine from Google
http://code.google.com/p/pytesser/
by Michael J.T. O'Kelly
V 0.0.1, 3/10/07"""

from PIL import Image
import subprocess
import utils

tesseract_exe_name = 'tesseract' # Name of executable to be called at command line
scratch_image_name = "temp.bmp" # This file must be .bmp or other Tesseract-compatible format
scratch_text_name_root = "temp" # Leave out the .txt extension
cleanup_scratch_flag = False  # Temporary files cleaned up after OCR operation

def call_tesseract(input_filename, output_filename):
    """Calls external tesseract.exe on input file (restrictions on types),
    outputting output_filename+'txt'"""
    args = [tesseract_exe_name, input_filename, output_filename]
    proc = subprocess.Popen(args)
    retcode = proc.wait()
    if retcode!=0:
        raise("errors")

def image_to_string(im, cleanup = cleanup_scratch_flag):
    """Converts im to file, applies tesseract, and fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    try:
        utils.image_to_scratch(im, scratch_image_name)
        call_tesseract(scratch_image_name, scratch_text_name_root)
        text = utils.retrieve_text(scratch_text_name_root)
    finally:
        if cleanup:
            utils.perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text

def image_file_to_string(filename, cleanup = cleanup_scratch_flag, graceful_errors=True):
    """Applies tesseract to filename; or, if image is incompatible and graceful_errors=True,
    converts to compatible format and then applies tesseract.  Fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    try:
        try:
            call_tesseract(filename, scratch_text_name_root)
            text = utils.retrieve_text(scratch_text_name_root)
        except Exception as e:
            if graceful_errors:
                im = image.open(filename)
                text = image_to_string(im, cleanup)
            else:
                raise
    finally:
        if cleanup:
            utils.perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text


if __name__=='__main__':
    im = Image.open('test.png')
    text = image_to_string(im)
    print(text)
    try:
        text = image_file_to_string('fnord.tif', graceful_errors=False)
    except Exception as e:
        print("fnord.tif is incompatible filetype.  Try graceful_errors=True")
        print(e)
    text = image_file_to_string('fnord.tif', graceful_errors=True)
    print("fnord.tif contents:", text)
    text = image_file_to_string('fonts_test.png', graceful_errors=True)
    print(text)
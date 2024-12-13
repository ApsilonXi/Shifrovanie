import chardet
import os
import tempfile

CONFIDENCE_THRESHOLD = 0.8 # minimum confidence to transcode the file

def convert_to_utf8(filename):
    with open(filename, 'rb') as f:
        content_bytes = f.read()

    detected = chardet.detect(content_bytes)
    encoding = detected['encoding']
    confidence = detected['confidence']

    print(f"{filename}: detected as {encoding} with confidence {confidence}.")

    if confidence < CONFIDENCE_THRESHOLD:
        print(f"{filename} skipped.")
        return

    content_text = content_bytes.decode(encoding)

    with tempfile.NamedTemporaryFile(mode = 'w', dir = os.path.dirname(filename), encoding = 'utf-8', delete = False) as f:
        f.write(content_text)

    os.replace(f.name, filename)

# Example usage:
convert_to_utf8('lab2.2/output12.txt')
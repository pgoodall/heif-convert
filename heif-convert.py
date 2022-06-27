import argparse
from PIL import Image
import pillow_heif

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Specify the path to the file you want to convert")
args = parser.parse_args()

heif_file = pillow_heif.read_heif(args.file)
image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw",
)

image.save("./picture_name.jpg", format("JPEG"))

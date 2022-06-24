from PIL import Image
import pillow_heif

heif_file = pillow_heif.read_heif("IMG_2084.HEIC")
image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw",
)

image.save("./picture_name.jpg", format("JPEG"))

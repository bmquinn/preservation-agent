from smolagents import Tool

from PIL import Image

from PIL.ExifTags import TAGS


def exif_obj_to_dict(exif_obj):
    exif_dict = {}
    for tag_id, value in exif_obj.items():
        tag = TAGS.get(tag_id, tag_id)

        # Handle bytes
        if isinstance(value, bytes):
            try:
                value = value.decode()
            except UnicodeDecodeError:
                value = value.hex()

        exif_dict[tag] = value

    return exif_dict


class ImageTool(Tool):
    name = "image_data"
    description = """Extracts the technical metadata from an image."""
    inputs = {"path": {"type": "string", "description": "The path to the image."}}
    output_type = "any"

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def forward(self, path: str) -> str:
        with Image.open(path) as img:
            return {"exif": exif_obj_to_dict(img._exif)}

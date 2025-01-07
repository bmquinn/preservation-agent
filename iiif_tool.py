from smolagents import Tool

from piffle.presentation import IIIFPresentation


class IIIFTool(Tool):
    name = "iiif"
    description = """Fetches a IIIF manifest for a given URL. Presents the data in a structured format to the user."""
    inputs = {"url": {"type": "string", "description": "The URL to the IIIF manifest."}}
    output_type = "any"

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def forward(self, url: str) -> str:
        print(f"Fetching IIIF manifest for {url}")
        manifest = IIIFPresentation.from_url(url)
        print(f"Manifest: {manifest}")
        return manifest

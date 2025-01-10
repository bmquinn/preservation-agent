import hashlib
from smolagents import Tool


class ChecksumTool(Tool):
    name = "checksum"
    description = """Generates or verifies checksums (e.g., MD5, SHA-256) for a given file to ensure data integrity."""
    inputs = {
        "path": {"type": "string", "description": "The path to the file."},
        "algorithm": {
            "type": "string",
            "description": "The checksum algorithm to use (e.g., md5, sha256).",
            "default": "sha256",
            "nullable": True,  # Added nullable field for optional parameter
        },
        "verify": {
            "type": "boolean",
            "description": "Whether to verify the checksum against a provided value.",
            "default": False,
            "nullable": True,  # Added nullable field for optional parameter
        },
        "expected_checksum": {
            "type": "string",
            "description": "The expected checksum value for verification.",
            "required_if": {"verify": True},
            "nullable": True,  # Added nullable field for optional parameter
        },
    }
    output_type = "any"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def forward(
        self,
        path: str,
        algorithm: str = "sha256",
        verify: bool = False,
        expected_checksum: str = None,
    ) -> str:
        hash_func = getattr(hashlib, algorithm, None)
        if not hash_func:
            raise ValueError(f"Unsupported checksum algorithm: {algorithm}")

        hash_obj = hash_func()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        computed_checksum = hash_obj.hexdigest()

        if verify:
            if not expected_checksum:
                raise ValueError("Expected checksum must be provided for verification.")
            is_valid = computed_checksum.lower() == expected_checksum.lower()
            return {"computed_checksum": computed_checksum, "is_valid": is_valid}
        else:
            return {"computed_checksum": computed_checksum}

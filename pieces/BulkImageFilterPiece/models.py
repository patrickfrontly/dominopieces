from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class OutputTypeType(str, Enum):
    """
    Output type for the result image(s)
    """

    file = "file"
    base64_string = "base64_string"
    both = "both"


class InputModel(BaseModel):
    input_images: List[str] = Field(
        description="Input images. Each item should be either a path to a file, or a base64 encoded string.",
        json_schema_extra={
            "from_upstream": "always",
        },
    )
    sepia: bool = Field(default=False, description="Apply sepia effect.")
    black_and_white: bool = Field(default=False, description="Apply black and white effect.")
    brightness: bool = Field(default=False, description="Apply brightness effect.")
    darkness: bool = Field(default=False, description="Apply darkness effect.")
    contrast: bool = Field(default=False, description="Apply contrast effect.")
    red: bool = Field(default=False, description="Apply red effect.")
    green: bool = Field(default=False, description="Apply green effect.")
    blue: bool = Field(default=False, description="Apply blue effect.")
    cool: bool = Field(default=False, description="Apply cool effect.")
    warm: bool = Field(default=False, description="Apply warm effect.")
    output_type: OutputTypeType = Field(
        default=OutputTypeType.both,
        description="Format of the output images. Options are: `file`, `base64_string`, `both`.",
    )


class OutputModel(BaseModel):
    image_base64_strings: List[str] = Field(
        default_factory=list,
        description="Base64 encoded strings of the output images (one per input).",
    )
    image_file_paths: List[str] = Field(
        default_factory=list,
        description="Paths to the output image files (one per input).",
    )



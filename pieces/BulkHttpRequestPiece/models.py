from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MethodTypes(str, Enum):
    GET = "GET"


class InputModel(BaseModel):
    urls_csv: str = Field(
        description="Comma-separated list of URLs to request (e.g. 'https://a.png,https://b.png')."
    )
    method: MethodTypes = Field(
        default=MethodTypes.GET,
        description="HTTP method to use. BulkHttpRequest currently supports GET only.",
    )
    bearer_token: Optional[str] = Field(
        default=None,
        description="Bearer token to use for authentication (applied to all requests).",
    )


class OutputModel(BaseModel):
    base64_bytes_data_list: List[str] = Field(
        description="Array of output payloads as base64 encoded strings (one per URL, in the same order)."
    )



from domino.testing import piece_dry_run
from io import BytesIO
from pathlib import Path

import base64
from PIL import Image


def _load_test_image_base64() -> str:
    img_path = str(Path(__file__).parents[1] / "PFImageFilterPiece" / "test_image.png")
    img = Image.open(img_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def test_bulkimagefilterpiece_base64_output():
    base64_image = _load_test_image_base64()
    input_data = dict(
        input_images=[base64_image, base64_image],
        sepia=True,
        blue=True,
        output_type="base64_string",
    )
    piece_output = piece_dry_run(
        piece_name="BulkImageFilterPiece",
        input_data=input_data,
    )
    assert piece_output is not None
    assert isinstance(piece_output.get("image_base64_strings"), list)
    assert len(piece_output["image_base64_strings"]) == 2
    assert all(isinstance(s, str) and len(s) > 0 for s in piece_output["image_base64_strings"])


def test_bulk_workflow_http_then_filter():
    # 2-step workflow: bulk fetch -> bulk filter
    req_out = piece_dry_run(
        piece_name="BulkHttpRequestPiece",
        input_data={
            "urls_csv": "https://httpbin.org/image/png,https://httpbin.org/image/png",
            "method": "GET",
        },
    )

    filt_out = piece_dry_run(
        piece_name="BulkImageFilterPiece",
        input_data={
            "input_images": req_out["base64_bytes_data_list"],
            "sepia": True,
            "output_type": "base64_string",
        },
    )
    assert len(filt_out["image_base64_strings"]) == 2



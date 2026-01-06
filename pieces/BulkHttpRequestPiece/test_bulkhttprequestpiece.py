from domino.testing import piece_dry_run
import base64


def test_bulkhttprequest_get_images():
    input_data = {
        "urls_csv": "https://httpbin.org/image/png,https://httpbin.org/image/jpeg",
        "method": "GET",
    }
    piece_output = piece_dry_run(
        piece_name="BulkHttpRequestPiece",
        input_data=input_data,
    )
    assert isinstance(piece_output.get("base64_bytes_data_list"), list)
    assert len(piece_output["base64_bytes_data_list"]) == 2

    decoded_0 = base64.b64decode(piece_output["base64_bytes_data_list"][0].encode("utf-8"))
    decoded_1 = base64.b64decode(piece_output["base64_bytes_data_list"][1].encode("utf-8"))
    assert len(decoded_0) > 0
    assert len(decoded_1) > 0



import base64

import requests
from domino.base_piece import BasePiece

from .models import InputModel, OutputModel


class BulkHttpRequestPiece(BasePiece):
    def piece_function(self, input_data: InputModel):
        if input_data.method != "GET":
            raise Exception(f"Unsupported HTTP method for bulk requests: {input_data.method}")

        urls = [u.strip() for u in input_data.urls_csv.split(",")]
        urls = [u for u in urls if u]
        if not urls:
            raise ValueError("No URLs provided. Please pass a comma-separated list in urls_csv.")

        headers = {}
        if input_data.bearer_token:
            headers["Authorization"] = f"Bearer {input_data.bearer_token}"

        session = requests.Session()
        base64_list = []
        for url in urls:
            try:
                resp = session.get(url, headers=headers)
                resp.raise_for_status()
            except requests.RequestException as e:
                raise Exception(f"HTTP request error for url='{url}': {e}")

            base64_list.append(base64.b64encode(resp.content).decode("utf-8"))

        return OutputModel(base64_bytes_data_list=base64_list)



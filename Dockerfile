FROM ghcr.io/tauffer-consulting/domino-base-piece:latest

# Bake the repository into the image exactly how Domino expects it
COPY config.toml domino/pieces_repository/
COPY pieces domino/pieces_repository/pieces
COPY .domino domino/pieces_repository/.domino
COPY dependencies/requirements_0.txt domino/pieces_repository/dependencies/

RUN pip install --no-cache-dir -r domino/pieces_repository/dependencies/requirements_0.txt



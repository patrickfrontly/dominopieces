# Domino Pieces (patrickfrontly/dominopieces)

This is a minimal Domino Pieces repository containing:

- **PFHttpRequestPiece**: Make an HTTP request to a URL and return the response bytes as base64.
- **PFImageFilterPiece**: Apply simple image filters and return image output as file/base64.
- **BulkHttpRequestPiece**: Fetch multiple URLs (comma-separated) and return an array of base64 response bytes.
- **BulkImageFilterPiece**: Apply the same image filters, but to an array of images (base64 strings or file paths).

## Manual publish (no GitHub Actions)

Domino runs Pieces from a **Docker image** referenced in `.domino/dependencies_map.json`.
For version `0.0.4` this repository expects the image:

- `ghcr.io/patrickfrontly/dominopieces:0.0.4-group0`

### 1) Build & push the image to GHCR

Prereqs:

- Docker Desktop running
- A GitHub Personal Access Token (PAT) with **write:packages** (and **read:packages** is recommended)

From the repo root:

```bash
docker login ghcr.io -u patrickfrontly
docker build -t ghcr.io/patrickfrontly/dominopieces:0.0.4-group0 .
docker push ghcr.io/patrickfrontly/dominopieces:0.0.4-group0
```

### 2) Commit and tag the repo

Domino selects repository versions via **git tags**.

```bash
git add config.toml .domino Dockerfile pieces dependencies README.md
git commit -m "Release 0.0.4"
git push

git tag 0.0.4
git push --tags
```

### 3) Add the repository in Domino

In the UI (Workspace Settings → Pieces Repositories), add:

- `https://github.com/patrickfrontly/dominopieces`

Select version:

- `0.0.4`

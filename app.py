from pathlib import Path

from flask import Flask, abort, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
PAGES_DIR = PUBLIC_DIR / "pages"

app = Flask(__name__, static_folder=str(PUBLIC_DIR), static_url_path="/public")


@app.get("/")
def index():
    return send_from_directory(PAGES_DIR / "main", "welcome.html")


@app.get("/favicon.ico")
def favicon():
    return send_from_directory(PUBLIC_DIR / "assets" / "icons", "favicon.ico")


@app.get("/assets/<path:asset_path>")
def assets(asset_path: str):
    return send_from_directory(PUBLIC_DIR / "assets", asset_path)


@app.get("/styles/<path:style_path>")
def styles(style_path: str):
    return send_from_directory(PUBLIC_DIR / "styles", style_path)


@app.get("/scripts/<path:script_path>")
def scripts(script_path: str):
    return send_from_directory(BASE_DIR / "scripts", script_path)


@app.get("/pages/<section>/<page>")
def pages(section: str, page: str):
    page_path = PAGES_DIR / section / page
    if not page_path.exists() or page_path.suffix != ".html":
        abort(404)
    return send_from_directory(page_path.parent, page_path.name)


if __name__ == "__main__":
    app.run(debug=True)

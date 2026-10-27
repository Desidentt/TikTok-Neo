import os
import base64
valid_png_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
valid_png_bytes = base64.b64decode(valid_png_base64)
def fix_invalid_pngs(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        if f.read(8) != b'\x89PNG\r\n\x1a\n':
                            with open(filepath, 'wb') as wf: wf.write(valid_png_bytes)
                except Exception: pass
if __name__ == "__main__": fix_invalid_pngs("tiktok_workspace/res")

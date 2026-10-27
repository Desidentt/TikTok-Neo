import re, os
def fix_manifest(workspace_dir):
    manifest_path = os.path.join(workspace_dir, "AndroidManifest.xml")
    if not os.path.exists(manifest_path): return
    with open(manifest_path, 'r', encoding='utf-8') as f: content = f.read()
    content = re.sub(r'\s+[\w:]+="@\d+"', '', content)
    with open(manifest_path, 'w', encoding='utf-8') as f: f.write(content)
if __name__ == "__main__": fix_manifest("tiktok_workspace")

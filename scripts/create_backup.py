import zipfile
import os

def make_backup(out_path='..\\FabianProject-backup.zip', exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = {'.venv', 'Models', '.git'}
    out_path = os.path.abspath(out_path)
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk('.'):
            # skip excluded dirs
            parts = os.path.normpath(root).split(os.sep)
            if any(p in exclude_dirs for p in parts):
                continue
            for f in files:
                if f.endswith(('.pyc', '.pyo')):
                    continue
                full = os.path.join(root, f)
                arc = os.path.relpath(full, '.')
                z.write(full, arc)
    print('Backup created at', out_path)

if __name__ == '__main__':
    make_backup()

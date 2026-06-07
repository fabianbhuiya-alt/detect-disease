import subprocess
from pathlib import Path

repo_dir = Path(__file__).resolve().parents[1]
result_path = repo_dir / 'push_result.txt'
cmd = [r'C:\Program Files\Git\cmd\git.exe', 'push', '-u', 'origin', 'main']
proc = subprocess.run(cmd, cwd=repo_dir, capture_output=True, text=True)
result_path.write_text(f'RC={proc.returncode}\nSTDOUT={proc.stdout}\nSTDERR={proc.stderr}')
print('done')

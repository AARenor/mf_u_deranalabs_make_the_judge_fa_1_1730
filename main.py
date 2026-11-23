import os
from pathlib import Path
import sys


text = "For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway."
assert 1 <= len(text) <= 280

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(text.encode("utf-8"))
print(len(text), file=sys.stderr)

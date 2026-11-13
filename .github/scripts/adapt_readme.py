"""Copy the personal profile README and point its per-account block at this account."""
import re
import sys

src_path, dest_path = sys.argv[1], sys.argv[2]
src = open(src_path).read()

# Only the per-account block (the contribution snake) changes; everything else stays identical.
out = re.sub(
    r"<!-- per-account:start.*?<!-- per-account:end -->",
    lambda m: m.group(0).replace("AhmadoshHamad/AhmadoshHamad", "Ahmadosh-Hamad/Ahmadosh-Hamad"),
    src,
    flags=re.S,
)
note = "<!-- Synced from AhmadoshHamad/AhmadoshHamad. Edit it there; changes here are overwritten. -->\n"
open(dest_path, "w").write(note + out)

import os
from pathlib import Path

JOKE = 'I wrote "Best of luck on your next chapter!" in an office card without checking the front, so Dave spent his birthday quietly packing his desk.'


def main() -> None:
    """Write the single-line office joke entry deterministically to /output/entry.txt."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()

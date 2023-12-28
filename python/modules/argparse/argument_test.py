
import argparse
import pathlib
import subprocess

def version(ref=None):
    root = pathlib.Path(__file__) / ".." / ".." / ".."
    root = root.resolve()
    if (root / ".git").exists():
        args = ["git", "-C", str(root), "describe", "--match=[0-9]*"]
        if ref is not None:
            args.append(ref)
        describe = (
            subprocess.check_output(args).strip().decode("utf-8")
        )
        print(describe)
    else:
        return (root / "VERSION").read_text(encoding="utf-8").rstrip()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Python Argument Module Test")
    parser.add_argument("ref", nargs="?", default=None, help="reference")

    options = parser.parse_args()
    print(version(options.ref))
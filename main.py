import argparse
import subprocess
import sys


SCENES = [
    {"name": "Scene1Intro", "file": "scenes/scene1_intro.py"},
    {"name": "Scene2DP", "file": "scenes/scene2_dp.py"},
    {"name": "Scene3Text", "file": "scenes/scene3_text.py"},
    {"name": "Scene4Image", "file": "scenes/scene4_image.py"},
    {"name": "Scene5Tabular", "file": "scenes/scene5_tabular.py"},
    {"name": "Scene6System", "file": "scenes/scene6_system.py"},
]

QUALITY_FLAGS = {
    "l": "-pql",
    "m": "-pqm",
    "h": "-pqh",
    "k": "-pqk",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render Manim scenes in order")
    parser.add_argument(
        "scenes",
        nargs="*",
        help="Scene class names to render. Default: all",
    )
    parser.add_argument(
        "-q",
        "--quality",
        default="l",
        choices=QUALITY_FLAGS.keys(),
        help="Render quality: l, m, h, k",
    )
    parser.add_argument(
        "--media-dir",
        default="output",
        help="Output directory for rendered media",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available scenes and exit",
    )
    return parser.parse_args()


def list_scenes() -> None:
    for scene in SCENES:
        print(f"{scene['name']} -> {scene['file']}")


def main() -> int:
    args = parse_args()

    if args.list:
        list_scenes()
        return 0

    scene_map = {scene["name"]: scene for scene in SCENES}

    if args.scenes:
        missing = [name for name in args.scenes if name not in scene_map]
        if missing:
            print("Unknown scene(s):", ", ".join(missing))
            print("Available scenes:")
            list_scenes()
            return 2
        selected = [scene for scene in SCENES if scene["name"] in args.scenes]
    else:
        selected = SCENES

    quality_flag = QUALITY_FLAGS[args.quality]

    for scene in selected:
        command = [
            sys.executable,
            "-m",
            "manim",
            quality_flag,
            "--media_dir",
            args.media_dir,
            scene["file"],
            scene["name"],
        ]
        code = subprocess.call(command)
        if code != 0:
            return code

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

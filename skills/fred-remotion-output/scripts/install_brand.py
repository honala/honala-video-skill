"""Install transparent compatibility assets for legacy channel overlays."""
import argparse
import shutil
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
TRANSPARENT_PNG = SKILL / 'assets/component-kit-public/transparent.png'


def install_brand(project):
    target = Path(project) / 'public/brand'
    if target.resolve() == (SKILL / 'templates/episode-skeleton/public/brand').resolve():
        raise ValueError('Pass a working project, not the repository’s archived logo assets.')
    target.mkdir(parents=True, exist_ok=True)
    for filename in ('light.png', 'dark.png', 'honala-light.png', 'honala-dark.png'):
        shutil.copyfile(TRANSPARENT_PNG, target / filename)
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path, help='Remotion 工程根目录')
    args = parser.parse_args()
    print(install_brand(args.project))

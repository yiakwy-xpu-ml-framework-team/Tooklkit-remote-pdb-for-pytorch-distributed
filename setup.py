import os
import re
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)

def find_version(filepath: str) -> str:
    """Extract version information from the given filepath.
    """
    with open(filepath) as fp:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  fp.read(), re.M)
        if version_match:
            print(f"version: {version_match.group(1)}")
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

def get_path(*filepath) -> str:
    return os.path.join(ROOT_DIR, *filepath)

def get_version() -> str:
    version = find_version(get_path("version.py"))
    return version

setup(
    name="remote pdb",
    version=get_version(),
    author="LEI WANG",
    license='MIT',
    author_email='yiak.wy@gmail.com',
    url="https://github.com/yiakwy-xpu-ml-framework-team/Tooklkit-remote-pdb-for-pytorch-distributed.git",
    packages=find_packages(),
    python_requires='>=3.10',
)
"""
Start as a module
"""


import contextlib
import zipfile
import os
import argparse
from tqdm import tqdm
import requests
import logging
import glob


def get_size(start_path="."):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def download(url: str, fname: str, chunk_size: int = 1024) -> bool:
    """
    "Download a file from a URL to a local file."

    The first line is the function's signature. It's a single line of code that tells you everything
    you need to know about the function

    :param url: The URL of the file to download
    :type url: str
    :param fname: The name of the file to be downloaded
    :type fname: str
    :param chunk_size: The size of the chunks to download, defaults to 1024 (optional)
    """
    try:
        resp = requests.get(url, stream=True)
        total: int = int(resp.headers.get("content-length", 0))
        with open(fname, "wb") as file, tqdm(
            desc=fname,
            total=total,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=chunk_size):
                size = file.write(data)
                bar.update(size)
    except ConnectionError:
        logging.warning("Connection error")
        return False
    return True


def unpack(name, path="./"):
    with zipfile.ZipFile(name, mode="r") as zip:
        size = len(zip.namelist())
        for member in tqdm(iterable=zip.namelist(), total=size, desc="Extracting "):
            with contextlib.suppress(zipfile.error):
                zip.extract(member, path)
                member = os.path.join(path, member)
                tqdm.write(f"{os.path.basename(member)}({str(os.path.getsize(member))}B)")
        zip.close()
    print("\n\n")


parser = argparse.ArgumentParser()

VOICEVOX_ENGINE_URL = "https://github.com/VOICEVOX/voicevox/releases/download/0.14.6/voicevox-windows-cpu-0.14.6.zip"

UNSPECIFIED = object()

parser.add_argument("--force-reinstall", choices=[], nargs="?", default=UNSPECIFIED)
parser.add_argument("--as-not-module", choices=[], nargs="?", default=UNSPECIFIED)

args = parser.parse_args()


if not os.path.exists("VOICEVOX/VOICEVOX/") or args.force_reinstall is None:
    download(VOICEVOX_ENGINE_URL, "VOICEVOX_engine.zip")
    if args.as_not_module is None:
        unpack("VOICEVOX_engine.zip")
    else:
        unpack("VOICEVOX_engine.zip", "VOICEVOX")
    os.remove("VOICEVOX_engine.zip")
else:
    for file_name in list(set(glob.glob("./**/**/**/VOICEVOX.exe", recursive=True))):
        if get_size(os.path.dirname(file_name)) < 1258291200:
            download(VOICEVOX_ENGINE_URL, "VOICEVOX_engine.zip")
            if args.as_not_module is None:
                unpack("VOICEVOX_engine.zip")
            else:
                unpack("VOICEVOX_engine.zip", "VOICEVOX")
            os.remove("VOICEVOX_engine.zip")

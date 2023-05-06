import zipfile
import os
import argparse
from tqdm import tqdm
import requests
import logging


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
        total: int = int(resp.headers.get('content-length', 0))
        with open(fname, 'wb') as file, tqdm(
            desc=fname,
            total=total,
            unit='iB',
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


def unpack(name):
    with zipfile.ZipFile(name, mode='r') as zip:
        for member in tqdm(iterable=zip.namelist(), total=len(zip.namelist()), desc='Extracting '):
            try:
                zip.extract(member)
                tqdm.write(
                    f"{os.path.basename(member)}(" + str(os.path.getsize(member)) + "B)")
            except zipfile.error as e:
                pass
        zip.close()


parser = argparse.ArgumentParser()

VOICEVOX_ENGINE_URL = 'https://github.com/VOICEVOX/voicevox/releases/download/0.14.6/voicevox-windows-cpu-0.14.6.zip'


parser.add_argument('--mode', choices=['merge', 'split'], default='merge')

args = parser.parse_args()

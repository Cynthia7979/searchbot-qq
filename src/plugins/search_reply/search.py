from html2image import Html2Image
from string import ascii_letters
from time import sleep
import shutil, os

dest = 'D://Tools\cqHTTP\data\images'

os.chdir(dest)

hti = Html2Image()

legal_symbols = ascii_letters+'!@#$%^&()_+=-0987654321`~.,[]{};'


def get_img(kwrds: (tuple, list)) -> str:
    search_phrase = "+".join(kwrds)
    search_link = f'https://www.google.com/search?q={search_phrase}'
    filename = strip_special_symbol(search_phrase)
    sleep(1.5)
    print('[search.py] Getting screenshot of', search_link)
    result = hti.screenshot(url=search_link, save_as=filename+'.png')
    # return result[0]
    return move_file(result[0])


def move_file(from_: str) -> str:
    filename = os.path.basename(from_)
    to = os.path.join(dest, filename)
    if os.path.exists(to):
        return filename
    elif not os.path.exists(from_):
        print(f'[search.py] WARNING: File does not exist. Aborting.')
        return to  # Assume that it has already been moved
    else:
        print(f'[search.py] Moving image from {from_} to {to}...')
        shutil.move(from_, to)
        return filename


def strip_special_symbol(s: str) -> str:
    result = ''
    for l in s:
        if l in legal_symbols:
            result += l
        else:
            result += '-'
    return result

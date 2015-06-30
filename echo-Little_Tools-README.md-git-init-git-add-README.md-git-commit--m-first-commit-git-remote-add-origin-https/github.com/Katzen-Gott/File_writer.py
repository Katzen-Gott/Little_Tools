from os import listdir, makedirs
from os.path import isdir, exists, join
from shutil import copyfile
from time import sleep


def copy_files(from_dir, to_dir):
    fix = lambda user_path: user_path.replace('~', '/home/alissa')
    from_dir = fix(from_dir)
    to_dir = fix(to_dir)
    if not to_dir.endswith('/'):
        to_dir += '/'
    if not exists(from_dir):
        raise AttributeError("Source folder doesn't exist")
    if not exists(to_dir):
        print('making path')
        makedirs(to_dir)
    items = sorted(listdir(from_dir))
    if not items:
        raise AttributeError("Source folder is empty")
    for item in items:
        if item.startswith('.'):
            continue
        item_path = join(from_dir, item)
        destination = join(to_dir, item)
        print(item_path,destination)
        if isdir(item_path):
            print('found a folder. Going into')
            copy_files(item_path, destination)
        else:
            print('copying', item)
            copyfile(item_path, destination)
            sleep(1)
            while not check_copied(item, to_dir):
                sleep(1)
    return


def check_copied(file, directory):
    return listdir(directory)[-1] == file


def runner():
    from_dir = input('source folder:\n')
    to_dir = input('destination folder:\n')
    copy_files(from_dir, to_dir)

if __name__ == '__main__':
    runner()

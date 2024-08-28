import os
import shutil


def clear_folder(dest):
    for filename in os.listdir(dest):
        filepath = os.path.join(dest, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)


def copy_to_directory(curr_path, src, destination):

    clear_folder(destination)

    path_from = os.path.join(curr_path, src)

    items = os.listdir(path_from)

    for item in items:

        path_to_item = os.path.join(path_from, item)

        if os.path.isdir(path_to_item):

            path_to_dest = os.path.join(destination, item)

            print(path_to_dest)

            if not os.path.exists(path_to_dest):
                os.mkdir(path_to_dest)

            copy_to_directory(path_to_item, '',
                              os.path.join(destination, item))

        else:
            shutil.copy(path_to_item, destination)


def main():

    copy_to_directory(os.path.abspath(''), 'static',
                      os.path.join(os.path.abspath(''), 'public'))


if __name__ == '__main__':
    main()

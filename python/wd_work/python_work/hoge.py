import sys

def replace_path():
    # delete exist path
    del sys.path[14:]
    ip_path = input('Enter path to bin: ')
    print(ip_path)


if __name__ == '__main__':
    replace_path()

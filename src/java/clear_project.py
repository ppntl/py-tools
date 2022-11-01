import os, sys, pathlib, shutil

root_path = r"D:\code"
del_dir_name = "target"


def recursion(path):
    for dir in os.listdir(path):
        tmp = os.path.join(path, dir)
        if os.path.isdir(tmp):
            if dir == del_dir_name:
                print(tmp)
                shutil.rmtree(tmp, ignore_errors=True)
            else:
                recursion(tmp)


def start():
    global root_path,del_dir_name
    argv = sys.argv
    arg_num = argv.__len__()
    # for i in range(arg_num):
    #     print("{0} --> {1}".format(i, argv[i]))

    if arg_num > 1:
        root_path = argv[1]
        del_dir_name=argv[2]

    print("{0} --> {1}".format(root_path,del_dir_name))
    recursion(root_path)


if __name__ == '__main__':
    start()

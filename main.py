import sys, getopt
from folder_exploration import folder_exploration

accepted_extensions = ['.mp3', '.wav', ".ogg"]


def main(argv):
    path_to_folder = ''
    recursive = False
    combine = True
    parse = False
    parse_time = 0
    try:
        opts, _ = getopt.getopt(argv, "F:rpP:")
    except getopt.GetoptError:
        print('main.py -F <inputfolder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-F':
            path_to_folder = arg
        elif opt == '-r':
            recursive = True
        elif opt == '-p':
            parse = True
            combine = False
            parse_time = 10
        elif opt == '-P':
            parse = True
            combine = False
            parse_time = arg
    if path_to_folder == '':
        print('main.py -F <inputfolder>')
        sys.exit(2)

    print(f"options : "
          f"folder : {path_to_folder} \n"
          f"recursive : {recursive} \n"
          f"combine : {combine} \n"
          f"parse : {parse} \n"
          f"parse_time : {parse_time}s \n"
          )

    folder_exploration(path_to_folder, recursive, combine, parse, parse_time)


if __name__ == "__main__":
    main(sys.argv[1:])

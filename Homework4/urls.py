import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url")
    return parser


urls = [
    "https://gas-kvas.com/grafic/uploads/posts/2023-09/1695816032_gas-kvas-com-p-kartinki-luntik-15.jpg",
    "https://otkrit-ka.ru/uploads/posts/2021-11/foto-i-kartinki-vseh-geroev-iz-smesharikov-3.png",
    "https://i.ytimg.com/vi/C7tji7oebOI/maxresdefault.jpg",
]

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    urls.append(namespace.url)
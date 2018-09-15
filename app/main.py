import argparse

import controllers

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', type=str, default='/')
    args = parser.parse_args()

    controllers.Runner.start(args.root)

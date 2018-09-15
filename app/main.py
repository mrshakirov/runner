import argparse

import termchart

import services


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', type=str, default='/')
    args = parser.parse_args()

    services.Runner.start(args.root)
    values = [i[1] for i in services.Report.files()]
    graph = termchart.Graph(values)
    graph.draw()

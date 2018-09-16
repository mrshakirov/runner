import argparse
import datetime as dt

import services


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', type=str, default='/')
    args = parser.parse_args()

    start = dt.datetime.now()
    services.Runner.start(args.root)
    services.Report.draw()
    stop = dt.datetime.now()
    print('finished: %s' % (stop - start).total_seconds())

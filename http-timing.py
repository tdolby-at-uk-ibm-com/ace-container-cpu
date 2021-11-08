#!/usr/bin/env python3

import requests
import time
import argparse

parser = argparse.ArgumentParser(description='Time HTTP requests')
parser.add_argument('--url', help='URL to invoke', default='http://localhost:7800/cpuBurnFlow')
parser.add_argument('--iterations', help='Iterations parameter to pass to the flow', type=int, default=5000)
parser.add_argument('--requests', help='Number of requests to make', type=int, default=100)
args = parser.parse_args()

start_time = time.time_ns()

finalUrl = args.url;
if args.iterations > 0:
    finalUrl = '{0}?iterations={1}'.format(args.url, args.iterations)

for reqNumber in range(args.requests):
    before_time = time.time_ns()
    r = requests.get(finalUrl)
    after_time = time.time_ns()
    print('{0} Status code {1} time {2}'.format(((int)((before_time-start_time)/1000000)), r.status_code, (after_time - before_time)))

end_time = time.time_ns()
print('100 requests in {0}ms avg {1}ms'.format((int)((end_time - start_time)/1000000), ((int)((end_time - start_time)/(args.requests * 1000000)))))

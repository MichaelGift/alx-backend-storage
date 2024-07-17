#!/usr/bin/env python3
"""Log stats in MongoDB using PyMongo.
"""
from pymongo import MongoClient


def print_http_request_logs(nginx_collection):
    """Print the number of logs and the number of logs by method.
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_http_request_logs(client.logs.nginx)

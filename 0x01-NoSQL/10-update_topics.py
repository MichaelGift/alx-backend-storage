#!/usr/bin/env python3
"""Update a document in a collection.
"""


def update_topics(mongo_collection, name, topics):
    """Updates a document in a collection.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

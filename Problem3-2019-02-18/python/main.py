#!/usr/bin/env python3

from json import dumps, loads


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.serialized = {}


def serialize(node: Node, result: str = "") -> str:
    node.serialized["val"] = node.val

    if node.left is not None:
        node.serialized["left"] = serialize(node.left)

    if node.right is not None:
        node.serialized["right"] = serialize(node.right)

    return dumps(node.serialized)


def deserialize(node_str: str) -> Node:
    node_json = loads(node_str)
    if "left" in node_json:
        if node_json["left"] == dict:
            node_json["left"] = dumps(node_json["left"])
        if "right" in node_json:
            if node_json["right"] == dict:
                node_json["right"] = dumps(node_json["right"])
            return Node(
                node_json["val"],
                left=deserialize(node_json["left"]),
                right=deserialize(node_json["right"]),
            )
        else:
            return Node(node_json["val"], left=deserialize(node_json["left"]))
    elif "right" in node_json:
        if node_json["right"] == dict:
            node_json["right"] = dumps(node_json["right"])
        return Node(node_json["val"], right=deserialize(node_json["right"]))
    return Node(node_json["val"])

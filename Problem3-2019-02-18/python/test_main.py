from .main import Node, serialize, deserialize


def test_serialize_single_node():
    node = Node("root")
    # root has value root and no left, no right nodes, thus two end markers
    expected = '{"val": "root"}'
    serialized = serialize(node)
    assert serialized == expected


def test_serialize_two_nodes_left_side():
    node = Node("root", left=Node("left"))
    expected = '{"val": "root", "left": "{\\"val\\": \\"left\\"}"}'
    serialized = serialize(node)
    assert serialized == expected


def test_serialize_two_nodes_right_side():
    node = Node("root", right=Node("right"))
    expected = '{"val": "root", "right": "{\\"val\\": \\"right\\"}"}'
    serialized = serialize(node)
    assert serialized == expected


def test_serialize_three_nodes_one_each_side():
    node = Node("root", left=Node("left"), right=Node("right"))
    expected = '{"val": "root", "left": "{\\"val\\": \\"left\\"}", "right": "{\\"val\\": \\"right\\"}"}'
    serialized = serialize(node)
    assert serialized == expected


def test_example():
    node = Node("root", Node("left", Node("left.left")), Node("right"))
    assert deserialize(serialize(node)).left.left.val == "left.left"

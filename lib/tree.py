class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._get_element_by_id_recursive(self.root, id)

    def _get_element_by_id_recursive(self, node, id):
        if node is None:
            return None
        if node.get('id') == id:
            return node
        if 'children' in node:
            for child in node['children']:
                result = self._get_element_by_id_recursive(child, id)
                if result is not None:
                    return result
        return None

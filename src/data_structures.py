class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.num_entries = 0
        self.entries = []

    def insert(self, entry: str):
        current = self.root
        for ch in entry:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True
        self.num_entries += 1
        self.entries.append(entry)

    def has_entry(self, entry):
        try:
            node = self.goto_prefix(entry)
            return node.is_end
        except ValueError:
            return False
    
    def goto_prefix(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                raise ValueError(f"{prefix} not in Trie")
            current = current.children[ch]
        return current

    def count_prefix(self, prefix):
        try:
            node = self.goto_prefix(prefix)

            def walk_subtree_recursive(node):
                count = 0
                if node.is_end:
                    count += 1
                for ch in node.children:
                    count += walk_subtree_recursive(node.children[ch])
                return count
            
            return walk_subtree_recursive(node)
        except ValueError:
            return 0

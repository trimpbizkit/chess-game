class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.num_entries = 0

    def insert(self, entry: str):
        current = self.root
        for ch in entry:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True
        self.num_entries += 1

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

    def list_full_entries(self):
        def walk_subtree_recursive(node, current_keys):
            end_terms = []
            if node.is_end:
                end_terms.append(current_keys)
            for ch in node.children:
                new_keys = current_keys
                new_keys.extend(ch)
                end_terms.extend(walk_subtree_recursive(node.children[ch], new_keys))
            return end_terms
        
        full_key_lists = walk_subtree_recursive(self.root, [])
        # logic for full_key_list being substrings to join
        full_entries = []
        for key_list in full_key_lists:
            full_entries.append("".join(key_list))
        return full_entries

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self._stack:
            return None
        return self._stack.pop()
    
    def peek(self):
        if not self._stack:
            return None
        return self._stack[-1]
    
    def is_empty(self):
        return len(self._stack) == 0
    
    def size(self):
        return len(self._stack)

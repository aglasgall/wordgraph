from collections import deque

class node(object):
    def __init__(self,word):
        self.word = word
        self.neighbors = set()
        # used internally by find_path; is transient
        self.parent = None

    def add_neighbor(self, node):
        self.neighbors.add(node)
        node.neighbors.add(self)


def hamming_distance(word1, word2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(word1, word2))

class graph(object):
    def __init__(self, wordlist):
        # for uniqueness of nodes
        self.nodes = {}
        for word in wordlist:
            self.nodes[word] = node(word)        
        wordlen = 0
        for word in wordlist:
            # validate that all words in the list are the same length
            if len(word) != wordlen:
                if wordlen == 0:
                    wordlen = len(word)
                else:
                    raise ValueError, ("%s is not %d letters long" % (word, wordlen))
            # actually build the graph
            word_node = self.nodes[word]
            for other_word in wordlist:
                if word == other_word:
                    continue
                if hamming_distance(word, other_word) == 1:
                    word_node.add_neighbor(self.nodes[other_word])


    # straightfoward breadth-first search with path tracking
    def find_path(self, word1, word2):
        if (word1 not in self.nodes) or (word2 not in self.nodes):
            raise ValueError, "Both words must be in the word list"
        starting_node = self.nodes[word1]
        queue = deque()
        visited = set()
        visited.add(starting_node)
        queue.append(starting_node)
        while(len(queue) != 0):
            node = queue.popleft()
            if node.word == word2:
                # walk the chain of parent pointers to recover the path;
                # it'll come out backwards, so reverse it before returning it.
                path = [node.word]
                while node.word != word1:
                    path.append(node.parent.word)
                    node = node.parent
                path.reverse()
                return path
            else:
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        neighbor.parent = node
                        queue.append(neighbor)    

import unittest
import wordgraph

class word_graph_tests(unittest.TestCase):
    def test_validates_word_length(self):
        wordlist = ["abcde", "defghi"]
        self.assertRaises(ValueError, wordgraph.graph, wordlist)

    def test_validates_presence_of_words_in_graph(self):
        wordlist = ["abcde", "defgh"]
        graph = wordgraph.graph(wordlist)
        self.assertRaises(ValueError, graph.find_path, "abcde", "lmnop")
        self.assertRaises(ValueError, graph.find_path, "lmnop", "abcde")

    def test_finds_valid_path(self):
        wordlist = ["smart",
                    "start",
                    "stark",
                    "stack",
                    "slack",                    
                    "black"]
        graph = wordgraph.graph(wordlist)
        for i in xrange(0,len(wordlist)-1):
            self.assertEquals(1,wordgraph.hamming_distance(wordlist[i], 
                                                           wordlist[i+1]))
        

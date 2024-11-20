class HuffmanNode :
    def __init__(self, ch, frequency,  left,   right) :
        self.ch = ch
        self.frequency = frequency
        self.left = left
        self.right = right
 
    def __str__(self):
    	return "(" + str(self.ch) + ", " + str(self.frequency) + ")"  
 
class HuffmanCoding :
 
    def getCode(self, input) :
        freqMap = self.buildFrequencyMap(input) 
        nodeQueue = self.sortByFrequence(freqMap)
        self.root = self.buildTree(nodeQueue)
        codeMap = self.createHuffmanCode(self.root)
        return codeMap
 
    def buildFrequencyMap(self, input) :
        map = {}
        for c in input:
            map[c] = map.get(c,0) + 1
        return map
 
    def sortByFrequence(self, map) :
        queue = []
        for k, v in map.items():
            queue.append(HuffmanNode(k, v, None, None))       
        queue.sort(key = lambda x: x.frequency)
        return queue  
 
    def buildTree(self, nodeQueue) :             
        while len(nodeQueue) > 1:
            node1 = nodeQueue.pop(0)
            node2 = nodeQueue.pop(0)
            node = HuffmanNode('', node1.frequency + node2.frequency, node1, node2)
            nodeQueue.append(node)
        return nodeQueue.pop(0)
 
    def createHuffmanCode(self, node) :
        map = {}
        self.createCodeRec(node, map, "")
        return map
    
    def createCodeRec(self, node, map, s) :
        if node.left == None and node.right == None :
            map[node.ch] = s
            return
        self.createCodeRec(node.left, map, s + '0')
        self.createCodeRec(node.right, map, s + '1')
 
    def encode(self, codeMap, input) :
        s = ""
        for  i in range(0, len(input)):
            s += codeMap.get(input[i])
        return s
 
    def decode(self, coded) :
        s = ""
        curr = self.root
        for  i in range (0, len(coded)) :
            curr = curr.right if coded[i] == '1' else curr.left
            if curr.left == None and curr.right == None:
                s += curr.ch
                curr = self.root 
        return s
	
input="AAAAAABBCCDDEEFFFFF"
huffman = HuffmanCoding()       
codeMap = huffman.getCode(input)
print("code: " + str(codeMap))
encoded = huffman.encode(codeMap, input)
print("encode message: " + encoded)
decode = huffman.decode(encoded)
print("decoding string: " + decode)
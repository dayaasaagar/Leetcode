class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.suggestions=[]
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        root =TrieNode()

        for product in products:
            node =root
            for p in product:
                node =node.children[p]
                if len(node.suggestions)<3:
                    node.suggestions.append(product)

        result =[]

        node =root
        for char in searchWord:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                while len(result)<len(searchWord):
                    result.append([])
                break
        return result


import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        words = set()
        combined = positive + negative
        for sentence in combined:
            for word in sentence.split():
                words.add(word)
        
        #sorting the words:
        sorted_words = sorted(list(words))
        words_map = {}
        for i,word in enumerate(sorted_words):
            words_map[word] = i+1

        def encode(combined):
            output = []
            for sentence in combined:
                ans = []
                for word in sentence.split():
                    ans.append(words_map[word])
                output.append(torch.tensor(ans))
            return output
        
        return torch.nn.utils.rnn.pad_sequence(encode(combined),batch_first = True)
        
        

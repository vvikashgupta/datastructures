class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palinderome(str):
            return True if str == str[::-1] else False
        result_set = []
        if words:
            words_len = len(words)
            for index in range(words_len):
                for count in range(words_len):
                    if index == count:
                        continue
                    else:
                        if is_palinderome(words[index] + words[count]):
                            result_set.append([index,count])
            return result_set

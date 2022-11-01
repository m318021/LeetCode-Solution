class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        stream = sentence.split(" ")

        for i in range(len(stream)):
            sub_words = stream[i].split(searchWord)
            if len(sub_words) > 1 and sub_words[0] == "":
                return i+1

        return -1





if __name__ == '__main__':
    sentence = "i love eating burger"
    searchWord = "burg"
    output = Solution().isPrefixOfWord(sentence, searchWord)
    print(output,"\n")

    sentence = "this problem is an easy problem"
    searchWord = "pro"
    output = Solution().isPrefixOfWord(sentence, searchWord)
    print(output,"\n")

    sentence = "i am tired"
    searchWord = "you"
    output = Solution().isPrefixOfWord(sentence, searchWord)
    print(output,"\n")
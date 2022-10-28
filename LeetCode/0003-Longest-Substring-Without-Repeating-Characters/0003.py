class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        print(s)
        dict_sub_string = {}
        start = 0
        result = 0

        for i in range(len(s)):
            print("Before i={}, s[{}] = {}, start={}, result={}, dict={}".format(i,i,s[i],start,result,dict_sub_string))
            if s[i] in dict_sub_string:
                start = max(dict_sub_string[s[i]],start)
            result = max(result, i-start+1)
            dict_sub_string[s[i]] = i+1
            print("After  i={}, s[{}] = {}, start={}, result={}, dict={}".format(i,i,s[i],start,result,dict_sub_string))
            print("\n")




        return result

        # print(s)
        # dict_sub_string = {}
        # count = 0
        # first_string = -1
        # for i in range(len(s)):
        #     print("first_string = {}".format(first_string))
        #     print("s[{}]={}".format(i,s[i]))
        #     print("dict_sub_string= {}' ".format(dict_sub_string))
        #     print("count = {}".format(count))
        #     print("==========================================")
        #     if s[i] in dict_sub_string and dict_sub_string[s[i]] > first_string:
        #         first_string = dict_sub_string[s[i]]
        #     dict_sub_string[s[i]] = i
            
        #     count = max(count, (i-first_string))
        #     print("!!first_string = {}".format(first_string))
        #     print("!!s[{}]={}".format(i,s[i]))
        #     print("!!dict_sub_string= {}' ".format(dict_sub_string))
        #     print("!!count = {}".format(count))
        #     print("++++++++++++++++++++++++++++++++++++++++++")


        # print("first_string = {}".format(first_string))
        # print("s[{}]={}".format(len(s)-1,s[len(s)-1]))
        # print("dict_sub_string= {}' ".format(dict_sub_string))
        # print("count = {}".format(count))



        # return count
            



if __name__ == '__main__':

    # s = "abcabcbb"
    s = "pwwkew"
    result = Solution().lengthOfLongestSubstring(s)
    # result1 = Solution().twoSum([2,7,11,15], 9)
    # print("Input: nums = [2,7,11,15], target = 9\nOutput = {}\n".format(result1))

    # result2 = Solution().twoSum([3,2,4], 6)
    # print("Input: nums = [3,2,4], target = 6\nOutput = {}\n".format(result2))
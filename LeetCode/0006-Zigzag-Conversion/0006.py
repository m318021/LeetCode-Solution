from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:


        if numRows == 1:
            return s
        
        rows = ["" for i in range(numRows)]
        
        direction = -1
        row = 0
        for i in range(len(s)):
            
            rows[row]+=s[i]
            if (row == 0 or row==numRows-1):
                direction *= -1
            row+=direction
            
        return "".join(rows)

    	# dict_letters = { value:'' for value in range(numRows)}


    	# count = 0
    	# flag = 1
    	# for i in range(len(s)):
     #        index = count % numRows
     #        if index == numRows-1:
     #            flag = -1
     #        elif index == 0:
     #            flag = 1
     #        dict_letters[ index ] += s[i]
     #        count = count + flag


    	# result = ""
    	# print(dict_letters.values())
    	# for value in dict_letters.values():
    	# 	result += value

    	# return result



if __name__ == '__main__':

	s = "PAYPALISHIRING"
	numRows = 3

	result = Solution().convert(s, numRows)
	print(result)

	numRows = 4

	result = Solution().convert(s, numRows)
	print(result)
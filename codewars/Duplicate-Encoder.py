from typing import List

def duplicate_encode(word):
    #your code here
    dict_record = {}
    result = ""
    word = word.lower()

    index = 0
    for i in range(len(word)):
        if word[i] not in dict_record:
            dict_record[word[i]] = 0
        else:
            dict_record[word[i]] = dict_record[word[i]] + 1


    for i in range(len(word)):
        if dict_record[word[i]] > 0:
            result += ')'
        else:
            result += '('


    return result



if __name__ == '__main__':

    result = duplicate_encode("din")
    print("din = {}".format(result))
    result = duplicate_encode("recede")
    print("recede = {}".format(result))
    result = duplicate_encode("Success")
    print("Success = {}".format(result))
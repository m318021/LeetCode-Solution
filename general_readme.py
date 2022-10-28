import json

folder_name = "LeetCode"
# 0003 0004 0006 0008 0014 0015 0020 0046 0047 0055 0102 0107 0172 0217

"0003 0004 0006 0008 0014 0015 0020 0046 0047() 0055 0102() 0107() 0172 0217 "
cases = [
    {
        "id" : "0003",
        "url" : "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        "language" : "Python3",
        "difficulty" : "Medium",
    },
    {
        "id": "0004",
        "url": "https://leetcode.com/problems/two-sum/",
        "language" : "Python3",
        "difficulty" : "Hard",
    },
    {
        "id": "0006",
        "url": "https://leetcode.com/problems/zigzag-conversion/",
        "language" : "Python3",
        "difficulty" : "Medium",
    },
    {
        "id": "0008",
        "url": "https://leetcode.com/problems/string-to-integer-atoi/",
        "language": "Python3",
        "difficulty": "Medium ",
    },
    {
        "id": "0014",
        "url": "https://leetcode.com/problems/longest-common-prefix/",
        "language": "Python3",
        "difficulty": "Easy",
    },
    {
        "id": "0015",
        "url": "https://leetcode.com/problems/3sum/",
        "language": "Python3",
        "difficulty": "Medium",
    },
    {
        "id": "0020",
        "url": "https://leetcode.com/problems/valid-parentheses/",
        "language": "Python3",
        "difficulty": "Easy",
    },
    {
        "id": "0046",
        "url": "https://leetcode.com/problems/permutations/",
        "language": "Python3",
        "difficulty": "Medium",
    },
    {
        "id": "0047",
        "url": "https://leetcode.com/problems/permutations-ii/",
        "language": "Python3",
        "difficulty": "Medium",
    },
    {
        "id": "0055",
        "url": "https://leetcode.com/problems/jump-game/",
        "language": "Python3",
        "difficulty": "Medium",
    },
    {
        "id": "0102",
        "url": "https://leetcode.com/problems/binary-tree-level-order-traversal/",
        "language": "Python3",
        "difficulty": "Medium",
    },
    {
        "id": "0107",
        "url": " https://leetcode.com/problems/binary-tree-level-order-traversal-ii/",
        "language": "Python3",
        "difficulty": "Easy",
    },
    {
        "id": "0172",
        "url": "https://leetcode.com/problems/factorial-trailing-zeroes/",
        "language": "Python3",
        "difficulty": "Easy",
    },
    {
        "id": "0217",
        "url": "https://leetcode.com/problems/contains-duplicate/",
        "language": "Python3",
        "difficulty": "Easy",
    },
]

def func_generate_case_info(id, url, language, difficulty):

    split_url = url.split("/")
    path_name = split_url[-2]
    split_path_name = path_name.split("-")
    # print(split_path_name)
    new_split_path_name = []
    new_path_name = ""
    for word in split_path_name:
        upper_char = word[0].upper()
        upper_char = upper_char + word[1:]
        new_split_path_name.append(upper_char)
    title = ""
    for word in new_split_path_name:
        title = title + word + " "
        new_path_name = new_path_name + word + "-"

    new_path_name = new_path_name[:-1]
    title = title[:-1]

    case_info = {
        "id": id,
        "title": title,
        "url": url,
        "language": language,
        "case_path": "{}/{}-{}/{}.py".format(folder_name, id, new_path_name, id),
        "difficulty": difficulty
    }

    return case_info

if __name__ == '__main__':

    readme_md = []
    for case in cases:
        result = func_generate_case_info(id=case["id"], url=case["url"], language=case["language"], difficulty=case["difficulty"])
        add_line = "|{}|[{}]({}) | [{}](./{}) | {} | ".format(result["id"],
                                                              result["title"],
                                                              result["url"], result["language"],
                                                              result["case_path"],
                                                              result["difficulty"])

        print(add_line)

        readme_md.append(add_line)

    print("Json file : ")
    json_formatted_str = json.dumps(readme_md, indent=4)
    print(json_formatted_str)







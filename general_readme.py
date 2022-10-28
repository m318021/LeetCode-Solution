import json

folder_name = "LeetCode"
cases = [
    {
        "id" : "0258",
        "url" : "https://leetcode.com/problems/add-digits/",
        "language" : "Python3",
        "difficulty" : "Easy",
    },
    {
        "id": "0263",
        "url": "https://leetcode.com/problems/ugly-number/",
        "language" : "Python3",
        "difficulty" : "Easy",
    },
    {
        "id": "1945",
        "url": "https://leetcode.com/problems/length-of-last-word/",
        "language" : "Python3",
        "difficulty" : "Easy",
    },
]


def func_generate_case_info(id, url, language, difficulty):

    split_url = url.split("/")
    path_name = split_url[-2]
    split_path_name = path_name.split("-")
    # print(split_path_name)
    new_path_name = []
    for word in split_path_name:
        upper_char = word[0].upper()
        upper_char = upper_char + word[1:]
        new_path_name.append(upper_char)
    title = ""
    for word in new_path_name:
        title = title + word + " "

    title = title[:-1]

    case_info = {
        "id": id,
        "title": title,
        "url": url,
        "language": language,
        "case_path": "{}/{}-{}/{}.py".format(folder_name, id, path_name, id),
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







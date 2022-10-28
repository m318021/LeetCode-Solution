import json

folder_name = "LeetCode"
cases = [

    {
        "id" : "0001",
        "name" : "Two Sum",
        "url": "https://leetcode.com/problems/two-sum/",
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







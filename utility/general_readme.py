import json
import configparser
import pathlib, os
import yaml
import requests, hmac, hashlib
from urllib.parse import urljoin

# leetCode_config = configparser.ConfigParser()
root_path = pathlib.Path(__file__).parent.parent.resolve()

folder_name = "LeetCode"
leetCode_yaml_path = "utility/leetCode.yaml"
default_file_text = "if __name__ == '__main__': \n    print(\"TEST\")"
language = "Python3"

def func_get_leetcode_cases(limit=100, filters={}):
    url = "https://leetcode.com/graphql/"

    body = {
        "query":"\n query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n problemsetQuestionList: questionList(\n categorySlug: $categorySlug\n limit: $limit\n skip: $skip\n filters: $filters\n ) {\n total: totalNum\n questions: data {\n acRate\n difficulty\n freqBar\n frontendQuestionId: questionFrontendId\n isFavor\n paidOnly: isPaidOnly\n status\n title\n titleSlug\n topicTags {\n name\n id\n slug\n }\n hasSolution\n hasVideoSolution\n }\n }\n}\n ",
        "variables":{
            "categorySlug":"",
            "skip":0,
            "limit":limit,
            "filters":filters
        }
    }

    headers = {
        "accept": "*/*",
        "content-type": "application/json"
    }

    response = requests.Session().get(url=url, headers=headers, data=json.dumps(body))

    assert response.status_code == 200

    return response.json()

def func_get_leetcode_case_data(case_id):
    filters = {"searchKeywords": str(case_id)}
    filter_questions = func_get_leetcode_cases(filters=filters)["data"]["problemsetQuestionList"]["questions"]
    case = {}
    for data in filter_questions:
        if data["frontendQuestionId"] == str(case_id):
            case = data
            break

    return case

def get_yaml_data(yaml_file_path):
    file_path = os.path.join(root_path, yaml_file_path)
    with open(file_path) as f:
        yaml_data = yaml.load(f, Loader=yaml.SafeLoader)

    return yaml_data

def print_json(input):
    json_formatted_str = json.dumps(input, indent=4)
    print(json_formatted_str)

def print_result(data):
    for item in data:
        print(item)

def func_generate_case_info(case_id):

    case_info = func_get_leetcode_case_data(int(case_id))

    case_folder_name = case_id
    split_case_title = case_info["title"].split(" ")
    for word in split_case_title:
        case_folder_name = case_folder_name + "-" + word

    case_name = "{}.py".format(case_id)

    data = {
        "title" : case_info["title"],
        "url" : "https://leetcode.com/problems/{}/".format(case_info["titleSlug"]),
        "difficulty" : case_info["difficulty"],
        "case_path" : "{}/{}/{}".format(folder_name, case_folder_name, case_name),
        "folder_path" : "{}/{}".format(folder_name, case_folder_name)
    }

    return data

def generate_readme_md_by_yaml(yaml_file_path = leetCode_yaml_path, open_file = True):
    leetCode_info = get_yaml_data(yaml_file_path=yaml_file_path)
    readme_md = []
    for case_id in leetCode_info['cases']:
        str_case_id = ""
        if 0<case_id<10:
            str_case_id = "000"+str(case_id)
        elif 9 < case_id < 100:
            str_case_id = "00"+str(case_id)
        elif 99 < case_id < 1000:
            str_case_id = "0"+str(case_id)
        else:
            str_case_id = str(case_id)

        result = func_generate_case_info(str_case_id)

        add_line = "| {} | [{}]({}) | [{}](./{}) | {} | ".format(str_case_id,
                                                              result["title"],
                                                              result["url"],
                                                              language,
                                                              result["case_path"],
                                                              result["difficulty"]
                                                              )

        if open_file:
            if os.path.isdir(result["folder_path"]) == False:
                os.mkdir(result["folder_path"])
                print("Create Folder : {}".format(result["folder_path"]))

                f = open(result["case_path"], "w+")
                f.write(default_file_text)
                f.close()
                print("Create File : {}".format(result["case_path"]))

            else:
                print("FIle : \"{}\" exist".format(result["case_path"]))

        readme_md.append(add_line)

    return readme_md


if __name__ == '__main__':

    read_md_info = generate_readme_md_by_yaml(open_file=True)
    read_md_info.sort()
    print("\nREADME.md ===============================\n")
    print_result(read_md_info)
    print("\n ===============================\n")
    print("{} cases".format(len(read_md_info)))













import json
import configparser
import pathlib, os
import yaml, time
import requests, hmac, hashlib
import path
from urllib.parse import urljoin
from utility.api_request import *
# leetCode_config = configparser.ConfigParser()
root_path = pathlib.Path(__file__).parent.parent.resolve()

folder_name = "LeetCode"
README_MD = os.path.join(root_path, "README.md")
leetCode_yaml_path = "add_leetCode_cases.yaml"
default_file_text = "from typing import List\nif __name__ == '__main__': \n    #input\n    #output"
language = "Python3"



class Generate_ReadMe():
    def __init__(self):
        self.url = "https://leetcode.com"
        self.api_request = API_Request(server=self.url)
        self.path = "graphql/"
        self.body = {
            "query":"\n query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n problemsetQuestionList: questionList(\n categorySlug: $categorySlug\n limit: $limit\n skip: $skip\n filters: $filters\n ) {\n total: totalNum\n questions: data {\n acRate\n difficulty\n freqBar\n frontendQuestionId: questionFrontendId\n isFavor\n paidOnly: isPaidOnly\n status\n title\n titleSlug\n topicTags {\n name\n id\n slug\n }\n hasSolution\n hasVideoSolution\n }\n }\n}\n ",
            "variables":{
                "categorySlug":"",
                "skip":0,
                "limit":0,
                "filters": {}
            }
        }
        self.header = {
            "accept": "*/*",
            "content-type": "application/json"
        }

    def func_get_leetcode_cases(self, limit=100, filters={}, checkout_status=True):

        body = self.body
        body["variables"]["limit"] = limit
        body["variables"]["filter"] = filters
        headers = self.header
        response = self.api_request.post(path=self.path, headers=headers, data=json.dumps(body))
        assert response.status_code == 200
        return response.json()

    def func_get_total_leet_code_cases(self):
        get_total_cases = self.func_get_leetcode_cases()

        total = get_total_cases["data"]["problemsetQuestionList"]["total"]

        total_questions = self.func_get_leetcode_cases(limit=total)["data"]["problemsetQuestionList"]["questions"]

        return total_questions


    def func_get_leetcode_case_data(self, case_id, total_questions):

        case = {}
        for data in total_questions:
            if data["frontendQuestionId"] == str(case_id):
                case = data
                break

        return case

    def get_yaml_data(self, yaml_file_path):
        file_path = os.path.join(root_path, yaml_file_path)
        with open(file_path) as f:
            yaml_data = yaml.load(f, Loader=yaml.SafeLoader)

        return yaml_data

    def print_json(self, input):
        json_formatted_str = json.dumps(input, indent=4)
        print(json_formatted_str)

    def print_result(self, data):
        for item in data:
            print(item)

    def func_generate_case_info(self, case_id, total_questions):

        case_info = self.func_get_leetcode_case_data(int(case_id), total_questions=total_questions)

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

    def func_print_case_info(self, total_questions, case_id:str, open_file = True):
        result = self.func_generate_case_info(case_id=case_id, total_questions=total_questions)

        add_line = "| {} | [{}]({}) | [{}](./{}) | {} | ".format(case_id,
                                                                 result["title"],
                                                                 result["url"],
                                                                 language,
                                                                 result["case_path"],
                                                                 result["difficulty"]
                                                                 )

        if open_file:
            abs_path = os.path.join(root_path, result["folder_path"] )
            abs_file_path = os.path.join(root_path, result["case_path"])
            if os.path.isdir(abs_path) == False:
                os.mkdir(abs_path)
                print("Create Folder : {}".format(result["folder_path"]))

                f = open(abs_file_path, "w+")
                f.write(default_file_text)
                f.close()
                print("Create File : {}".format(result["case_path"]))

            else:
                print("FIle : \"{}\" exist".format(result["case_path"]))

        return add_line



    def generate_readme_md_by_yaml(self, total_questions, yaml_file_path = leetCode_yaml_path, open_file = True):
        leetCode_info = self.get_yaml_data(yaml_file_path=yaml_file_path)
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

            add_line = self.func_print_case_info(total_questions, str_case_id)
            readme_md.append(add_line)

        return readme_md

    def generate_readme_md_case_info(self, total_questions):
        abs_folder_path = os.path.join(root_path, folder_name)
        case_list = os.listdir(path= abs_folder_path)

        result = []
        for folder in case_list:

            if folder != ".DS_Store":
                split_folder_name = folder.split("-")
                print("-", end='')
                add_line = self.func_print_case_info(total_questions, split_folder_name[0], False)
                result.append(add_line)

        print("Done")

        return result


    def write_readme_md_file(self, readme_data):


        summary = "LeetCode\n========\n\n|-- | ID | Title | python3                                   | Difficulty |\n| -- |-- | ----- | ------------------------------------------- | ---------- | "
        count = 1
        for item in readme_data:
            summary = summary + "\n" +"|  " + str(count) +item
            count = count+1

        f = open(README_MD, "w")
        f.write(summary)
        f.close()
        print(summary)



if __name__ == '__main__':

    generate_readme = Generate_ReadMe()
    total_questions = generate_readme.func_get_total_leet_code_cases()

    read_md_info = generate_readme.generate_readme_md_by_yaml(total_questions, open_file=True)
    read_md_info.sort()
    print("\nREADME.md ===============================\n")
    generate_readme.print_result(read_md_info)
    print("\n ===============================\n")
    print("add {} cases".format(len(read_md_info)))
    print("\n\n ===============================\n\n")
    result = generate_readme.generate_readme_md_case_info(total_questions)
    result.sort()
    print("Upate READEME.md ")
    generate_readme.write_readme_md_file(result)
    print("{} cases".format(len(result)))















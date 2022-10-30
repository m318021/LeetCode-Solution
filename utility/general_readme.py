import json
import configparser
import pathlib, os
import yaml

# leetCode_config = configparser.ConfigParser()
root_path = pathlib.Path(__file__).parent.parent.resolve()

folder_name = "LeetCode"
leetCode_yaml_path = "utility/leetCode.yaml"
default_file_text = "if __name__ == '__main__': \n    print(\"TEST\")"

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

def func_generate_case_info(case_info):

    split_case_title = case_info["title"].split(" ")
    case_folder_name = case_info["id"]

    for word in split_case_title:
        case_folder_name = case_folder_name + "-" + word

    case_name = "{}.py".format(case_info["id"])

    data = case_info
    data["case_path"] = "{}/{}/{}".format(folder_name, case_folder_name, case_name)
    data["folder_path"] = "{}/{}".format(folder_name, case_folder_name)

    return data

def generate_readme_md_by_yaml(yaml_file_path = leetCode_yaml_path, open_file = True):
    leetCode_info = get_yaml_data(yaml_file_path=yaml_file_path)

    readme_md = []
    for index in leetCode_info:
        result = func_generate_case_info(leetCode_info[index])
        add_line = "| {} | [{}]({}) | [{}](./{}) | {} | ".format(result["id"],
                                                              result["title"],
                                                              result["url"],
                                                              result["language"],
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
    print_result(generate_readme_md_by_yaml(open_file=True))












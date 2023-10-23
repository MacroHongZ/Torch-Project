import json

with open("Demo/code/version1/main.py", "r") as fp:
    main_content = fp.read()

with open("Demo/code/version1/utils.py", "r") as fp:
    utils_content = fp.read()

with open("Demo/code/version1/model.py", "r") as fp:
    model_content = fp.read()

with open("Demo/code/version1/data.py", "r") as fp:
    data_content = fp.read()

content = {"main": main_content,
           "utils": utils_content,
           "model": model_content,
           "data": data_content}

with open("code.json", "w+") as fp:
    json.dump(content, fp, indent=4)

import json

with open("Demo/code/version1/main.py", "r") as fp:
    main_content = fp.read()

with open("Demo/code/version1/model/mlp.py", "r") as fp:
    model_content = fp.read()

with open("Demo/code/version1/model/mlp_trainer.py", "r") as fp:
    modelTra_content = fp.read()

with open("Demo/code/version1/model/trainer_template.py", "r") as fp:
    Tra_content = fp.read()

with open("Demo/code/version1/model/metric.py", "r") as fp:
    metric_content = fp.read()

with open("Demo/code/version1/data/demo_data.py", "r") as fp:
    data_content = fp.read()

with open("Demo/code/version1/data/utils.py", "r") as fp:
    utils_content = fp.read()

content = {
    "main": main_content,
    "model": model_content,
    "modelTra": modelTra_content,
    "baesTra": Tra_content,
    "metric": metric_content,
    "data": data_content,
    "utils": utils_content,
}

with open("code.json", "w+") as fp:
    json.dump(content, fp, indent=4)

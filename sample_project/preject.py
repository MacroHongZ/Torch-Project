import os
import time
import json


class Project():
    def __init__(self, project_name="MyProject", path=os.getcwd()):
        if not os.path.exists(path):
            raise IOError("The path not exists")
        else:
            directory = os.path.join(path, project_name)

        self.project_name = project_name
        self.path = directory
        self.directories = ["code", "data", "report"]

    def creat_directory(self):
        os.mkdir(self.path)
        for directory in self.directories:
            main_path = os.path.join(self.path, directory)
            os.mkdir(main_path)

        self.creat_code_dir()
        self.creat_data_dir()

    def creat_code_dir(self):
        current_directory = os.path.join(self.path, self.directories[0])
        path1 = os.path.join(current_directory, "version1")
        path2 = os.path.join(current_directory, "version2")
        os.mkdir(path1)
        os.mkdir(path2)

        self.add_code(path1)

    def creat_data_dir(self):
        current_directory = os.path.join(self.path, self.directories[1])
        path1 = os.path.join(current_directory, "dataset1")
        path2 = os.path.join(current_directory, "dataset2")
        os.mkdir(path1)
        os.mkdir(path2)

    @staticmethod
    def add_code(path):
        if len(os.listdir(path)) != 0:
            raise ValueError("path is not empty")

        os.mkdir(os.path.join(path, "output_files"))
        os.mkdir(os.path.join(path, "output_files", "check_point"))

        os.mkdir(os.path.join(path, "model"))
        os.mkdir(os.path.join(path, "data"))

        with open('code.json', "r") as fp:
            code_content = json.load(fp)

        date = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
        path1 = os.path.join(path, "main.py")
        with open(path1, "w") as fp:
            fp.write('# create time: {}'.format(date))
            fp.write("\n")
            fp.write('# author:  WangHZ')
            fp.write("\n")
            fp.write(code_content["main"])

        path1 = os.path.join(path, "utils.py")
        with open(path1, "w") as fp:
            fp.write("# other code")
            fp.write("\n")
            fp.write(code_content["utils"])

        path1 = os.path.join(path, "model\\model.py")
        with open(path1, "w") as fp:
            fp.write(code_content["model"])

        path1 = os.path.join(path, "data\\data.py")
        with open(path1, "w") as fp:
            fp.write(code_content["data"])


project = Project(project_name="Demo_Pro")
project.creat_directory()

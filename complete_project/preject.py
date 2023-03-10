import os
import time
import json


class Project():
    ascii_art = """
                            ,-. 
                           /$$| 
                          ,;$'`: 
                         / $'  `, 
                         | `     \, 
                         |,m.    ,\_ 
                         |Y"F ,-,$$ `. 
                         |`-'/-'$$,::.\ 
                          \    ;$';::: ) 
                         ,:\   $':::;,'_ 
    _,---------.__   ,.. ::'\ `';::',-' \ 
   ($$$"'   (88") `-.;:::;, )  `',-dP  : `, 
    `--.      ,--,     `-.|"-.,     --. : \, 
        \_    `-',$$$:.   \ -'\`-._  `'  : \__ 
          `.`$$$$"',.:::/  `.-'\   `--._      `---._________,'`._,' 
            ) .:::::::'/,   \`. \       `--------------------``' 
            `-.`:::'_,'P  / `  \_| 
               `---'/:   (;  : 
                    `. : :   |           Congratulation !!!
                      `-.  ..|               Welcome to Torch_Project.
                         `.  | 
                           ):     
                           || 
                           || 
                           || 
                           || 
                           |' 
                           /' 
                          /| 
                         ( / 
                          ) 
                         | 
    """
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

        self._creat_code_dir()
        self._creat_data_dir()

        print(self.ascii_art)

    def _creat_code_dir(self):
        current_directory = os.path.join(self.path, self.directories[0])
        path1 = os.path.join(current_directory, "version1")
        path2 = os.path.join(current_directory, "version2")
        os.mkdir(path1)
        os.mkdir(path2)

        self.add_code(path1)
        self.add_code(path2)

    def _creat_data_dir(self):
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

        path1 = os.path.join(path, "model/mlp.py")
        with open(path1, "w") as fp:
            fp.write(code_content["model"])
        path1 = os.path.join(path, "model/mlp_train.py")
        with open(path1, "w") as fp:
            fp.write(code_content["modelTra"])
        path1 = os.path.join(path, "model/__init__.py")
        with open(path1, "w") as fp:
            fp.write("from .mlp_train import MlpTrainer")

        path1 = os.path.join(path, "data/demo_data.py")
        with open(path1, "w") as fp:
            fp.write(code_content["data"])
        path1 = os.path.join(path, "data/__init__.py")
        with open(path1, "w") as fp:
            fp.write("from .demo_data import load_dataset")


project = Project(project_name="Demo1")
project.creat_directory()

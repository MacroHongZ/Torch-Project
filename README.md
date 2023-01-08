# Torch-Project
A Python module for quickly creating a pytorch project from scratch.

# Introduction

This repository contains two project templates：`sample_project` AND `complete_project`. Each of these has a `Project` class in `project.py`.

To create a project:
```python
project = Project(project_name="Demo_Pro", path="path")
project.creat_directory()
```

The directory structure of the two project templates is as follows.

`sample_project`
```
├─code
│  ├─version1
│  │  │  main.py
│  │  │  utils.py
│  │  │
│  │  ├─data
│  │  │      data.py
│  │  │
│  │  ├─model
│  │  │      model.py
│  │  │
│  │  └─output_files
│  │      └─check_point
│  └─version2
├─data
│  ├─dataset1
│  └─dataset2
└─report
```

`complete_project`
```
├─code
│  ├─version1
│  │  │  main.py
│  │  │  utils.py
│  │  │
│  │  ├─data
│  │  │      demo_data.py
│  │  │      __init__.py
│  │  │
│  │  ├─model
│  │  │      mlp.py
│  │  │      mlp_train.py
│  │  │      __init__.py
│  │  │
│  │  └─output_files
│  │      └─check_point
│  └─version2
├─data
│  ├─dataset1
│  └─dataset2
└─report
```

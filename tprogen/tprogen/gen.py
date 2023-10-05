import toml
import os
from jinja2 import Template


def load(tfile):
# 读取TOML配置文件
    with open(tfile, "r") as file:
        config_data = file.read()

# 使用Jinja2模板渲染变量
    template = Template(config_data)
    rendered_config = template.render()

# 解析渲染后的TOML配置
    config = toml.loads(rendered_config)

    rendered_config = template.render(config)
    config = toml.loads(rendered_config)

# 打印解析后的配置
    return config


def generate_folder_structure(config, parent_path=""):
    for key, value in config.items():
        if isinstance(value, dict):
            folder_path = os.path.join(parent_path, key)
            os.makedirs(folder_path, exist_ok=True)
            generate_folder_structure(value, folder_path)
        else:
            file_path = os.path.join(parent_path, key)
            with open(file_path, "w") as file:
                file.write(value)

def test():
     # 读取TOML配置文件
    with open("resource/config.toml", "r") as file:
        config = toml.load(file)

# 生成文件夹结构
    generate_folder_structure(config["folder"],"tests")   

if __name__ == "__main__":
    test()
    

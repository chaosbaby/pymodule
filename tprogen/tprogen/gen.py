import toml
import os
from jinja2 import Template


def load(tfile, params = {}):
# 读取TOML配置文件
    with open(tfile, "r") as file:
        config_data = file.read()

# 使用Jinja2模板渲染变量
    template = Template(config_data)
    rendered_config = template.render()

# 解析渲染后的TOML配置
    config = toml.loads(rendered_config)

    rendered_config = template.render(config, **params)
    config = toml.loads(rendered_config)

# 打印解析后的配置
    return config

def __gen_struct(config, parent_path=""):

    os.makedirs(parent_path, exist_ok=True)
    for key, value in config.items():
        if isinstance(value, dict):
            folder_path = os.path.join(parent_path, key)
            os.makedirs(folder_path, exist_ok=True)
            __gen_struct(value, folder_path)
        else:
            file_path = os.path.join(parent_path, key)
            with open(file_path, "w") as file:
                file.write(value)

def generate(name="proj", template=None, **kwargs):
    settings = kwargs
    settings['name'] = name
    config = load(template, settings)
    __gen_struct(config['folder'], name)

import click

@click.command()
@click.option('--name', default="proj", help="project name", prompt="Project name")
@click.option('--ver', default="0.0.1", help="project version", prompt="Project version")
@click.option('--template', default="resource/config.toml", help="template path", prompt="template path")
@click.option('--requires', default="", help="pre requires", prompt="pre requires module") 
def gen(**kwargs):
    settings = kwargs
    print(settings)
    generate(**settings)
    
    
if __name__ == "__main__":
    gen()


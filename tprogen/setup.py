from setuptools import setup, find_packages
setup(
    name='tprogen',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    # package_data={
    #     '': ['resource/**/*']
    # },
    install_requires=[
        'click',
        'toml',
        'jinja2',
    ],
    entry_points="""
    [console_scripts]
    tgen = tprogen.gen:gen
    """,

    )

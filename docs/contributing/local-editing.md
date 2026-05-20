# Editing locally

To edit locally, you will have to install python on your computer. 
You can use `uv` to install python and then to manage this project.

First clone the repository:

```shell
git clone https://github.com/AntaresSimulatorTeam/antares-doc.git
cd antares-doc
```

If you want to create and sync a virtual environment with uv: 

```shell
uv venv
```

then activate it 

=== "Linux/MacOS"

    ```shell
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    .venv\Source\activate
    ```


Then sync the dependencies 

```shell
uv sync 
```

And now you are ready to edit pages ! You can preview the docs on your local machine 
by running `mkdocs serve` in your terminal. 
You will be able to open a preview of the doc in your browser. 
It will reload automatically when you change and save a file.

!!! bug
    If the site doesn't reload automatically on serve, try downgrading the click package from
    `click==8.3.0` to `click==8.2.1` (see [issue](https://github.com/mkdocs/mkdocs/issues/4032))

# Editing locally

To edit locally, you will have to install python on your computer. 

!!! note "Prerequisites"
    You need to have python >=3.11 installed on your machine.
    Python usually comes with the `pip` package manager. However, 
    you can also use `uv` to manage this project.

First clone the repository in a suitable folder:

```shell
git clone https://github.com/AntaresSimulatorTeam/antares-doc.git
cd antares-doc
```

## Set with `pip`

Create a virtual environment:

```shell
python -m venv .venv
```

and activate it

=== "Linux/MacOS"

    ```shell
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    .venv\Source\activate
    ```

Then install all the dependencies inside the virtual environment:

```
pip install .
```

## Set with `uv`

Alternatively, you can use [`uv`](https://docs.astral.sh/uv/) to manage this project
much faster.

If you want to create a virtual environment and install all the dependencies:

```shell
uv sync
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

## Use `mkdocs` to previsualize your changes

And now you are ready to edit pages ! You can preview the docs on your local machine 
by running `mkdocs serve` in your terminal. 
You will be able to open a preview of the doc in your browser. 
It will reload automatically when you change and save a file.



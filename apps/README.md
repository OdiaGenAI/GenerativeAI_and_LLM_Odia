# Translate to Indic Languages

This app helps in translating `.json` and `.jsonl` datasets from english to indian languages.

## Getting Started With Development

1. Ensure you meet the versions requirements, mentioned [here](#versions)

2. Install `pre-commit` library on your development setup

```bash
  pip3 install pre-commit
```

3. Prepping the environment - From the base directory of the repo execute the following commands:

```bash
  ./install.sh
```

4. Creating the config file

- Do remember that all entries to config file should be made without being surrounded by any quotes

- Create a file name `.config.ini` from the sample file `config.ini.sample`. More details about config file [here](#config-file).

5. Running app - From the base directory of the repo execute the following commands:

```bash
  ./translate-to-indic-lang/run.sh
```

6. The **output** folder, from the base directory of the repo.

```bash
  cd indicTrans/.work_dir/output/merged
  ls output.json
```

Any possible errors are logger under `indicTrans/.work_dir/output/translated/errors` as individual files.

### Config File

- **TARGET_URL** is the direct JSON/JSONL URL that could be gotten from **View Raw** feature for Git repos

- **TARGET_LANG** is the indian language that you are attempting to translate from. The possible values can be one below. Our provider continuosly update their models, the supported languages could be found [here](https://github.com/AI4Bharat/indicTrans).

| Indian Language | Language Code |
| :-------------: | :-----------: |
|    Assamese     |      as       |
|      Hindi      |      hi       |
|     Marathi     |      mr       |
|      Tamil      |      ta       |
|     Bengali     |      bn       |
|      Odia       |      or       |
|     Telugu      |      te       |
|    Gujarati     |      gu       |
|    Malayalam    |      ml       |
|     Punjabi     |      pa       |

- **MAX_PARALLEL_REQUESTS** the number of threads that could run in parallel to aid in translation

- **CLEAN_START** can be either **True** or **False**. If set to **False** when there are re-runs, you'll not lose your previous outputs. When set to **True**, and you run the app, it deletes the previous work directory and starts from scratch.

### Versions

| Package | Version |
| :-----: | :-----: |
|  wget   |   any   |
| Python  |   3.9   |

### Developer Hints

1. Check the number of files translated, when the app is still running. From the project's home directory run the following command.

```bash
  ls indicTrans/.work_dir/output/translated/data | wc -l
```

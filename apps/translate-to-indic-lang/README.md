# Translate to Indic Languages

This app helps in translating `.json` and `.jsonl` datasets from english to indian languages.

## Getting Started With Development

1. Install `pre-commit` library on your development setup

```bash
  pip3 install pre-commit
```

2. Prepping the environment - From the base directory of the repo execute the following commands:

```bash
  ./apps/install.sh
```

3. Creating the config file

- Do remember that all entries to config file should be made without being surrounded by any quotes

- Create a file name `.config.ini` from the sample file `config.ini.sample`. More details about config file [here](#config-file).

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

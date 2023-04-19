# Translate to Indic Language

This app helps in translating `.json` and `.jsonl` datasets from english to indian languages.

## Getting Started With Development

1. Install `pre-commit` library on your development setup

```bash
  pip3 install pre-commit
```

2. Prepping the environment

```bash
  ./apps/install.sh
```

3. Creating the config file

- Do remember that all entries to config file should be made without being surrounded by any quotes

- Create a file name `.config.ini` from the sample file `config.ini.sample`

- Fill the relevant informations:

  - **TARGET_URL** is the direct JSON URL that could be gotten from the raw github

  - **CLEAN_START** is specifically beneficial when there's re-runs, you'll not lose your previous outputs.

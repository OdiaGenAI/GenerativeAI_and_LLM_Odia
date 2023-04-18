#!/usr/bin/env bash

BASE_DIR="$(dirname "$(realpath "$0")")"
SCRIPTS_DIR="$(dirname "$(dirname "$(realpath "$0")")")"
PROJECT_DIR="$(dirname "$(dirname "$(realpath "${BASE_DIR}")")")"
ENV_NAME=".odiagenai"

copy_required_files()
{
    echo "Copying required files ..."
    # cp ${SCRIPTS_DIR}/translations/sample.py ${PROJECT_DIR}/indicTrans
    cp ${SCRIPTS_DIR}/app/*.py ${PROJECT_DIR}/indicTrans
    cp ${SCRIPTS_DIR}/app/.config.ini ${PROJECT_DIR}/indicTrans 2>/dev/null
}

activate_virtual_environment()
{
    echo "Activating virtual environment ..."
    source ${PROJECT_DIR}/${ENV_NAME}/bin/activate
}

copy_required_files
activate_virtual_environment
cd ${PROJECT_DIR}/indicTrans
# python3 sample.py
python3 translate_to_indic_lang.py

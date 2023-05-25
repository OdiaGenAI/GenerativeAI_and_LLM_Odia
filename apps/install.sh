#!/usr/bin/env bash

BASE_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR="$(dirname "$(realpath "${BASE_DIR}")")"
MODEL_FILENAME="en2indic.zip"
ENV_NAME=".odiagenai"

cleanup()
{
    echo "Cleaning up ..."
    if [ -d "${PROJECT_DIR}/${ENV_NAME}" ] 
    then
        source ${PROJECT_DIR}/${ENV_NAME}/bin/activate
        deactivate
    fi 

    rm -rf ${PROJECT_DIR}/${ENV_NAME} || true
    rm -rf ${PROJECT_DIR}/indicTrans || true
    rm -rf ${PROJECT_DIR}/en-indic || true
}

create_virtual_environment()
{
    echo "Creating virtual environment ..."
    python3.9 -m venv ${PROJECT_DIR}/${ENV_NAME}
    source ${PROJECT_DIR}/${ENV_NAME}/bin/activate
    deactivate
}

clone_repos()
{
    echo "Starting to clone repos ..."
    cd ${PROJECT_DIR}
    git clone https://github.com/AI4Bharat/indicTrans.git 
    
    cd ${PROJECT_DIR}/indicTrans
    rm -rf ${PROJECT_DIR}/indicTrans/.git
    git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
    git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
    git clone https://github.com/pytorch/fairseq.git
}

install_deps()
{
    echo "Installing dependencies ..."
    source ${PROJECT_DIR}/${ENV_NAME}/bin/activate
    python3 -m pip install --upgrade pip
    pip3 install -r ${PROJECT_DIR}/pip-requirements.txt --no-cache-dir
    export INDIC_RESOURCES_PATH=${PROJECT_DIR}/indicTrans/indic_nlp_resources
    cd ${PROJECT_DIR}/indicTrans/indic_nlp_library
    python3 -m pip install ./
    cd ${PROJECT_DIR}/indicTrans/fairseq
    python3 -m pip install ./
}

download_and_unzipmodel()
{
    echo "Fetching Model ..."
    if [ ! -f "${PROJECT_DIR}/${MODEL_FILENAME}" ] 
    then
        echo "Unavailable on your local, need to download."
        wget https://ai4b-public-nlu-nlg.objectstore.e2enetworks.net/en2indic.zip -O ${PROJECT_DIR}/${MODEL_FILENAME}
    fi
    echo "Unzipping Model ..."
    unzip ${PROJECT_DIR}/${MODEL_FILENAME} -d ${PROJECT_DIR}
}

cleanup
create_virtual_environment
clone_repos
install_deps
download_and_unzipmodel

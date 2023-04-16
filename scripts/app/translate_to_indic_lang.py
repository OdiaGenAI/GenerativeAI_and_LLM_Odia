#!../venv/bin/python3
"""translate_to_indic_lang - translates to indic languages"""

import sys

sys.path.append("../")
from helpers import Helpers
from indicTrans.inference.engine import Model


class TranslateToIndicLang:
    def __init__(self) -> None:
        """Init Function for class"""
        self.en2indic_model = None
        self.helperFuncs = Helpers()

    def __clone_repos_and_install_deps(self) -> None:
        """Clone Repos and Install Deps"""
        self.helperFuncs.execute_shell_command(
            "git clone https://github.com/AI4Bharat/indicTrans.git"
        )
        self.helperFuncs.execute_shell_command(
            "cd indicTrans && git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git"
        )
        self.helperFuncs.execute_shell_command(
            "cd indicTrans && git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git"
        )
        self.helperFuncs.execute_shell_command(
            "cd indicTrans && git clone https://github.com/rsennrich/subword-nmt.git"
        )
        self.helperFuncs.execute_shell_command(
            "git clone https://github.com/pytorch/fairseq.git"
        )
        self.helperFuncs.execute_shell_command("cd fairseq && pip install ./")

    def __download_model(self) -> None:
        """Downloads Model"""
        self.helperFuncs.execute_shell_command(
            "curl https://ai4b-public-nlu-nlg.objectstore.e2enetworks.net/en2indic.zip --output en2indic.zip && unzip en2indic.zip"
        )

    def __get_model(self) -> None:
        """Instantiate Model"""
        self.en2indic_model = Model(expdir="./en-indic")

    def run(self):
        # self.__clone_repos_and_install_deps()
        # self.__download_model()
        self.__get_model()


TranslateToIndicLang().run()

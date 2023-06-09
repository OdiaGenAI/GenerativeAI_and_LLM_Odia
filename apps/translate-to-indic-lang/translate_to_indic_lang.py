#!../venv/bin/python3
"""translate_to_indic_lang - translates to indic languages"""

import os
import json
import sys

from concurrent.futures import ThreadPoolExecutor

from helpers import Helpers
from inference.engine import Model


class TranslateToIndicLang:
    def __init__(self) -> None:
        """Init Function for class"""
        self.model = None
        self.helperFuncs = Helpers()
        self.SRC_LANG = "en"
        self.cfg = self.helperFuncs.read_configfile(".config.ini")
        self.__set_variables()

    def __check_supported_file_ext(self) -> None:
        """Checks for supported file extensions"""
        if self.TARGET_URL.endswith(".json"):
            self.INPUT_FILETYPE = "JSON"
            self.INPUT_FILENAME = "input.json"
        elif self.TARGET_URL.endswith(".jsonl"):
            self.INPUT_FILETYPE = "JSONL"
            self.INPUT_FILENAME = "input.jsonl"
        else:
            print("Please check TARGET_URL, supported file types are - .json, .jsonl")
            sys.exit(1)

    def __set_variables(self) -> None:
        """Sets variables to be used"""
        self.CLEAN_START = self.cfg["APP"].getboolean("CLEAN_START")
        self.TARGET_URL = self.cfg["APP"].get("TARGET_URL")
        self.TARGET_LANG = self.cfg["APP"].get("TARGET_LANG")
        self.MAX_PARALLEL_REQUESTS = self.cfg["APP"].get("MAX_PARALLEL_REQUESTS")
        self.WORK_DIR = os.getcwd() + "/" + ".work_dir"
        self.OUTPUT_FOLDERNAME = "output"
        self.__check_supported_file_ext()
        self.MERGED_OUTPUT_FILENAME = "output.json"
        self.INPUT_FILELOC = self.WORK_DIR + "/" + self.INPUT_FILENAME
        self.OUTPUT_FOLDERLOC = self.WORK_DIR + "/" + self.OUTPUT_FOLDERNAME
        self.TRANSLATED_OUTPUT_DATA_LOC = self.OUTPUT_FOLDERLOC + "/translated/data"
        self.TRANSLATED_OUTPUT_ERR_LOC = self.OUTPUT_FOLDERLOC + "/translated/error"
        self.MERGED_OUTPUT_LOC = self.OUTPUT_FOLDERLOC + "/" + "merged"
        self.MERGED_OUTPUT_FILENAME = (
            self.MERGED_OUTPUT_LOC + "/" + self.MERGED_OUTPUT_FILENAME
        )

    def __initiate_model(self) -> None:
        """Instantiate Model"""
        self.model = Model(expdir="../en-indic")

    def __cleanup(self) -> None:
        """Cleanup work environment"""
        print("Initiating Cleanup ...")
        self.helperFuncs.execute_shell_command("rm -rf " + self.WORK_DIR)

    def __create_work_env(self) -> None:
        """Building work environment"""
        print("Creating work environment ...")
        self.helperFuncs.execute_shell_command("mkdir -p " + self.WORK_DIR)
        self.helperFuncs.execute_shell_command("mkdir -p " + self.OUTPUT_FOLDERLOC)
        self.helperFuncs.execute_shell_command(
            "mkdir -p " + self.TRANSLATED_OUTPUT_DATA_LOC
        )
        self.helperFuncs.execute_shell_command(
            "mkdir -p " + self.TRANSLATED_OUTPUT_ERR_LOC
        )
        self.helperFuncs.execute_shell_command("mkdir -p " + self.MERGED_OUTPUT_LOC)

    def __download_target(self) -> None:
        """Downloading target"""
        print("Downloading target ...")
        self.helperFuncs.execute_shell_command(
            "curl -L "
            + self.TARGET_URL
            + " --output "
            + self.WORK_DIR
            + "/"
            + self.INPUT_FILENAME
        )

    def __read_input_file(self) -> list:
        """Collecting meta information about data"""
        data = []

        if self.INPUT_FILETYPE == "JSON":
            with open(self.INPUT_FILELOC, "r") as f:
                data = json.load(f)
        elif self.INPUT_FILETYPE == "JSONL":
            with open(self.INPUT_FILELOC, "r") as f:
                data = [json.loads(line) for line in f]
        return data

    def __initialize_setup(self) -> None:
        """initializing setup"""
        if (not os.path.exists(self.WORK_DIR)) and (not self.CLEAN_START):
            self.__cleanup()
            self.__create_work_env()
            self.__download_target()
            os.environ["PYTHONPATH"] = os.getcwd() + "/fairseq/"

    def translate_text(self, value) -> str:
        """translate text from source to target language"""
        if "\n" in value:
            replace_dn = value.replace("\n\n", "\n")
            split_lines = replace_dn.splitlines()
            text_splits = self.model.batch_translate(
                split_lines, self.SRC_LANG, self.TARGET_LANG
            )
            response = "\n".join(text_splits)
        else:
            response = self.model.translate_paragraph(
                value, self.SRC_LANG, self.TARGET_LANG
            )
        return response.strip()

    def translate_item(self, item) -> dict:
        """translate item"""
        translated_item = {}
        for key, value in item.items():
            if value:
                # To handle when value is a list
                if isinstance(value, list):
                    value = "\n".join(value)

                translated_value = self.translate_text(value)
                translated_item[key] = translated_value
                translated_item["english_" + key] = value
            else:
                translated_item[key] = ""
                translated_item["english_" + key] = ""
        return translated_item

    def save_item(self, item, filename) -> None:
        """Save translated file"""
        with open(filename, "w") as f:
            json.dump(item, f, ensure_ascii=False, indent=4)

    def translate_and_save(self, item, i) -> None:
        """translating and saving to file"""
        output_fname = self.TRANSLATED_OUTPUT_DATA_LOC + "/" + f"translated_{i}.json"
        failure_fname = (
            self.TRANSLATED_OUTPUT_ERR_LOC + "/" + f"error_in_translation_{i}.txt"
        )
        if os.path.isfile(output_fname) or os.path.isfile(failure_fname):
            return

        print("Evaluating element number - " + f"{i}")

        try:
            translated_item = self.translate_item(item)
            self.save_item(translated_item, output_fname)
            print("Successfully translated - " + output_fname)
        except Exception as e:
            print(e)
            print("Error in translation - " + f"error_in_translation_{i}.txt")
            with open(
                failure_fname,
                "a",
            ) as f:
                f.write(repr(e))

    def merge_json_files(self, data_cnt) -> None:
        merged_data = []
        for i in range(data_cnt):
            file_path = os.path.join(
                self.TRANSLATED_OUTPUT_DATA_LOC, f"translated_{i}.json"
            )

            if not os.path.isfile(file_path):
                continue

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                merged_data.append(data)

        with open(self.MERGED_OUTPUT_FILENAME, "w", encoding="utf-8") as file:
            json.dump(merged_data, file, indent=2, ensure_ascii=False)

    def run_translation(self) -> int:
        """Runs the translation code"""
        data = self.__read_input_file()
        data_cnt = len(data)
        print("Working with - " + str(data_cnt) + " elements ...")

        with ThreadPoolExecutor(
            max_workers=int(self.MAX_PARALLEL_REQUESTS)
        ) as executor:
            {
                executor.submit(self.translate_and_save, item, i)
                for i, item in enumerate(data)
            }

        # for i in data:
        #     self.translate_and_save(i, data.index(i))

        return data_cnt

    def run(self) -> None:
        """Runs the app"""
        self.__initialize_setup()
        self.__initiate_model()
        data_cnt = self.run_translation()
        self.merge_json_files(data_cnt)


TranslateToIndicLang().run()

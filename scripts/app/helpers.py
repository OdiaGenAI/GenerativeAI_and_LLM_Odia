"""Helpers - hosts all helper functions"""
#!../venv/bin/python3

import configparser, subprocess, sys


class Helpers:
    """Helpers - hosts all helper functions"""

    def __init__(self) -> None:
        pass

    def read_configfile_section(self, filename, section):
        """Reads a particular section from a config file"""
        try:
            config = configparser.ConfigParser(interpolation=None)
            with open(filename, encoding="utf8") as cfg_file:
                config.read_file(cfg_file)
            return config[section]
        except FileNotFoundError as fnf:
            print(
                "Config file not found. Please create a .config.ini file under scripts/app"
            )
            sys.exit(1)

    def read_configfile(self, filename):
        """Reads an entire config file"""
        try:
            config = configparser.ConfigParser(interpolation=None)
            with open(filename, encoding="utf8") as cfg_file:
                config.read_file(cfg_file)
            return config
        except FileNotFoundError as fnf:
            print(
                "Config file not found. Please create a .config.ini file under scripts/app"
            )
            sys.exit(1)

    def execute_shell_command(self, cmd):
        """Executes shell command"""
        print("Executing shell command - " + cmd)
        output = subprocess.run(cmd, shell=True, check=True, capture_output=True)
        return output

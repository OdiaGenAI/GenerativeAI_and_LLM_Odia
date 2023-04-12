"""Helpers - hosts all helper functions"""
#!../venv/bin/python3

import configparser, subprocess


class Helpers:
    """Helpers - hosts all helper functions"""

    def __init__(self) -> None:
        pass

    def read_configfile_section(self, filename, section):
        """Reads a particular section from a config file"""
        config = configparser.ConfigParser(interpolation=None)
        with open(filename, encoding="utf8") as cfg_file:
            config.read_file(cfg_file)
        cfg = dict(config[section].items())
        return cfg

    def read_configfile(self, filename):
        """Reads an entire config file"""
        config = configparser.ConfigParser(interpolation=None)
        with open(filename, encoding="utf8") as cfg_file:
            config.read_file(cfg_file)
        return config

    def execute_shell_command(self, cmd):
        """Executes shell command"""
        print("Executing shell command - " + cmd)
        output = subprocess.run(cmd, shell=True, check=True, capture_output=True)
        return output

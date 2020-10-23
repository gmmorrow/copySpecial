#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Gabrielle, jazmyne, python documentation"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    special_paths = []
    for filename in os.listdir(dirname):
        match = re.search(r'__\w+__', filename)
        if match:
            special_paths.append(os.path.abspath(
                os.path.join(dirname, filename)))
    return special_paths


def create_dir(path):
    """Check to see if dir exists"""
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError:
            print(f"Creation of dir {path} failed")
            return False
    return True


def copy_to(path_list, dest_dir):
    """shows path list and directory, copies to destination"""
    # if not os.path.isdir(dest_dir):
    #     os.makedirs(dest_dir)
    # for path in path_list:
    #     shutil.copy(path, dest_dir)
    #     return
    create_dir_status = create_dir(dest_dir)
    if not create_dir_status:
        return
    for f in path_list:
        shutil.copyfile(f, os.path.join(dest_dir, os.path.basename(f)))


def zip_to(path_list, dest_zip):
    """copies destinations if exists"""
    print("Command im going to do:")
    for path in path_list:
        print(f'zip -j {dest_zip}')
        subprocess.run(['zip', '-j', dest_zip, path])
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dest zipfile for special files')

    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    if not ns:
        sys.exit(1)
    special_paths = get_special_paths(ns.from_dir)

    # Your code here: Invoke (call) your functions
    if ns.todir:
        copy_to(special_paths, ns.todir)
    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    if not ns.todir and not ns.tozip:
        print(*special_paths, sep='\n')


if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python
import os
import subprocess
import sys
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except FileNotFoundError:
        pass

def remove_dir(dirpath):
    try:
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))
    except FileNotFoundError:
        pass 

def execute(*args, supress_exception = False, cwd=None):
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        proc = subprocess.Popen(args, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

        out, err = proc.communicate()
        out = out.decode('utf-8')
        err = err.decode('utf-8')
        if err and not supress_exception:
            raise Exception(err)
        else:
            return out
    finally:
        os.chdir(cur_dir)


def init_git():
    # workaround for issue #1
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute("git", "config", "--global", "init.defaultBranch", "main", cwd = PROJECT_DIRECTORY)
        execute("git", "init", cwd=PROJECT_DIRECTORY)



if __name__ == '__main__':

    try:
        init_git()
    except Exception as e:
        print(e)

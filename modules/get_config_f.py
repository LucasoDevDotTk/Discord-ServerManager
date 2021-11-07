"""
MIT License

Copyright (c) 2021 lucaso60
Copyright (c) 2021 LEL Studios
Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present Pycord Development

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os 
import json

from functions.functions import time_now


def get_config(CONFIG_FOLDER_PATH):
    if os.path.exists(CONFIG_FOLDER_PATH):

        with open(CONFIG_FOLDER_PATH) as f:
            config_data = json.load(f)
            return config_data
    else:
        config_temp = {"Token": "", "Debug_id": ""}

        with open(CONFIG_FOLDER_PATH, "w+") as f:
            json.dump(config_temp, f)

        print(f"{time_now()} Config file not found, creating one...")
        print(f"{time_now()} Please close the program and fill the config file with your token and debug id.")
        exit()

#!/usr/bin/env python3

# jsonVal01
# Invoke by: jsonVal01 <JSONFilename>
# Checks validity of JSON file by JSON Decoder.
# Original Creation: 10MAR21
# Released under Apache 2.0 License

import json
import sys

with open(sys.argv[1]) as file:
    try:
        json.load(file)  # Attempt to assign JSON-data to a var
    except json.decoder.JSONDecodeError:
        print("Invalid JSON data. Exiting.")
        raise  # If data is invalid, send error.
    else:
        print("JSON data is valid. Exiting.")  # in case json is valid

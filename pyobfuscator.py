# -*- coding: utf-8 -*-
import json
import os
import requests

# leveraging post function from obfuscator.io

class PyObfuscator:
    def obfuscate(self, lines):
        print("obfuscate related js files")
        response = requests.post("https://obfuscator.io/obfuscate", json=
            {
                "code": lines, 
                "options": {
                    "compact": True,
                    "controlFlowFlattening": False,
                    "controlFlowFlatteningThreshold": 0.75,
                    "deadCodeInjection": False,
                    "deadCodeInjectionThreshold": 0.4,
                    "debugProtection": False,
                    "debugProtectionInterval": False,
                    "disableConsoleOutput": False,
                    "domainLock": [],
                    "identifierNamesGenerator": "hexadecimal",
                    "identifiersPrefix": "",
                    "renameGlobals": False,
                    "reservedNames": [],
                    "reservedStrings": [],
                    "rotateStringArray": True,
                    "rotateStringArrayEnabled": True,
                    "seed": 0,
                    "selfDefending": False,
                    "sourceMap": False,
                    "sourceMapBaseUrl": "",
                    "sourceMapFileName": "",
                    "sourceMapMode": "off",
                    "sourceMapSeparate": False,
                    "stringArray": True,
                    "stringArrayEncoding": False,
                    "stringArrayEncodingEnabled": True,
                    "stringArrayThreshold": 0.8,
                    "stringArrayThresholdEnabled": True,
                    "target": "browser",
                    "transformObjectKeys": False,
                    "unicodeEscapeSequence": False
                }
            }
        )
        
        lines = json.loads(response.text)["code"]
    return lines

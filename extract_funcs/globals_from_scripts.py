from collections import defaultdict
import json
from pathlib import Path
import re
from threading import local

NS_MODS = Path("path/to/Titanfall2/R2Northstar/mods")
NATIVE_SCRIPTS = Path("path/to/assets_dump/scripts/vscripts")
SCRIPTS_JSON = "path/to/ModdingDocs/extract_funcs/scripts.json"
CONSTS_DUMP_JSON = "path/to/ModdingDocs/extract_funcs/globals.json"

# Layers of vscripts, topmost is overwritten by below
VSCRIPT_LAYERS = [
    (
        "Titanfall 2",
        NATIVE_SCRIPTS
    ),
    (
        "Northstar.CustomServers",
        NS_MODS / "Northstar.CustomServers/mod/scripts/vscripts",
    ),
    ("Northstar.Coop", NS_MODS / "Northstar.Coop/mod/scripts/vscripts"),
    ("Northstar.Custom", NS_MODS / "Northstar.Custom/mod/scripts/vscripts"),
    ("Northstar.Client", NS_MODS / "Northstar.Client/mod/scripts/vscripts"),
]


def get_layer(filename):
    for name, layer in reversed(VSCRIPT_LAYERS):
        path = layer / filename
        if path.exists():
            return path, name
    raise FileNotFoundError(f"Could not locate {filename} in any layer.")


def openl(filename: str, mode="r", encoding="utf-8"):
    path, name = get_layer(filename)
    if path:
        return name, path.open(mode, encoding=encoding, errors="ignore")

def is_generic_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_float_number(s):
    if s[0] == '-' or is_generic_number(s[0]):
        if('.' in s):
            return "float"
        else:
            return "int"

with open(SCRIPTS_JSON) as f:
    scripts = json.load(f)

sl_cmnt = re.compile(r"\/\/.*")

def runon_parse(inp: str):
    try:
        inp, additional = inp.split("&&")
        additional = " &&" + additional
    except ValueError:
        additional = ""
    runons = inp.split("||")
    runons = [r.strip(" \n()") + additional for r in runons]
    return runons


funcs = defaultdict(list)

for runon, filelist in scripts.items():
    runons = runon_parse(runon)
    if "CONSOLE_PROG" in runon:
        continue
    for filename in filelist:
        try:
            found_in, fp = openl(filename)
            with fp as f:
                ml_comment_depth = 0
                global_all = False
                runons_mod = []
                globalized_funcs = []
                for line in f:
                    line = line.removesuffix("\n")
                    # comment skipping
                    line = sl_cmnt.sub("", line)
                    if "/*" in line:
                        ml_comment_depth += 1
                        line = line.split("/*")[0]
                    elif "*/" in line:
                        ml_comment_depth -= 1
                        line = line.split("*/")[1]
                    elif ml_comment_depth > 0:
                        continue

                    # preproc conditions
                    if "#if" in line:
                        runon_modifier = line.strip().replace("#if ", "")
                        runons_mod = runon_parse(runon_modifier)
                    if "#elseif" in line:
                        runon_modifier = line.strip().replace("#elseif ", "")
                        runons_mod = runon_parse(runon_modifier)
                    if "#endif" in line:
                        runon_modifier = ""
                        runons_mod = []

                    if line.startswith("global "):
                        line = ' '.join(line.expandtabs(1).split())
                        if '<' in line and '>' in line:
                            prev: str = line[:line.find('<')]
                            after: str = line[line.find('>'):]
                            between: str = line[line.find('<'):line.find('>')].replace(' ', '')
                            line = prev + between + after
                        l: list = line.split(" ")
                        constant:bool = False
                        push:int = 0
                        type:str = ""
                        name:str = ""
                        value:str = ""
                        if l[1] == "function":
                            continue
                        if l[1] == "const":
                            constant = True
                            push = 1
                        type = l[1+push]
                        name = l[2+push]
                        if name == "=":
                            name = type
                            type = "unknown"
                        if "=" in l and l[len(l)-1] != "=":
                            value = l[l.index("=") + 1]
                            if value.startswith("\""):
                                type = "string"
                            if value.startswith("$"):
                                type = "asset"
                            if value.startswith("{"):
                                type = "table"
                            if value.startswith("["):
                                type = "array"
                            if value.startswith("<"):
                                type = "vector"
                            if value.startswith("Vector("):
                                type = "vector"
                            if value.startswith("false") or value.startswith("true"):
                                type = "bool"
                            if is_generic_number(value):
                                if "." in value:
                                    type = "float"
                                else:
                                    type = "int"
                            if value.startswith("0x"): # respawn uses hex addresses only for flags afaik
                                type = "int"
                            if "<<" in value or ">>" in value: # respawn bit shifting only for flags afaik
                                type = "int"
                        local_params = {}
                        local_params["name"] = name
                        local_params["type"] = type
                        if constant:
                            local_params["constant"] = constant
                        if len(value):
                            local_params["value"] = value
                        local_params["foundin"] = found_in
                        local_params["runon"] = runons_mod or runons
                        # funcs[str(runons_mod or runons)].append(local_params)
                        funcs["globals"].append(local_params)

        except FileNotFoundError:
            print("\n=====\nFile not found: " + filename + "\n=====\n")

with open(CONSTS_DUMP_JSON, "w") as f:
    json.dump(funcs, f)

import json

data = {}

GLOBALS_JSON = "path/to/globals.json"
UI_P = "path/to/globals_ui.rst"
CLIENT_P = "path/to/globals_client.rst"
SERVER_P = "path/to/globals_server.rst"

with open(GLOBALS_JSON, "r") as f:
    data = json.load(f)

globals_server = []
globals_client = []
globals_ui = []

for gl in data["globals"]:
    r: list = gl["runon"]
    if "SERVER" in r:
        globals_server.append(gl)
    if "CLIENT" in r:
        globals_client.append(gl)
    if "UI" in r:
        globals_ui.append(gl)


def writeBulletPoints(f, gl):
    if "constant" in gl and gl["constant"] == True:
        f.write(".. note::\n\n\t" + gl["name"] + " is constant\n\n")

    if "type" in gl:
        f.write(bulletPoint("type", gl["type"]))
    if "value" in gl:
        f.write(bulletPoint("value", gl["value"]))
    # if "constant" in gl:
    # 	f.write(bulletPoint("constant", gl["constant"]))


def bulletPoint(tp: str, val: str):
    return f"* {tp}: {val}\n\n"


with open(SERVER_P, "w") as f:
    f.write("SERVER Globals\n=====\n")
    for gl in globals_server:
        f.write("\n``" + gl["name"] + "``\n^^^^^^^^^^\n\n")
        writeBulletPoints(f, gl)

with open(CLIENT_P, "w") as f:
    f.write("CLIENT Globals\n=====\n")
    for gl in globals_client:
        f.write("\n``" + gl["name"] + "``\n^^^^^^^^^^\n\n")
        writeBulletPoints(f, gl)

with open(UI_P, "w") as f:
    f.write("UI Globals\n=====\n")
    for gl in globals_ui:
        f.write("\n``" + gl["name"] + "``\n^^^^^^^^^^\n\n")
        writeBulletPoints(f, gl)

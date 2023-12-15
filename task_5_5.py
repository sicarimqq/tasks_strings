import json
from pprint import pprint

with open("template.json") as f:
    file_content = f.read()
    template = json.loads(file_content)

pprint(template)
model = template
print("-----------------------------------------------------------------")
for switch in model.keys():
    if model[switch]["10/100Mbps"] == "5x" and \
            model[switch]["MAC address entries"] == "2k":
        pprint(model[switch])

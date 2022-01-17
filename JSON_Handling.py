import json
with open("CPSC_catalog.json", "r") as f:
    data = json.load(f)


with open("course_plan.json", "r") as f:
    plan_data = json.load(f)

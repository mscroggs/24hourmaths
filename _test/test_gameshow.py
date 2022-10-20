import os
import re


def test_duplicate_people():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../game-show-2.md")) as f:
        data = f.read()

    people = {}

    for i in data.split("{% include _gameperson.html ")[1:]:
        i = i.split("%}")[0]
        info = {i: j for i, j in re.findall(r"([^ ]+)=\"([^\"]*)\"",i)}

        if info["name"] in people:
            assert people[info["name"]] == info
        else:
            people[info["name"]] = info

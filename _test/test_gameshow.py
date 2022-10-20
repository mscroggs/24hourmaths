import os
import re
import pytest

names = set()
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../game-show-2.md")) as f:
    data = f.read()

for i in data.split("{% include _gameperson.html ")[1:]:
    i = i.split("%}")[0]
    info = {i: j for i, j in re.findall(r"([^ ]+)=\"([^\"]*)\"",i)}

    names.add(info["name"])


@pytest.mark.parametrize("name", names)
def test_duplicate_people(name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../game-show-2.md")) as f:
        data = f.read()

    pinfo = None

    for i in data.split("{% include _gameperson.html ")[1:]:
        i = i.split("%}")[0]
        info = {i: j for i, j in re.findall(r"([^ ]+)=\"([^\"]*)\"",i)}

        if info["name"] == name:
            if pinfo is None:
                pinfo = info

            assert pinfo == info

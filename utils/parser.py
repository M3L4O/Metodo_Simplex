import numpy as np
import re


class Problem:
    def __init__(self, obj_func, restrictions) -> None:
        self.obj_func = obj_func
        self.restrictions = restrictions

    def parser(self):
        if self.obj_func.casefold().startswith("max"):
            self.direction = "max"
        else:
            self.direction = "min"

        self.obj_func = (
            self.obj_func.casefold().replace(self.direction, "").replace(":", "")
        )
        self.obj_func = re.sub("x.", "", self.obj_func)
        self.obj_func = re.split(r"[+]", self.obj_func)
        self.obj_func = [float(element) for element in self.obj_func]

        for index in range(len(self.restrictions)):
            if re.findall(r"[\=]", self.restrictions[index]):
                self.restrictions[index] = [
                    float(element)
                    for element in re.split(
                        r"[\+\=]", re.sub("x.", "", self.restrictions[index])
                    )
                    if element not in ("", " ")
                ]

    def standard_form(self):
        self.parser()
        return self.obj_func, self.restrictions, self.direction


if __name__ == "__main__":
    pb = Problem("Max: 2x1+10x2", ["10x1+2x2 + 1x3 = 10"])
    print(pb.standard_form())

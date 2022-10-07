import numpy as np
import pandas as pd


class Tableau:
    def __init__(self, objective_func: np.ndarray, restrictions: np.ndarray) -> None:
        self.restrictions = restrictions
        self.length = len(restrictions[0]) - 1
        diff_len = len(restrictions[0]) - len(objective_func)
        self.objective_func = np.append(objective_func, [0] * diff_len)

        self.bases = [
            index
            for index in range(self.length)
            if np.sum(self.restrictions[:, index]) + self.objective_func[index] == 1
        ]

    def __repr__(self):
        table = dict()
        for index in range(self.length):
            table[f"X_{index+1}"] = np.append(
                self.restrictions[:, index], self.objective_func[index]
            )
        table["b"] = np.append(self.restrictions[:, -1], self.objective_func[-1])
        df = pd.DataFrame(
            table, index=[f"X_{index+1}" for index in self.bases] + ["FO"]
        )

        return df.to_string()


if __name__ == "__main__":
    OF = np.array([1, 2])
    restrictions = np.array([[3, 2, 1, 0, 10], [1, 2, 0, 1, 12]])
    tb = Tableau(OF, restrictions)
    print(tb)

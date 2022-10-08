import numpy as np
import pandas as pd


class Tableau:
    def __init__(self, obj_func: np.ndarray, restrictions: np.ndarray):

        pd.options.display.float_format = "{:.1f}".format

        self.restrictions = restrictions
        self.height, self.length = restrictions.shape

        diff_len = self.length - len(obj_func)
        self.obj_func = np.append(obj_func, [0] * diff_len) * -1

        self.bases = [
            index
            for index in range(self.length - 1)
            if np.sum(self.restrictions[:, index]) + self.obj_func[index] == 1
        ]

    def is_great_solution(self):
        return np.all(self.obj_func >= 0)

    def unlimited_solution(self, column):
        return np.all(self.restrictions[:, column] <= 0)

    def get_minimizer_column(self):
        return np.argmin(self.obj_func)

    def get_base_to_getout(self, column):
        divisions = dict()
        for row in range(self.height):
            if self.restrictions[row, column] > 0:
                divisions[row] = (
                    self.restrictions[row, -1] / self.restrictions[row, column]
                )
        print(divisions)
        return min(divisions, key=divisions.get)

    def calculate_new_rows(self, row, column):
        for _row in range(self.height):
            if _row != row:
                factor = (
                    self.restrictions[_row, column] / self.restrictions[row, column]
                )
                self.restrictions[_row, :] -= factor * self.restrictions[row, :]
        factor = self.obj_func[column] / self.restrictions[row, column]
        self.obj_func -= factor * self.restrictions[row, :]
    
    def solution(self):
        _vars = [0]*(self.length-1)
        for row, base in enumerate(self.bases):
            _vars[base] = self.restrictions[row, -1] 
        return _vars

    def solver(self):
        while not self.is_great_solution():
            column = self.get_minimizer_column()
            if self.unlimited_solution(column):
                return self.solution(), "Ilimitada"


            row = self.get_base_to_getout(column)

            print(self, end="\n\n")
            self.restrictions[row, :] /= self.restrictions[row, column]

            print(
                f"Variavel a entrar: X_{column}\nVariavel a sair: X_{self.bases[row]}"
            )
            self.bases[row] = column
            self.calculate_new_rows(row, column)
        else:
            return self.solution(), "Limitada"

    def __repr__(self):
        table = dict()
        for index in range(self.length - 1):
            table[f"X_{index}"] = np.append(
                self.restrictions[:, index], self.obj_func[index]
            )
        table["b"] = np.append(self.restrictions[:, -1], self.obj_func[-1])
        df = pd.DataFrame(table, index=[f"X_{index}" for index in self.bases] + ["FO"])

        return df.to_string()


if __name__ == "__main__":
    OF = np.array([5, 2, 0, 0, 0], dtype=np.float64)
    restrictions = np.array(
        [[1, 0, 1, 0, 0, 3], [0, 1, 0, 1, 0, 4], [4, 3, 0, 0, 1, 12]], dtype=np.float64
    )
    tb = Tableau(OF, restrictions)
    print(tb.solver())

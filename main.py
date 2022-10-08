import numpy as np
from utils.parser import Problem
from utils.tableau import Tableau


def main():
    explain = """
A entrada do programa deve ser a função objetiva seguida das restrições já na forma padrão. SEMPRE com o coeficiente antecedendo a variável, mesmo que este seja 0 ou 1.
Ex:.
Para um PPL:
Max z = 10x1 + 20x2

Suj a:

x1 + 2x2 <=10
x1 + 3x2 <=20

Entrada no programa:

Max: 10x1 + 20x2
1x1 + 2x2 + 1x3 + 0x4 = 10
1x1 + 3x2 + 0x3 +1x4 = 20


"""
    print(explain)
    infos = []
    print("Digite a entrada acima demonstrada:")

    while True:
        info = input()
        if info == "":
            break

        infos.append(info)

    problem = Problem(infos[0], infos[1:])
    obj_func, restrictions, direction = problem.standard_form()
    tab = Tableau(np.array(obj_func), np.array(restrictions), direction)
    tab.solver()


if __name__ == "__main__":
    main()

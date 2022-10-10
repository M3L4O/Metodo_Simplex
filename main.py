import numpy as np
from utils.parser import Problem
from utils.tableau import Tableau


def main():
    explain = """
A entrada do programa deve ser a função objetiva seguida das restrições já na FORMA PADRÃO. SEMPRE com o coeficiente antecedendo a variável, mesmo que este seja 0 ou 1, caso o coeficiente seja negativo, ainda usa-se o operador "+",  enquanto que a variável tem nomes xi para i = 1...n.
Ex:.
Para um PPL:
Min z = -5x1 - 2x2

Suj a:

x1 <= 3
x2 <= 4
x1 + 2x2 <= 9

x1, x2 >= 0
Entrada no programa:
min:-5x1 + -2x2
1x1 + 0x2 + 1x3 + 0x4 + 0x5 = 3
0x1 + 1x2 + 0x3 + 1x4 + 0x5 = 4
1x1 + 2x2 + 0x3 + 0x4 + 1x5 = 9
<-- Por fim um ENTER
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
    _vars, type = tab.solver()
    print(f"X = {_vars[0]}, Z = {float(_vars[1])}, Solução {type}")
    
    _ = input("Tecle enter para encerrar: ") 
if __name__ == "__main__":
    main()

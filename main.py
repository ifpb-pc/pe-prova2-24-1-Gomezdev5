from collections import Counter
from typing import List
def q1a(nums: List[int]) -> bool:
    for i in nums:  
        if i != nums:
            return True
        else:
            return False


def q1b(nums: List[int]) -> bool:
    lista1 = []
    for num in nums:
        if num in lista1:
            return True
        lista1.append(num)
    return False


def q2(s: str,t: str) -> bool:
    if s == t:
        return True
    else:
        return False

def q3() -> int:
    pass

    

        

def q4():
    def ler_valores(): 
        lista = []
        while True:
            
            nota = int(input("Digite sua nota: "))
            
            if nota == 0:
                break
            else:
                lista.append(nota)

        return lista


    def processa_lista(lista):
        par= [] 
        impar = []
        par_old = 0
        impar_old = 0
        for i in lista:
            if i % 2 == 0:
                par.append(i)
                par_old += 1
                if par_old >= 5:
                    par.pop(0)
            else:
                impar.append(i)
                impar_old += 1 
                if impar_old >= 5:
                    impar.pop(0)

        return par,impar

    


if __name__=="__main__":
    # teste sua questão manualmente aqui
    pass


import random
import copy
def alet_plants(plantas,plantas_Reload):
    parada_ALT =  True
    while parada_ALT:
        chaves_PLT = list(plantas.keys()) 
        tamanho_Classe = len(chaves_PLT)
        if tamanho_Classe > 0:
            classe = random.randint(0,tamanho_Classe - 1)

            tamanho_Tipo = len(plantas[chaves_PLT[classe]])
            if tamanho_Tipo > 0:
                tipo = random.randint(0,tamanho_Tipo - 1)
                parada_ALT = False
            else:
                del plantas[chaves_PLT[classe]]
        else:
            plantas = copy.deepcopy(plantas_Reload) 

    print("PLANTA ESCOLHIDA: %s"%plantas[chaves_PLT[classe]][tipo])
    del plantas[chaves_PLT[classe]][tipo]



def alet_zombies(zumbis,zumbis_Reload):
    parada_ALT =  True
    while parada_ALT:
        chaves_ZUM = list(zumbis.keys()) 
        tamanho_Classe = len(chaves_ZUM)
        if tamanho_Classe > 0:
            classe = random.randint(0,tamanho_Classe - 1)

            tamanho_Tipo = len(zumbis[chaves_ZUM[classe]])
            if tamanho_Tipo > 0:
                tipo = random.randint(0,tamanho_Tipo - 1)
                parada_ALT = False
            else:
                del zumbis[chaves_ZUM[classe]]
        else:
            zumbis = copy.deepcopy(zumbis_Reload) 

    print("ZUMBI ESCOLHIDO: %s"%zumbis[chaves_ZUM[classe]][tipo])
    del zumbis[chaves_ZUM[classe]][tipo]

import pickle
import aleatorizar
plantas_Reload = {"DisparaErvilha":["Ervilha de Fogo", 
                             'Ervilha de Gelo', 
                             "Ervilha Tóxica", 
                             "Comando Ervilha", 
                             "Agente Ervilha", 
                             "Lei Ervilha", 
                             "Dispara Ervilha", 
                             "Ervilha de Plasma"],
            
            "Girassol":["Flor Mística",
                        "Flor Elétrica", 
                        "Flor de Fogo", 
                        "Girassol das Trevas", 
                        "Petala de Metal", "Faraó do Sol", 
                        "Flor Alienígina"],
           
            "Carnívora":["Carnívora Turbo", 
                         "Carnívora Tóxica", 
                         "Carnívora de Fogo", 
                         "Carnívora Elétrica", 
                         "Carnívora Vampira", 
                         "Carnívora Blindada", 
                         "Carnívora Chestter", 
                         "Carnívora Come-Tudo"],
                         
            "Cacto":["Cacto Camuflado", 
                     "Cacto de Fogo", 
                     "Cacto de Gelo", 
                     "Cacto Elétrico",
                     "Cacto do Futuro", 
                     "Cacto Bandido", 
                     "Cacto Bandido", "Cacto Jade"],
            
            "Chefão": [  "Modo Dave Doidão"  ]}


zumbis_Reload = {"Saldado":["Saldado Comuflado", 
                     "Super Comando", 
                     "General Supremo", 
                     "Comandante Tanque", 
                     "Saldado Ártico", 
                     "Soldado Aéreo", 
                     "Centurião"],
                     
           "Engenheiro":["Soldador", 
                         "Pintor", 
                         "Mecânico", 
                         "Eletricista", 
                         "Encanador", 
                         "Paisagista", 
                         "Especialista em Saneamento"],
            
           "Cientista":["Químico", 
                        "Físico", 
                        "Dr.Tóxico", 
                        "Astranauto", 
                        "Biólogo Marinho", 
                        "Arqueólogo", 
                        "Dr.Chestter", 
                        "Paleontólogo"],
            
            "All-Star":["Astro do Baisebol", 
                        "Astro do Rugby", 
                        "Astro do Roquéi", 
                        "Astro do Criquete", 
                        "Astro do Goleiro", 
                        "Astro da Luta Livre", 
                        "Astro do Golfe"],
            
            "Zumbão":["Moodo Dr. Zumbão"]}


plantas = {"DisparaErvilha":["Ervilha de Fogo", 
                             'Ervilha de Gelo', 
                             "Ervilha Tóxica", 
                             "Comando Ervilha", 
                             "Agente Ervilha", 
                             "Lei Ervilha", 
                             "Dispara Ervilha", 
                             "Ervilha de Plasma"],
            
            "Girassol":["Flor Mística",
                        "Flor Elétrica", 
                        "Flor de Fogo", 
                        "Girassol das Trevas", 
                        "Petala de Metal", "Faraó do Sol", 
                        "Flor Alienígina"],
           
            "Carnívora":["Carnívora Turbo", 
                         "Carnívora Tóxica", 
                         "Carnívora de Fogo", 
                         "Carnívora Elétrica", 
                         "Carnívora Vampira", 
                         "Carnívora Blindada", 
                         "Carnívora Chestter", 
                         "Carnívora Come-Tudo"],
                         
            "Cacto":["Cacto Camuflado", 
                     "Cacto de Fogo", 
                     "Cacto de Gelo", 
                     "Cacto Elétrico",
                     "Cacto do Futuro", 
                     "Cacto Bandido", 
                     "Cacto Cítrico", 
                     "Cacto Jade"],
            
            "Chefão": [  "Modo Dave Doidão"  ]}

zumbis = {"Saldado":["Saldado Comuflado", 
                     "Super Comando", 
                     "General Supremo", 
                     "Comandante Tanque", 
                     "Saldado Ártico", 
                     "Soldado Aéreo", 
                     "Centurião"],
                     
           "Engenheiro":["Soldador", 
                         "Pintor", 
                         "Mecânico", 
                         "Eletricista", 
                         "Encanador", 
                         "Paisagista", 
                         "Especialista em Saneamento"],
            
           "Cientista":["Químico", 
                        "Físico", 
                        "Dr.Tóxico", 
                        "Astranauta", 
                        "Biólogo Marinho", 
                        "Arqueólogo", 
                        "Dr.Chestter", 
                        "Paleontólogo"],
            
            "All-Star":["Astro do Baisebol", 
                        "Astro do Rugby", 
                        "Astro do Roquéi", 
                        "Astro do Criquete", 
                        "Astro do Goleiro", 
                        "Astro da Luta Livre", 
                        "Astro do Golfe"],
            
            "Zumbão":["Moodo Dr. Zumbão"]}


try:
    arq_Plantas = open("Plantas.text", "rb")
    plantas = pickle.load(arq_Plantas)
    arq_Plantas.close()
except:
    arq_Plantas = open("Plantas.text", "wb")
    arq_Plantas.close()


try:
    arq_Zumbis = open("Zumbis.text", "rb")
    zumbis = pickle.load(arq_Zumbis)
    arq_Zumbis.close()
except:
    arq_Zumbis = open("Zumbis.text", "wb")
    arq_Zumbis.close()



parada = True
while parada:
    print()
    executar = (input("""
                   ############################################
        ################      PLANTAS VS ZUMBIS       ####################
        ###           ###################################              ###
        ##################################################################    
        #########             1 - PLANTAS                        #########
        #########             2 - ZUMBIS                         #########    
        #########             0 - SAIR """))
    print()

    

    if executar == "1":
        parada_PLT = True
        while parada_PLT:
            print()
            executar_PLT = (input("""
                    ############################################
            ################           PLANTAS            ####################
            ###           ###################################              ###
            ##################################################################    
            #########             1 - ALEATORIZAR                    #########
            #########             2 - ERVILHAS                       ######### 
            #########             3 - GIROSSÓIS                      #########
            #########             4 - CARNÍVORAS                     #########
            ########              5 - CACTOS                         #########
            #########             0 - SAIR """))
            print()

            if executar_PLT == "1":
               aleatorizar.alet_plants(plantas,plantas_Reload)
          
            elif executar_PLT == "0":
                parada_PLT = False
            else:
                print("VALOR INVÁLIDO, POR FAVOR INSIRIR APENAS OS VALORES DA TABELA")

    elif executar == "2":
        parada_ZUM = True
        while parada_ZUM:
            print()
            executar_ZUM= (input("""
                    ############################################
            ################            ZUMBIS            ####################
            ###           ###################################              ###
            ##################################################################    
            #########             1 - ALEATORIZAR                    #########
            #########             2 - SOLDADOS                       ######### 
            #########             3 - ENGENHEIROS                    #########
            #########             4 - CIENTISTAS                     #########
            ########              5 - ALL-STAR                       #########
            #########             0 - SAIR """))
            print()

            if executar_ZUM == "1":
               aleatorizar.alet_zombies(zumbis,zumbis_Reload)
          
            elif executar_ZUM == "0":
                parada_ZUM = False
            else:
                print("VALOR INVÁLIDO, POR FAVOR INSIRIR APENAS OS VALORES DA TABELA")
    else:
        parada = False

#################################################
arq_Plantas = open('Plantas.text', 'wb')        ###
pickle.dump(plantas, arq_Plantas)               ###
arq_Plantas.close()                             ###            
                                                #SALVANDO DADOS
arq_Zumbis = open('Zumbis.text', 'wb')          ###
pickle.dump(zumbis, arq_Zumbis)                 ### 
arq_Zumbis.close()                              ###
#################################################
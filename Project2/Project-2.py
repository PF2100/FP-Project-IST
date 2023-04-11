def cria_posicao(x,y):
    '''
    cria posicao: int x int -> posicao
    Recebe os valores correspondentes as coordenadas de uma posicao e devolve a 
    posicao correspondente. O construtor verifica a validade dos seus 
    argumentos.Se os argumentos nao forem validos e gerado um ValueError com a 
    mensagem "cria_posicao: argumentos invalidos".
    '''
    if not (isinstance(x,int) and isinstance(y,int)) or x<0 or y<0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (x,y)

def cria_copia_posicao(pos):
    '''
    cria_copia_posicao: posicao -> posicao
    Recebe uma posicao e devolve uma copia nova da posicao.
    '''
    return cria_posicao(pos[0],pos[1])


def obter_pos_x(pos):
    '''
    obter_pos_x : posicao -> int
    Devolve a componente x da posicao pos.
    '''
    return pos[0]

def obter_pos_y(pos):
    '''
    obter_pos_y: posicao -> int
    Devolve a componente y da posicao pos
    '''
    return pos[1]

def eh_posicao(pos):
    '''
    eh_posicao: universal -> booleano
    Devolve True caso o seu argumento seja um TAD posicao e False caso 
    contrario.
    '''
    return isinstance(pos,tuple) and len(pos) == 2 and isinstance(pos[0],int) \
        and isinstance(pos[1],int) and pos[0] >= 0 and pos[1] >= 0 

def posicoes_iguais(pos1,pos2):
    '''
    posicoes_iguais: posicao x posicao -> booleano
    Devolve True apenas se pos1 e pos2 sao posicoes e sao iguais.
    '''
    return  pos1==pos2

def posicao_para_str(pos):
    '''
    posicao_para_str : posicao -> str
    Devolve a cadeia de caracteres "(x, y)" que representa o seu argumento, 
    sendo os valores x e y as coordenadas de pos.
    '''
    return str((pos[0],pos[1]))

def obter_posicoes_adjacentes(pos):
    '''
    obter_posicoes_adjacentes: posicao -> tuplo
    Devolve um tuplo com as posicoes adjacentes a posicao pos, comecando pela 
    posicao acima de pos e seguindo no sentido horario.
    '''
    abcissa=obter_pos_x(pos)
    ordenada=obter_pos_y(pos)
    c=()
    if ordenada - 1 >= 0:
        c+= (cria_posicao(abcissa,ordenada-1),)
    c+=(cria_posicao(abcissa+1,ordenada),cria_posicao(abcissa,ordenada+1)) 
    
    if abcissa - 1 >= 0 :
        c+= (cria_posicao(abcissa-1,ordenada),)
    
    return c
    

def ordenar_posicoes(posicoes):
    '''
    ordenar_posicoes: tuplo -> tuplo
    Devolve um tuplo contendo as mesmas posicoes do tuplo fornecido como 
    argumento, ordenadas de acordo com a ordem de leitura do prado.
    '''
    posicoes = sorted(posicoes, key = lambda x : obter_pos_x(x))
    return tuple(sorted(posicoes, key = lambda x : obter_pos_y(x)))
    

'''

2 TADS

'''

def cria_animal(especie,freq_r,freq_a):
    '''
    cria_animal: str x int x int -> animal
    Recebe uma cadeia de caracteres especie nao vazia correspondente a especie
    do animal e dois valores inteiros correspondentes a frequencia de reproducao 
    freq_r (maior do que 0) e a frequencia de alimentacao freq_a (maior ou igual
    que 0) e devolve o animal. Animais com  freq_a maior que 0 sao considerados 
    predadores, caso contrario sao considerados presas. O construtor verifica a 
    validade dos seus argumentos, gerando um ValueError com a mensagem 
    "cria_animal: argumentos invalidos" se os seus argumentos forem invalidos.
    '''
    if not (isinstance(especie,str) and len(especie) and \
        isinstance(freq_r, int) and isinstance(freq_a,int) and freq_r>0 and 
        freq_a >=0):
        raise ValueError("cria_animal: argumentos invalidos")
    return [especie,freq_r,0,freq_a,0]

def cria_copia_animal(animal):
    '''
    cria_copia_animal: animal -> animal
    Recebe um animal "animal" (predador ou presa) e devolve uma nova copia do 
    animal
    '''
    return animal.copy()




def obter_especie(animal):
    '''
    obter_especie: animal -> str
    Devolve a cadeia de caracteres correspondente a especie do animal.
    '''
    return animal[0]

def obter_freq_reproducao(animal):
    '''
    obter_freq_reproducao: animal -> int
    Devolve a frequencia de reproducao do animal "animal".
    '''
    return animal[1]

def obter_freq_alimentacao(animal):
    '''
    obter_freq_alimentacao: animal -> int
    Devolve a frequencia de alimentacao do animal "animal" (as presas devolvem 
    sempre 0).
    '''
    return animal[3]

def obter_idade(animal):
    '''
    obter_idade: animal -> int
    Devolve a idade do animal "animal".
    '''
    return animal[2]


def obter_fome(animal):
    '''
    obter_fome: animal -> int
    Devolve a fome do animal "animal" (as presas devolvem sempre 0).
    '''
    return animal[4]


def aumenta_idade(animal):
    '''
    aumenta_idade: animal -> animal
    Modifica destrutivamente o animal "animal" incrementando o valor da sua 
    idade em uma unidade, e devolve o proprio animal.
    '''
    animal[2]= animal[2] +1 
    return animal

def reset_idade(animal):
    '''
    reset_idade: animal -> animal
    Modifica destrutivamente o animal "animal" definindo o valor da sua idade 
    igual a 0,e devolve o proprio animal.
    '''
    animal[2] = 0
    return animal

def aumenta_fome(animal):
    '''
    aumenta_fome: animal -> animal
    Modifica destrutivamente o animal predador "animal" incrementando o valor da 
    sua fome em uma unidade, e devolve o proprio animal. Esta operacao nao 
    modifica os animais presa.
    '''
    if eh_predador(animal):
        animal[4] = animal[4] + 1 
    return animal

def reset_fome(animal):
    '''
    reset_fome: animal -> animal
    Modifica destrutivamente o animal predador "animal" definindo o valor da sua 
    fome igual a 0, e devolve o proprio animal. Esta operacao nao modifica os 
    animais presa.
    '''
    if eh_predador(animal):
        animal[4]= 0
    return animal

def eh_animal(animal):
    '''
    eh_animal: universal -> booleano
    Devolve True caso o seu argumento seja um TAD animal e False caso contrario.
    '''
    return isinstance(animal,list) and len(animal)==5 and \
    isinstance(animal[0],str) and len(animal[0]) and\
    isinstance(animal[1],int) and animal[1] > 0 and isinstance(animal[3],int) \
    and animal[3]>=0 and isinstance(animal[2],int) and animal[2]>= 0 and \
    isinstance(animal[4],int) and animal[4]>=0 and \
    not (animal[3]==0 and animal[4]!=0)



def eh_predador(animal):
    '''
    eh_predador : universal -> booleano
    Devolve True caso o seu argumento seja um TAD animal do tipo predador e 
    False caso contrario.
    '''
    return eh_animal(animal) and animal[3] != 0

def eh_presa(animal):
    '''
    eh_presa: universal -> booleano
    Devolve True caso o seu argumento seja um TAD animal do tipo presa e False 
    caso contrario.
    '''
    return eh_animal(animal) and animal[3] == 0 


def animais_iguais(animal_1,animal_2):
    '''
    animais_iguais: animal x animal -> booleano 
    Devolve True apenas se animal_1 e animal_2 sao animais e sao iguais.
    '''
    return eh_animal(animal_1) and eh_animal(animal_2) and \
           animal_1[0] == animal_2[0] and animal_1[1] == animal_2[1] and \
           animal_1[2] == animal_2[2] and animal_1[3] == animal_2[3] and \
           animal_1[4] == animal_2[4]


def animal_para_char(animal):
    '''
    animal_para_char : animal -> str
    Devolve a cadeia de caracteres dum unico elemento correspondente ao primeiro
    caracter da especie do animal passada por argumento, em maiuscula para 
    animais predadores e em minuscula para animais presa.
    '''
    if eh_presa(animal):
        return animal[0][0].lower()
    return animal[0][0].upper()


def animal_para_str(animal):
    '''
    animal_para_str : animal -> str
    Devolve a cadeia de caracteres que representa o animal.
    '''
    if eh_predador(animal):
        return "{} [{}/{};{}/{}]".format(animal[0],animal[2],animal[1],\
                animal[4],animal[3])
    return "{} [{}/{}]".format(animal[0],animal[2],animal[1])
    

def eh_animal_fertil(animal):
    '''
    eh_animal_fertil: animal -> booleano
    Devolve True caso o animal "animal" tenha atingido a idade de reproducao e 
    False caso contrario.
    '''
    return eh_animal(animal) and obter_idade(animal) >=\
    obter_freq_reproducao(animal)

def eh_animal_faminto(animal):
    '''
    eh_animal_faminto: animal -> booleano
    Devolve True caso o animal "animal" tenha atingindo um valor de fome igual 
    ou superior a sua frequencia de alimentacao e False caso contrario. As 
    presas devolvem sempre False.
    '''
    return eh_predador(animal) and obter_fome(animal)>=\
           obter_freq_alimentacao(animal)

def reproduz_animal(animal_p):
    '''
    reproduz_animal: animal -> animal
    Recebe um animal animal_p devolvendo um novo animal da mesma especie com 
    idade e fome igual a 0, e modificando destrutivamente o animal passado como 
    argumento animal_p alterando a sua idade para 0.
    '''
    animal_f = reset_fome(reset_idade(cria_copia_animal(animal_p)))
    animal_p = reset_idade(animal_p)
    return animal_f 


'''

Prado

'''


def eh_limite_aux(limite,pos):
    '''
    eh_limite_aux: tuplo x posicao -> booleano
    Funcao auxiliar que recebe um tuplo com as abcissas e ordenadas da posicao 
    limite do prado , verificando se a posicao se encontra nos limites do prado.
    '''
    return obter_pos_x(pos) == obter_pos_x(limite) or obter_pos_y(pos) == \
        obter_pos_y(limite) or obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0 \


       
def pos_iguais_aux(tuplo,posicao):
    '''
    pos_iguais_aux: tuple x posicao -> booleano
    Funcao auxiliar que recebe um tuplo com posicoes e verifica se existe alguma
    posicao igual a posicao "posicao".
    '''
    for posicoes in tuplo:
        if posicoes_iguais(posicoes,posicao):
            return True
    return False
    
        


def eh_animais_validos(animais):
    '''
    eh_animais_validos: tuple -> booleano
    Funcao auxiliar que recebe um tuplo com animais devolvendo True se todos os 
    animais forem animais validos e False caso contrario.
    '''
    for animal in animais:
        if not eh_animal(animal):
            return False
    return True




def cria_prado(limit,montes,animais,pos_animais):
    '''
    cria_prado : posicao x tuplo x tuplo x tuplo -> prado
    Recebe uma posicao "limit" correspondente a posicao que ocupa a montanha do 
    canto inferior direito do prado, um tuplo "montes" de 0 ou mais posicoes 
    correspondentes aos rochedos que nao sao as montanhas dos limites exteriores
    do prado, um tuplo "animais" de 1 ou mais animais, e um tuplo "pos_animais"
    da mesma dimensao do tuplo animais com as posicoes correspondentes ocupadas 
    pelos animais e devolve o prado que representa internamente o mapa e os 
    animais presentes. O construtor verifica a validade dos seus argumentos, 
    gerando a mensagem "cria_prado: argumentos invalidos" caso os argumentos
    sejam invalidos
    
    '''
    if not (eh_posicao(limit) and isinstance(montes,tuple) and \
        isinstance(animais,tuple) and len(animais)  and \
        isinstance(pos_animais,tuple) and len(animais) == len(pos_animais)):
        
        raise ValueError("cria_prado: argumentos invalidos")
    
    if len(montes):
        '''
        verifica se as posicoes sao rochedos e nao estao fora do limite do prado
        '''
        for monte in montes:
            
            if not (eh_posicao(monte) and not (eh_limite_aux(limit,monte) \
                or obter_pos_x(monte) > obter_pos_x(limit) or \
                obter_pos_y(monte) > obter_pos_y(limit))):
                raise ValueError("cria_prado: argumentos invalidos")
            
    if not eh_animais_validos(animais):
        raise ValueError("cria_prado: argumentos invalidos")
    
    for posicao in pos_animais:
        '''
        verifica se a as posicoes sao validas e nao estao nos limites do prado \
        ou fora dele e que nao existe um animal num rochedo.
        '''
        
        if not (eh_posicao(posicao)  and not (pos_iguais_aux(montes,posicao) or\
            eh_limite_aux(limit,posicao) or obter_pos_x(posicao) > \
            obter_pos_x(limit) or obter_pos_y(posicao) > obter_pos_y(limit))):
            
            raise ValueError("cria_prado: argumentos invalidos")
        
    return [limit,montes,animais,pos_animais]


def cria_copia_prado(prado):
    '''
    cria_copia_prado: prado -> prado
    Recebe um prado e devolve uma nova copia do prado.

    '''
    if not eh_prado(prado):
        raise ValueError("cria_prado: argumentos invalidos")
    prado_2=prado.copy()
    animais=()
    for animal in prado_2[2]:
        animais += (cria_copia_animal(animal),)
    prado_3=prado[:2]+[animais]+prado_2[3:]
    return prado_3    
    


def obter_tamanho_x(prado):
    '''
    obter_tamanho_x: prado -> int
    Devolve o valor inteiro que corresponde a dimensao Nx do prado.
    '''
    return obter_pos_x(prado[0]) + 1

def obter_tamanho_y(prado):
    '''
    obter_tamanho_y: prado -> int
    Devolve o valor inteiro que corresponde a dimensao Ny do prado.
    '''
    return obter_pos_y(prado[0]) + 1 


def obter_numero_predadores(prado):
    '''
    obter_numero_predadores: prado -> int
    Devolve o numero de animais predadores no prado.
    '''
    predadores = 0
    for animal in prado[2]:
        if eh_predador(animal):
            predadores += 1 
    return predadores


def obter_numero_presas(prado):
    '''
    obter_numero_presas: prado -> int
    Devolve o numero de animais presa no prado.
    '''
    presas = 0
    for animal in prado[2]:
        if eh_presa(animal):
            presas += 1 
    return presas


def obter_posicao_animais(prado):
    '''
    obter_posicao_animais: prado -> tuplo posicoes
    Devolve um tuplo contendo as posicoes do prado ocupadas por animais, 
    ordenadas em ordem de leitura do prado
    '''
    return ordenar_posicoes(prado[3])


def obter_animal(prado,posicao):
    '''
    obter_animal: prado x posicao -> animal
    Devolve o animal do prado que se encontra na posicao "posicao"
    '''
    for pos in range(len(prado[3])) :
        if posicoes_iguais(prado[3][pos],posicao):
            return prado[2][pos]
        


def eliminar_animal(prado,posicao):
    '''
    eliminar_animal: prado x posicao -> prado
    Modifica destrutivamente o prado "prado" eliminando o animal da posicao 
    "posicao" deixando-a livre. Devolve o proprio prado.
    '''
    for pos in range(len(prado[3])):
        if posicoes_iguais(prado[3][pos],posicao) :
            prado[2] = prado[2][:pos] + prado[2][pos+1:]
            prado[3] = prado[3][:pos] + prado[3][pos+1:]
            break
    return prado
        
def mover_animal(prado,pos1,pos2):
    '''
    mover_animal: prado x posicao x posicao -> prado
    Modifica destrutivamente o prado "prado" movimentando o animal da posicao 
    pos1 para a nova posicao pos2, deixando livre a posicao onde se encontrava. 
    Devolve o proprio prado.
    '''
    if eh_posicao_livre(prado,pos2):
        prado[3] = tuple(map(lambda x : pos2 if posicoes_iguais(x,pos1)\
                else x, prado[3]))
    return prado



def inserir_animal(prado,animal,posicao):
    '''
    inserir_animal: prado x animal x posicao -> prado
    Modifica destrutivamente o prado "prado" acrescentando na posicao "posicao"
    do prado o animal "animal" passado com argumento. Devolve o proprio prado.
    '''
    if eh_posicao_livre(prado,posicao):
        prado[2] = prado[2] + (animal,)
        prado[3] = prado[3] + (posicao,)
    return prado




def eh_prado(prado):
    '''
    eh_prado: universal -> booleano
    Devolve True caso o seu argumento seja um TAD prado e False caso contrario
    '''
    if not (isinstance(prado,list) and len(prado)==4 and eh_posicao(prado[0]) \
        and isinstance(prado[1],tuple) and isinstance(prado[2],tuple) and \
        isinstance(prado[3],tuple) and len(prado[2]) == len(prado[3])):
        return False

    if len(prado[1]):
        '''
        verifica se os rochedos (caso existam) sao posicoes e nao se encontram
        no limite do prado ou fora dele
        '''
        for posicao in prado[1]:
            
            if not (eh_posicao(posicao) and not (eh_limite_aux(prado[0],\
                posicao) or obter_pos_x(posicao) > obter_pos_x(prado[0]) or \
                obter_pos_y(posicao) > obter_pos_y(prado[0]))):
                return False
    if len(prado[2]):
        '''
        verifica se sao animais e se nao estao em rochedos ou fora do prado
        '''
        for posicao in obter_posicao_animais(prado):
            if not (eh_posicao(posicao) and not (pos_iguais_aux(prado[1],\
                posicao) or eh_limite_aux(prado[0],posicao) or \
                obter_pos_x(posicao) > obter_pos_x(prado[0]) or \
                obter_pos_y(posicao) > obter_pos_y(prado[0]))):   
                return False
       
        return eh_animais_validos(prado[2])
    
    return True




def eh_posicao_animal(prado,posicao):
    '''
    eh_posicao_animal: prado x posicao -> booleano
    Devolve True apenas no caso da posicao "posicao" do prado estar ocupada por 
    um animal.
    '''
    return eh_prado(prado) and eh_posicao(posicao) and \
           pos_iguais_aux(obter_posicao_animais(prado),posicao)
        



def eh_posicao_obstaculo(prado,posicao):
    '''
    eh_posicao_obstaculo: prado x posicao -> booleano
    Devolve True apenas no caso da posicao "posicao" do prado corresponder a uma
    montanha ou rochedo.
    ''' 
    return eh_prado(prado) and eh_posicao(posicao) and \
       (pos_iguais_aux(prado[1],posicao) or eh_limite_aux(prado[0],posicao))
       



def eh_posicao_livre(prado,posicao):
    '''
    eh_posicao_livre: prado x posicao -> booleano
    Devolve True apenas no caso da posicao "posicao" do prado corresponder a 
    um espaco livre (sem animais, nem obstaculos).
    '''
    return eh_prado(prado) and eh_posicao(posicao) and not \
    (eh_posicao_obstaculo(prado,posicao) or eh_posicao_animal(prado,posicao)or\
     obter_pos_x(posicao)>obter_pos_x(prado[0]) or obter_pos_y(posicao)>\
     obter_pos_y(prado[0]))


def prados_iguais(prado_1,prado_2):
    '''
    prados_iguais: prado x prado -> booleano
    Devolve True apenas se prado_1 e prado_2 forem prados e forem iguais.
    '''
    return eh_prado(prado_1) and eh_prado(prado_2) and prado_1==prado_2
    



def prado_para_str(prado):
    '''
    prado_para_str : prado -> str
    Devolve uma cadeia de caracteres que representa o prado como mostrado nos
    exemplos.
    '''
    c=""
    for pos_y in range(obter_tamanho_y(prado)):
        if pos_y != 0 :
            c+="\n"
        for pos_x in range(obter_tamanho_x(prado)):
            if pos_y==0 or pos_y == obter_tamanho_y(prado)-1:
                if pos_x == 0  or pos_x == obter_tamanho_x(prado)-1:
                    c+= "+"
                else:
                    c+= "-"
            else:
                if pos_x == 0 or pos_x==obter_tamanho_x(prado)-1:
                    c+="|"
                else:
                    if eh_posicao_obstaculo(prado,cria_posicao(pos_x,pos_y)):
                        c+="@"
                    elif eh_posicao_animal(prado,cria_posicao(pos_x,pos_y)):
                        c+= animal_para_char(obter_animal(prado,cria_posicao(\
                            pos_x,pos_y)))
                    else:
                        c+="."
    return c

        
        
def obter_valor_numerico(prado,posicao):
    '''
    obter_valor_numerico: prado x posicao -> int
    Devolve o valor numerico da posicao posicao correspondente a ordem de 
    leitura no prado "prado".
    '''
    return obter_pos_x(posicao) + obter_pos_y(posicao)*obter_tamanho_x(prado)



def obter_movimento(prado,posicao):
    '''
    obter_movimento: prado x posicao -> posicao
    Devolve a posicao seguinte do animal na posicao posicao dentro do prado 
    "prado" de acordo com as regras de movimento dos animais no prado.
    '''
    if eh_posicao_animal(prado,posicao):
        
        l_pos=obter_posicoes_adjacentes(posicao)
        
        presas=[x for x in l_pos  if eh_posicao_animal(prado,x) and \
            eh_presa(obter_animal(prado,x))] 
        
        idx = obter_valor_numerico(prado,posicao)
        l_pos=[x for x in l_pos if eh_posicao_livre(prado,x)]
        
        if eh_presa(obter_animal(prado,posicao)):
            
            if len(l_pos):
                return l_pos[idx%len(l_pos)]
            
            return posicao
        
        elif len(presas):
            return presas[idx%len(presas)]
        
        elif len(l_pos):
            return l_pos[idx%len(l_pos)]
        
        return posicao
    
    

'''
geracao
'''



def geracao(prado):
    '''
     geracao: prado -> prado 
     E a funcao auxiliar que modifica o prado "prado" fornecido como argumento
     de acordo com a evolucao correspondente a uma geracao completa, e devolve o
     proprio prado. Isto e, seguindo a ordem de leitura do prado, cada animal 
     (vivo) realiza o seu turno de acao de acordo com as regras descritas
    '''
    kill=()
    for pos in obter_posicao_animais(prado) :
        mov = obter_movimento(prado,pos)
        animal = obter_animal(prado,pos)
        aumenta_idade(animal)
        aumenta_fome(animal)
        if pos not in kill:
            if not posicoes_iguais(pos,mov):
                '''
                acoes possveis das presas
                '''
                if eh_presa(animal) :
                    mover_animal(prado,pos,mov)
                    if eh_animal_fertil(obter_animal(prado,mov)):
                        inserir_animal(prado,reproduz_animal(\
                            obter_animal(prado,mov)),pos)
                else:
                    '''
                    acoes possiveis dos predadores
                    '''
                    if eh_presa(obter_animal(prado,mov)):
                        eliminar_animal(prado,mov)
                        kill+=(mov,)
                        mover_animal(prado,pos,mov)
                        reset_fome(obter_animal(prado,mov))
                        if eh_animal_fertil(obter_animal(prado,mov)):
                            inserir_animal(prado,reproduz_animal(\
                                obter_animal(prado,mov)),pos)
                    else:
                        mover_animal(prado,pos,mov)
                        if eh_animal_fertil(obter_animal(prado,mov)):
                            inserir_animal(prado,reproduz_animal(\
                                obter_animal(prado,mov)),pos)                        
                                       
            if eh_animal_faminto(obter_animal(prado,mov)):
                eliminar_animal(prado,mov)
                
                       
    return prado




'''

Simula Ecossistema


'''



def animal_aux(cad):
    '''
    animal_aux : list -> tuple
    Funcao auxiliar que recebe uma lista com todos as linhas correspondentes a 
    animais com as suas carateristicas e posicoes , devolvendo um tuplo com os 
    respetivos animais definidos e as suas posicoes.
    '''
    animais=tuple([eval(x) for x in cad])
    posicoes = tuple([cria_posicao(x[3][0],x[3][1]) for x in animais])
    animais = tuple([cria_animal(x[0],x[1],x[2]) for x in animais])
    return animais,posicoes
    
    
def prado_aux(ficheiro):
    '''
    prado_aux: str -> prado
    Funcao auxiliar que recebe uma cadeia de caracteres correspondente a um 
    ficheiro com as caracteristicas de um prado , transformando-as num prado.
    '''
    with open(ficheiro,"r") as f2:
        linhas=f2.readlines()
        dim = cria_posicao(eval(linhas[0])[0],eval(linhas[0])[1])
        obs = tuple([cria_posicao(x[0],x[1]) for x in eval(linhas[1])])
        a_pos = animal_aux(linhas[2:])
        return cria_prado(dim,obs,a_pos[0],a_pos[1])    





def simula_ecossistema(ficheiro,gen,modo) :
    '''
    simula_ecossistema: str x int x booleano -> tuplo
    E a funcao principal que permite simular o ecossistema de um prado. A funcao
    recebe uma cadeia de caracteres "ficheiro", um valor inteiro "gen" e um 
    valor booleano "modo" e devolve o tuplo de dois elementos correspondentes ao
    numero de predadores e presas no prado no fim da simulacao. A cadeia de 
    caracteres "ficheiro" passada por argumento corresponde a um ficheiro de 
    configuracao da simulacao. O valor inteiro gen corresponde ao numero de 
    geracoes a simular. O argumento booleano "modo" ativa o modo verboso (True) 
    ou o modo quiet (False). No modo quiet mostra-se pela saida standard o prado
    ,o numero de animais e o numero de geracao no inicio da simulacao e apos a 
    ultima geracao. No modo verboso, apos cada geracao, mostra-se tambem o prado
    , o numero de animais e o numero de geracao, apenas se o numero de animais 
    predadores ou presas se tiver alterado.
    '''
    previous=None
    prado = prado_aux(ficheiro)
    print("Predadores:",obter_numero_predadores(prado),"vs Presas:",\
          obter_numero_presas(prado),"(Gen. 0)\n"+prado_para_str(prado))
    
    
    if modo==True:
        for g in range(1,gen+1):
            prado2=cria_copia_prado(prado)
            prado=geracao(prado)
            
            resposta=obter_numero_predadores(prado),obter_numero_presas(prado)
            if obter_numero_presas(prado2)!= obter_numero_presas(prado) or \
               obter_numero_predadores(prado2)!= obter_numero_predadores(prado):
                
                
                print("Predadores:",obter_numero_predadores(prado),\
                      "vs Presas:",obter_numero_presas(prado),"(Gen. "+str(g)+\
                      ")\n"+prado_para_str(prado))
                
                
            elif obter_posicao_animais(prado) == obter_posicao_animais(prado2):
                
                return obter_numero_predadores(prado),obter_numero_presas(prado)
            
        print("Predadores:",obter_numero_predadores(prado),"vs Presas:",\
              obter_numero_presas(prado),"(Gen. "+str(g)+")\n"+\
              prado_para_str(prado)) 
        
        return resposta
    
    else:
        for i in range(1,gen+1):
            prado2=cria_copia_prado(prado)
            prado=geracao(prado)
            if obter_posicao_animais(prado) == obter_posicao_animais(prado2):
                
                
                print("Predadores:",obter_numero_predadores(prado),\
            "vs Presas:",obter_numero_presas(prado),"(Gen. "+str(gen)+")\n"+\
            prado_para_str(prado))
                
                return obter_numero_predadores(prado),obter_numero_presas(prado)
            
        print("Predadores:",obter_numero_predadores(prado),"vs Presas:",\
            obter_numero_presas(prado),\
            "(Gen. "+str(gen)+")\n"+prado_para_str(prado))
        
        return obter_numero_predadores(prado),obter_numero_presas(prado)
def corrigir_palavra (bug_p) :
    ''' 
    cad. carateres -> cad. carateres
    
    Esta funcao recebe uma cadeia de caracteres que representa uma palavra e \
    devolve a cadeia de caracteres que corresponde a aplicacao das reducoes \
    conforme descritas para obter a palavra corrigida
    
    '''    
    bug_l = list(bug_p)
    pos = 0    
    while pos + 1 < len(bug_l) :
        if abs(ord(bug_l[pos]) - ord(bug_l[pos + 1])) == 32:
            del bug_l[pos:pos+2] 
            pos = 0  
        else:
            pos += 1 
    return "".join(bug_l)


def eh_anagrama (palavra_1,palavra_2) :
    '''
    cad. carateres x cad. carateres -> booleano
    
    Recebe duas cadeias de caracteres e devolde True se uma for um anagrama \
    da outra(se sao constituidas pelas mesmas letras ignoradno maisculas ou \
    a ordem) 
    '''
    return sorted(palavra_1.lower()) == sorted(palavra_2.lower()) 



def verifica_input(bug_p):
    '''
    cad. caracteres -> booleano
    
    Funcao verifica_input e uma funcao auxiliar que verifica a veracidade dos \
    argumentos
   
    '''
    if type(bug_p) != str :
        raise ValueError("corrigir_doc: argumento invalido")
    for idx in range(len(bug_p)) :
        el= ord(bug_p[idx])
        if not ((65 <= el <= 90) or (97 <= el <=122) or el == 32): 
            raise ValueError("corrigir_doc: argumento invalido")
        if el == 32 and ord(bug_p[idx+1]) == 32 :
            raise ValueError("corrigir_doc: argumento invalido")
        
def corrigir_doc(bug_p):
    '''
    cad. carateres -> cad. carateres
    
    Recebe uma cadeia de caracteres que corresponde a um texto com erros da \
    documentacao BDB e devolve essa cadeia de caracteres filtrada com as \
    palavras corrigidas. Apos a correcao os anagramas sao avaliados , sendo \
    apagados apenas aqueles que sao palavras diferentes.\
    Esta funcao verifica a validade do argumento gerando ValueError("corrigir\
    _doc: argumento invalido") caso o argumento nao seja valido.
    
    '''
    idx_1 , idx_2 = 0 , 0 
    verifica_input(bug_p)
    bug_w, bug_l, str1 = bug_p.split(),[], " "
    if len(bug_p) == 0:
        raise ValueError("corrigir_doc: argumento invalido")
    for bug in bug_w:
        palavra = corrigir_palavra(bug)
        bug_l += [palavra]
        
    while idx_1 + idx_2 + 2 != 2*len(bug_l):
        idx_2 += 1
        
        
        if eh_anagrama(bug_l[idx_1],bug_l[idx_2]) and \
           bug_l[idx_1].lower() != bug_l[idx_2].lower():
            
            del bug_l[idx_2]
            idx_2 = idx_1
            
        elif idx_2 + 1 == len(bug_l) :
            idx_1 += 1 
            idx_2 = idx_1
            
    return str1.join(bug_l) 



'''
funcao 2
'''




direcoes=("C","B","E","D")
def obter_posicao(direc,dig):
    '''
    cad. carateres x inteiro -> inteiro
    
    A funcao recebe uma cadeia de caracteres ,com apenas um caracter que \
    representa a direcao de um movimento,e um inteiro,que representa a posicao\
    atual, devolvendo o inteiro que corresponde a nova posicao apos o movimento.
    
    '''
    
    if direc =="C" and dig not in (1,2,3):
        dig = dig - 3
    elif direc =="B" and  dig not in(7,8,9):
        dig = dig + 3
    elif direc =="E" and dig not in (1,4,7):
        dig = dig - 1 
    elif direc == "D" and dig not in(3,6,9):
        dig = dig + 1
    return dig

def obter_digito(cadeia,dig):
    '''
    cad. carateres x inteiro -> inteiro
    
    Recebe uma cadeia de caracteres com um ou mais movimentos e um inteiro\
    representado a posicao inicial.Assim devolve a posicao final apos os 1\
    movimentos.
    
    '''
    for mov in cadeia:
        dig = obter_posicao(mov,dig)
    return dig
            
            
def obter_pin(tuplo):
    '''
    tuplo -> tuplo
    
    Recebe um tuplo com 4 a 10 sequencias de movimento e devolve o tuplo de \
    inteiros que corresponde ao pin codificado de acordo com o tuplo de \
    movimentos.\
    
    Esta funcao verifica a validade dos argumentos devolvendo ValueError("obter\
    _pin: argumento invalido") caso o argumento nao seja valido.
    
    '''
    dig=5
    pin=()  
    if type(tuplo)!= tuple or len(tuplo)<4 or len(tuplo)>10:
        raise ValueError("obter_pin: argumento invalido")
    for cadeia in tuplo :
        if  not isinstance(cadeia,str) or cadeia == ""  :
            raise ValueError("obter_pin: argumento invalido")
        else:
            conjunto = "".join(tuplo)
            for letra in conjunto:
                if letra not in direcoes :
                    raise ValueError("obter_pin: argumento invalido")   
        dig=obter_digito(cadeia,dig)
        pin += (dig,)
    return pin



'''
funcao 3
'''



def validar_cifra_entrada(tuplo):
    if tuplo == "" or not isinstance(tuplo,str):
        return False
    for elem in range(len(tuplo)) :
        if not (122>=ord(tuplo[0])>=97 and 122>=ord(tuplo[-1])>= 97) \
        or (ord(tuplo[elem])==45 and ord(tuplo[elem+1])==45)  :
            return False
        elif not (122>=ord(tuplo[elem])>=97 or ord(tuplo[elem]) == 45):
            return False
    return True

def validar_cod_crtl(tuplo):
    if not isinstance(tuplo,str) :
        return False
    if len(tuplo[1:-1])==5 and tuplo[0] == "[" and tuplo[-1] == "]":
        for letra in tuplo[1:-1]:
            if not 122>=ord(letra)>=97:
                return False
        return True
    return False

def validar_numero(tuplo):
    if isinstance(tuplo,tuple)!=True or len(tuplo)<2:
        return False
    for num in tuplo:
        if type(num)!= int or num < 0 :
            return False        
    return True


def eh_entrada(tuplo):
    '''
    universal -> booleano
    
    Recebe um argumento de qualquer tipo e devolve True se o seu argumento \
    corresponder a uma entrada BDB ( tuplo com 3 campos, uma cifra , uma \
    sequencia de controlo e uma sequencia de seguranca).
    
    '''
    if not isinstance(tuplo,tuple) or len(tuplo)!=3 :
        return False
    return validar_cifra_entrada(tuplo[0]) and validar_cod_crtl(tuplo[1]) and \
           validar_numero(tuplo[2])





def validar_cifra(tuplo,BDB):
    '''
    cad. carateres x cad. carateres -> booleano
    
    Recebe uma cadeia de caracteres contenco uma cifra e uma outra cadeia de \
    caracteres contendo uma sequencia de controlo devolvendo True se a \
    sequencia de controlo e coerente com a cifra conforme descrita.
    
    '''
    if not validar_cifra_entrada(tuplo) and validar_cod_crtl(BDB):
        return False
    dic_novo,dic,pre_seq,pre_cifra={},{},[],[]
    if not (isinstance(tuplo,str) and isinstance(BDB,str)):
        return False
    for letras in tuplo:
        if letras in dic :
            dic[letras] += 1
        else:
            dic[letras]= 1
            
    for val,key in sorted(((val,key) for key,val in dic.items()), reverse=True):
        dic_novo[key]=val
    
        dic_novo[key]=val
    if "-" in dic_novo:
        del dic_novo["-"]
    
    for key in dic_novo :
        if key not in pre_cifra:
            for key2 in dic_novo :
                if dic_novo[key]==dic_novo[key2]  :
                    pre_seq += [key2]
            pre_cifra += sorted(pre_seq)
            
            if len(pre_cifra)>=5:
                break
            else:
                pre_seq= []
                
    return pre_cifra[0:5] == list(BDB[1:len(BDB)-1])

def filtrar_bdb(lista_bdb):
    '''
    lista -> lista
    
    A funcao recebe uma lista com uma ou mais entradas BDB e devolve uma lista\
    com apenas as entradas em que o checksum nao e coerente com a cifra \
    correspondente na mesma ordem da lista original.\
    Esta funcao verifica a validade do argumento  gerando ValueError("filtrar_b\
    db: argumento invalido") caso o argumento nao seja valido.
    
    '''
    

    not_bdb= []
    if lista_bdb == [] or not isinstance(lista_bdb,list):
        raise ValueError("filtrar_bdb: argumento invalido")
    for bdb in lista_bdb :
        if not eh_entrada(bdb):
            raise ValueError("filtrar_bdb: argumento invalido")
        if not validar_cifra(bdb[0],bdb[1]) :
            not_bdb += [bdb]
    return not_bdb
            
            
'''

funcao 4 

'''


def obter_num_seguranca(tuplo):
    '''
    tuplo -> inteiro
    
    A funcao recebe um tuplo tuplo de numeros inteiros positivos e devolve o \
    numero de seguranca conforme descrito ( menor diferenca positiva entre \
    qualquer par de numeros)
    
    '''
    previous = abs(tuplo[0]-tuplo[1])
    for elem in tuplo :
        for elem2 in tuplo :
            if previous > abs(elem-elem2) and elem != elem2  :
                previous = abs(elem - elem2)
    return previous

def decifrar_texto(texto,cod_seq):
    '''
    cad. carateres x inteiro -> cad. carateres
    
    Esta funcao recebe uma cadeia de carateres contendo uma cifra e um numero \
    de seguranca, e devolve o texto decifrado conforme descrito.
    
    
    '''
    cod_seq = cod_seq % 26 
    text= list(texto)

    for idx in range(len(text)):
        ordem = ord(text[idx])
        if text[idx] == "-" :
            text[idx] = " " 
        else:
            if idx % 2 == 0 :
                contador = -1 
            else : 
                contador = 1
            while contador != cod_seq:
                if text[idx] == "z":
                    text[idx] = "a"
                    contador += 1 
                else:
                    text[idx] = chr(ord(text[idx])+ 1)
                    contador += 1
    return "".join(text)

def decifrar_bdb(lista):
    '''
    lista -> lista
    
    Receb uma lista contendo uma ou mais entradas BDB e  devolve uma lista com \
    tamanho igual, contendo o texto das entradas decifradas na mesma ordem . \
    Esta funcao verifica a validade dos argumentos gerando ValueError("decifrar\
    _dbd: argumento invalido").
    
    '''
    desencriptacao = []
    if not isinstance(lista,list) or len(lista) == 0 :
        raise ValueError("decifrar_bdb: argumento invalido")
    
    for bdb in lista :
        if len(bdb)<3 or not eh_entrada(bdb):
            raise ValueError("decifrar_bdb: argumento invalido")
        cod_seq = obter_num_seguranca(bdb[2])
        desencriptacao += [decifrar_texto(bdb[0],cod_seq)]
    return desencriptacao
        
'''


funcao 5 


'''

def ver_name(utlzr):
    return {"name", "pass" , "rule"}  == utlzr.keys() and \
    isinstance(utlzr["name"],str) and len(utlzr["name"]) != 0 

def ver_pass(utlzr):
    return isinstance(utlzr["pass"],str) and len(utlzr["pass"]) != 0 

def ver_rule(utlzr):
    if utlzr["rule"].keys() != {"vals","char"}:
        return False
    elif not isinstance(utlzr["rule"]["vals"],tuple) or len(utlzr["rule"]\
    ["vals"])!= 2 :
        return False
    elif utlzr["rule"]["vals"][0] > utlzr["rule"]["vals"][1] or utlzr["rule"]\
         ["vals"][0] < 0  or utlzr["rule"]["vals"][1] < 0 :
        return False
    return  isinstance(utlzr["rule"]["char"],str) and \
            len(utlzr["rule"]["char"]) == 1
    
    

def eh_utilizador(utlzr):
    '''
    universal -> booleano 
    
    A funcao recebe um argumento de qualquer tipo e devolve True se o seu \
    argumento correspondente a um dicionario contendo a informacao  de um \
    utilizador BDB(nome , senha e regra individual).
    
    '''
    return isinstance(utlzr,dict) and ver_name(utlzr) and ver_pass(utlzr) and\
           ver_rule(utlzr)



def eh_senha_valida(passe,regra):
    '''
    cad. carateres x dicionario -> booleano
    
    A funcao recebe uma cadeia de carateres que corresponde a uma senha e um \
    dicionario que tem a regra individual de criacao da senha e devolve True \
    se a senha cumpre todas as regras individuais e gerais conforme descritas.
    
    '''
    consec,prev,occor,vogais = 0 , None, 0,0
    a={"pass":passe,"rule":regra}
    if not (ver_rule(a) and ver_pass(a)):
        return False
    for letra in passe :
        if letra == prev :
            consec = 1            
        if letra in ("a","e","i","o","u"):
            vogais += 1
        if a["rule"]["char"] == letra:
            occor += 1 
        prev = letra
    return consec != 0 and vogais >=3 and \
    a["rule"]["vals"][0]<=occor<=a["rule"]["vals"][1] 


def filtrar_senhas(BDBS):
    '''
    lista -> lista
    
    A funcao recebe uma lista com um ou mais dicionarios correspondentes as \
    entradas BDB e devolve a lista ordenada alfabeticamente com os nomes \
    dos utiliadores com senhas erradas.\
    A funcao verifica a validade dos argumentos  gerando ValueError("filtrar_bd\
    b: argumento invalido ") se o seu argumento nao for valido .
    '''
    
    lista=[]
    if not isinstance(BDBS,list) or BDBS==[]:
        raise ValueError("filtrar_senhas: argumento invalido")
    for BDB in BDBS :
        if not eh_utilizador(BDB):
            raise ValueError("filtrar_senhas: argumento invalido")
        else:
            if not eh_senha_valida(BDB["pass"],BDB["rule"]):
                lista = [BDB["name"]] + lista
    return sorted(lista)
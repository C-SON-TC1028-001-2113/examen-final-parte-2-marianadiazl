def crearmatriz():
    lista=[]
    fila=int(input())
    columna=int(input())
    if fila>0 and columna>0:
        for i in range(fila):
            lista.append([])
            for j in range(columna):
                n=int(input())
                lista[i].append(n)
    else:
        print('Error')
    return lista

def main():
    matriz=crearmatriz()
    lista_colu=[]
    if len(matriz)>0:
        for i in range(len(matriz[0])):
            count=0
            for j in range(len(matriz)):
                count += matriz[j][i]
            lista_colu.append(count)
        print(lista_colu)



if __name__=='__main__':
    main()

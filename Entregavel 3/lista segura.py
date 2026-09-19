import copy

def adicionar_item_seguro(lista_original, novo_item):
    """
    Adiciona um item e retorna uma nova lista, 
    preservando a lista original intacta.
    """
    # Cria uma cópia rasa (shallow copy) da lista original
    nova_lista = lista_original.copy()
    
    # Adiciona o novo item apenas na cópia
    nova_lista.append(novo_item)
    
    return nova_lista


# Exemplo de uso

lista_base = ["Maçã", "Banana", "Laranja"]

# Chamada da função para gerar uma nova lista com o item adicional
lista_atualizada = adicionar_item_seguro(lista_base, "Uva")

print("Lista Original:", lista_base)
print("Nova Lista:    ", lista_atualizada)


# versão Portugol:

#programa
#{
#	// Função que recebe um vetor, cria uma cópia defensiva e adiciona um novo item
#	funcao adicionarItemSeguro(cadeia vetorOriginal[], inteiro tamanhoOriginal, cadeia novoItem, cadeia vetorResultado[])
#	{
#		// Step 1: Copia defensiva elemento por elemento para o novo vetor
#		para (inteiro i = 0; i < tamanhoOriginal; i++) {
#			vetorResultado[i] = vetorOriginal[i]
#		}
#
#		// Step 2: Adiciona o novo item na última posição do vetor resultado
#		vetorResultado[tamanhoOriginal] = novoItem
#	}
#
#	funcao inicio()
#	{
#		// Vetor original com 3 elementos
#		cadeia listaBase[3] = {"Maçã", "Banana", "Laranja"}
#		
#		// Vetor de destino com tamanho 4 para receber o elemento extra sem alterar o original
#		cadeia listaNova[4]
#
#		// Executa a adição com cópia defensiva
#		adicionarItemSeguro(listaBase, 3, "Uva", listaNova)
#
#		// Exibe a lista original (intacta)
#		escreva("Vetor Original: ")
#		para (inteiro i = 0; i < 3; i++) {
#			escreva("[", listaBase[i], "] ")
#		}
#
#		// Exibe a nova lista (com o novo item)
#		escreva("\nNovo Vetor:     ")
#		para (inteiro i = 0; i < 4; i++) {
#			escreva("[", listaNova[i], "] ")
#		}
#		escreva("\n")
#	}
#}
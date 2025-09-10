#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso da Caixa de Texto
Example usage of Text Box
"""

from caixa_texto import CaixaTexto

def exemplo_basico():
    """Demonstra o uso básico da Caixa de Texto"""
    print("=== Exemplo de Uso da Caixa de Texto ===\n")
    
    # Cria uma instância da Caixa de Texto
    caixa = CaixaTexto()
    
    # Exemplo 1: Salvar um texto simples
    texto_exemplo = """Este é um exemplo de texto salvo na Caixa.
    
Data: 2025-01-10
Conteúdo: Texto de exemplo para demonstrar o funcionamento.

A Caixa de Texto permite:
- Salvar textos em arquivos
- Fazer commits automáticos
- Organizar o conteúdo em um diretório específico
"""
    
    print("1. Salvando texto de exemplo...")
    sucesso = caixa.salvar_texto("exemplo", texto_exemplo, fazer_commit=True)
    
    if sucesso:
        print("✓ Texto salvo com sucesso!\n")
    
    # Exemplo 2: Ler o texto salvo
    print("2. Lendo o texto salvo...")
    conteudo = caixa.ler_texto("exemplo")
    if conteudo:
        print("Conteúdo lido:")
        print("-" * 40)
        print(conteudo)
        print("-" * 40 + "\n")
    
    # Exemplo 3: Listar todos os textos
    print("3. Listando todos os textos salvos...")
    textos = caixa.listar_textos()
    if textos:
        print("Textos disponíveis:")
        for texto in textos:
            print(f"  • {texto}")
    else:
        print("Nenhum texto encontrado.")
    
    print("\n=== Fim do Exemplo ===")
    print("\nPara usar o modo interativo, execute: python caixa_texto.py")

if __name__ == "__main__":
    exemplo_basico()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste completo da funcionalidade da Caixa de Texto
Complete test of Text Box functionality
"""

from caixa_texto import CaixaTexto
import os
import shutil

def test_completo():
    """Testa todas as funcionalidades da Caixa de Texto"""
    print("=== TESTE COMPLETO DA CAIXA DE TEXTO ===\n")
    
    # Limpa diretório de teste se existir
    if os.path.exists("textos_teste"):
        shutil.rmtree("textos_teste")
    
    # Cria instância de teste
    caixa = CaixaTexto("textos_teste")
    
    sucesso_total = True
    
    # Teste 1: Salvar texto
    print("1. Testando salvar texto...")
    texto1 = "Este é um texto de teste.\nLinha 2 do texto.\nFim do texto."
    sucesso = caixa.salvar_texto("teste1", texto1, fazer_commit=False)
    if sucesso:
        print("   ✓ Texto salvo com sucesso")
    else:
        print("   ✗ Falha ao salvar texto")
        sucesso_total = False
    
    # Teste 2: Ler texto
    print("\n2. Testando ler texto...")
    conteudo = caixa.ler_texto("teste1")
    if conteudo == texto1:
        print("   ✓ Texto lido corretamente")
    else:
        print("   ✗ Falha ao ler texto ou conteúdo incorreto")
        sucesso_total = False
    
    # Teste 3: Salvar outro texto
    print("\n3. Testando salvar segundo texto...")
    texto2 = "Segundo arquivo de teste com conteúdo diferente."
    sucesso = caixa.salvar_texto("teste2", texto2, fazer_commit=False)
    if sucesso:
        print("   ✓ Segundo texto salvo com sucesso")
    else:
        print("   ✗ Falha ao salvar segundo texto")
        sucesso_total = False
    
    # Teste 4: Listar textos
    print("\n4. Testando listar textos...")
    textos = caixa.listar_textos()
    expected_files = ["teste1.txt", "teste2.txt"]
    if all(arquivo in textos for arquivo in expected_files):
        print("   ✓ Listagem de textos funcionando")
        print(f"   Arquivos encontrados: {textos}")
    else:
        print("   ✗ Falha na listagem de textos")
        print(f"   Esperado: {expected_files}")
        print(f"   Encontrado: {textos}")
        sucesso_total = False
    
    # Teste 5: Fazer commit
    print("\n5. Testando fazer commit...")
    sucesso = caixa.fazer_commit("Teste de commit automático")
    if sucesso:
        print("   ✓ Commit realizado com sucesso")
    else:
        print("   ✗ Falha ao fazer commit")
        sucesso_total = False
    
    # Teste 6: Ler arquivo inexistente
    print("\n6. Testando ler arquivo inexistente...")
    conteudo = caixa.ler_texto("inexistente")
    if conteudo is None:
        print("   ✓ Tratamento de arquivo inexistente funcionando")
    else:
        print("   ✗ Falha no tratamento de arquivo inexistente")
        sucesso_total = False
    
    # Teste 7: Salvar com commit automático
    print("\n7. Testando salvar com commit automático...")
    texto3 = "Texto com commit automático."
    sucesso = caixa.salvar_texto("teste3", texto3, fazer_commit=True)
    if sucesso:
        print("   ✓ Salvar com commit automático funcionando")
    else:
        print("   ✗ Falha no salvar com commit automático")
        sucesso_total = False
    
    # Resultado final
    print("\n" + "="*50)
    if sucesso_total:
        print("🎉 TODOS OS TESTES PASSARAM! Sistema funcionando corretamente.")
    else:
        print("❌ ALGUNS TESTES FALHARAM! Verifique os erros acima.")
    print("="*50)
    
    # Limpeza opcional (comentar para manter arquivos de teste)
    # if os.path.exists("textos_teste"):
    #     shutil.rmtree("textos_teste")
    
    return sucesso_total

if __name__ == "__main__":
    test_completo()
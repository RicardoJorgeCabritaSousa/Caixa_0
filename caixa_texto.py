#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caixa de Texto - Sistema para guardar texto e fazer commits
Text Box - System to save text and make commits
"""

import os
import sys
import datetime
import subprocess
from pathlib import Path


class CaixaTexto:
    """Classe principal para gerenciamento de texto e commits"""
    
    def __init__(self, diretorio_textos="textos"):
        """
        Inicializa a Caixa de Texto
        
        Args:
            diretorio_textos (str): Diretório onde os textos serão salvos
        """
        self.diretorio_textos = Path(diretorio_textos)
        self.diretorio_textos.mkdir(exist_ok=True)
        self.repo_root = Path.cwd()
    
    def salvar_texto(self, nome_arquivo, conteudo, fazer_commit=True):
        """
        Salva texto em um arquivo e opcionalmente faz commit
        
        Args:
            nome_arquivo (str): Nome do arquivo (sem extensão)
            conteudo (str): Conteúdo do texto a ser salvo
            fazer_commit (bool): Se deve fazer commit após salvar
        
        Returns:
            bool: True se operação foi bem-sucedida
        """
        try:
            # Adiciona extensão .txt se não tiver
            if not nome_arquivo.endswith('.txt'):
                nome_arquivo += '.txt'
            
            caminho_arquivo = self.diretorio_textos / nome_arquivo
            
            # Salva o arquivo
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            
            print(f"✓ Texto salvo em: {caminho_arquivo}")
            
            if fazer_commit:
                return self.fazer_commit(f"Adicionado/atualizado: {nome_arquivo}")
            
            return True
            
        except Exception as e:
            print(f"✗ Erro ao salvar texto: {e}")
            return False
    
    def ler_texto(self, nome_arquivo):
        """
        Lê o conteúdo de um arquivo de texto
        
        Args:
            nome_arquivo (str): Nome do arquivo
        
        Returns:
            str: Conteúdo do arquivo ou None se erro
        """
        try:
            if not nome_arquivo.endswith('.txt'):
                nome_arquivo += '.txt'
            
            caminho_arquivo = self.diretorio_textos / nome_arquivo
            
            if not caminho_arquivo.exists():
                print(f"✗ Arquivo não encontrado: {caminho_arquivo}")
                return None
            
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                return f.read()
                
        except Exception as e:
            print(f"✗ Erro ao ler texto: {e}")
            return None
    
    def listar_textos(self):
        """
        Lista todos os arquivos de texto salvos
        
        Returns:
            list: Lista de nomes de arquivos
        """
        try:
            arquivos = list(self.diretorio_textos.glob('*.txt'))
            return [arquivo.name for arquivo in arquivos]
        except Exception as e:
            print(f"✗ Erro ao listar textos: {e}")
            return []
    
    def fazer_commit(self, mensagem=None):
        """
        Faz commit das mudanças no repositório
        
        Args:
            mensagem (str): Mensagem do commit
        
        Returns:
            bool: True se commit foi bem-sucedido
        """
        try:
            if mensagem is None:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                mensagem = f"Texto salvo em {timestamp}"
            
            # Adiciona todos os arquivos
            subprocess.run(['git', 'add', '.'], 
                         cwd=self.repo_root, check=True, capture_output=True)
            
            # Faz o commit
            resultado = subprocess.run(['git', 'commit', '-m', mensagem], 
                                     cwd=self.repo_root, check=True, capture_output=True, text=True)
            
            print(f"✓ Commit realizado: {mensagem}")
            return True
            
        except subprocess.CalledProcessError as e:
            if 'nothing to commit' in e.stdout:
                print("ℹ Nada para fazer commit (sem mudanças)")
                return True
            else:
                print(f"✗ Erro ao fazer commit: {e}")
                return False
        except Exception as e:
            print(f"✗ Erro ao fazer commit: {e}")
            return False
    
    def menu_interativo(self):
        """Menu interativo para usar a Caixa de Texto"""
        print("\n" + "="*50)
        print("   CAIXA DE TEXTO - Sistema de Gestão de Texto")
        print("="*50)
        
        while True:
            print("\nOpções disponíveis:")
            print("1. Salvar novo texto")
            print("2. Ler texto existente") 
            print("3. Listar todos os textos")
            print("4. Fazer commit manual")
            print("5. Sair")
            
            try:
                opcao = input("\nEscolha uma opção (1-5): ").strip()
                
                if opcao == '1':
                    self._opcao_salvar_texto()
                elif opcao == '2':
                    self._opcao_ler_texto()
                elif opcao == '3':
                    self._opcao_listar_textos()
                elif opcao == '4':
                    self._opcao_commit_manual()
                elif opcao == '5':
                    print("Saindo da Caixa de Texto. Até breve!")
                    break
                else:
                    print("✗ Opção inválida. Tente novamente.")
                    
            except KeyboardInterrupt:
                print("\n\nSaindo da Caixa de Texto. Até breve!")
                break
            except EOFError:
                print("\n\nSaindo da Caixa de Texto. Até breve!")
                break
            except Exception as e:
                print(f"✗ Erro: {e}")
                # Se for um erro de entrada não interativa, sair
                if "EOF" in str(e):
                    break
    
    def _opcao_salvar_texto(self):
        """Opção do menu para salvar texto"""
        nome = input("Nome do arquivo (sem extensão): ").strip()
        if not nome:
            print("✗ Nome do arquivo não pode estar vazio")
            return
        
        print("Digite o texto (pressione Ctrl+D ou Ctrl+Z para finalizar):")
        print("-" * 40)
        
        linhas = []
        try:
            while True:
                linha = input()
                linhas.append(linha)
        except EOFError:
            pass
        
        conteudo = '\n'.join(linhas)
        
        if conteudo.strip():
            commit = input("\nFazer commit automaticamente? (s/N): ").strip().lower() == 's'
            self.salvar_texto(nome, conteudo, commit)
        else:
            print("✗ Conteúdo vazio, não foi salvo")
    
    def _opcao_ler_texto(self):
        """Opção do menu para ler texto"""
        arquivos = self.listar_textos()
        if not arquivos:
            print("✗ Nenhum texto encontrado")
            return
        
        print("Textos disponíveis:")
        for i, arquivo in enumerate(arquivos, 1):
            print(f"{i}. {arquivo}")
        
        try:
            escolha = int(input("Escolha o número do arquivo: ")) - 1
            if 0 <= escolha < len(arquivos):
                conteudo = self.ler_texto(arquivos[escolha])
                if conteudo is not None:
                    print(f"\n--- Conteúdo de {arquivos[escolha]} ---")
                    print(conteudo)
                    print("-" * 40)
            else:
                print("✗ Número inválido")
        except ValueError:
            print("✗ Por favor, digite um número válido")
    
    def _opcao_listar_textos(self):
        """Opção do menu para listar textos"""
        arquivos = self.listar_textos()
        if arquivos:
            print(f"\nTextos salvos ({len(arquivos)}):")
            for arquivo in arquivos:
                print(f"  • {arquivo}")
        else:
            print("✗ Nenhum texto encontrado")
    
    def _opcao_commit_manual(self):
        """Opção do menu para commit manual"""
        mensagem = input("Mensagem do commit (deixe vazio para automática): ").strip()
        self.fazer_commit(mensagem if mensagem else None)


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Caixa de Texto - Sistema para salvar texto e fazer commits",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python caixa_texto.py                     # Modo interativo
  python caixa_texto.py --list              # Listar textos salvos
  python caixa_texto.py --read nome         # Ler texto específico
  python caixa_texto.py --save nome "texto" # Salvar texto via linha de comando
  python caixa_texto.py --commit "mensagem" # Fazer commit manual
        """
    )
    
    parser.add_argument('--list', '-l', action='store_true',
                       help='Listar todos os textos salvos')
    parser.add_argument('--read', '-r', metavar='NOME',
                       help='Ler um texto específico')
    parser.add_argument('--save', '-s', nargs=2, metavar=('NOME', 'TEXTO'),
                       help='Salvar texto via linha de comando')
    parser.add_argument('--commit', '-c', metavar='MENSAGEM',
                       help='Fazer commit com mensagem específica')
    parser.add_argument('--no-commit', action='store_true',
                       help='Não fazer commit automático ao salvar')
    
    args = parser.parse_args()
    
    caixa = CaixaTexto()
    
    # Verifica se alguma opção de linha de comando foi usada
    if args.list:
        textos = caixa.listar_textos()
        if textos:
            print(f"Textos salvos ({len(textos)}):")
            for texto in textos:
                print(f"  • {texto}")
        else:
            print("Nenhum texto encontrado.")
        return
    
    if args.read:
        conteudo = caixa.ler_texto(args.read)
        if conteudo is not None:
            print(f"--- Conteúdo de {args.read} ---")
            print(conteudo)
            print("-" * 40)
        return
    
    if args.save:
        nome, texto = args.save
        fazer_commit = not args.no_commit
        caixa.salvar_texto(nome, texto, fazer_commit)
        return
    
    if args.commit:
        caixa.fazer_commit(args.commit)
        return
    
    # Se nenhuma opção foi especificada, usar modo interativo
    caixa.menu_interativo()


if __name__ == "__main__":
    main()
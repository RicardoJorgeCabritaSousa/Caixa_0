# Caixa_0 - Sistema de Gestão de Texto

Material de Experimentação - Sistema para salvar texto e fazer commits automaticamente.

## Funcionalidades

- 📝 **Salvar Texto**: Criar e editar arquivos de texto
- 💾 **Commits Automáticos**: Fazer commits git automaticamente após salvar
- 📂 **Organização**: Textos organizados em diretório dedicado
- 🔍 **Listagem**: Visualizar todos os textos salvos
- 📖 **Leitura**: Ler textos salvos anteriormente

## Como Usar

### Modo Interativo
```bash
python caixa_texto.py
```

### Exemplo Programático
```bash
python exemplo_uso.py
```

### Uso no Código
```python
from caixa_texto import CaixaTexto

# Criar instância
caixa = CaixaTexto()

# Salvar texto com commit automático
caixa.salvar_texto("meu_texto", "Conteúdo do texto", fazer_commit=True)

# Ler texto
conteudo = caixa.ler_texto("meu_texto")

# Listar textos
textos = caixa.listar_textos()
```

## Estrutura do Projeto

```
Caixa_0/
├── caixa_texto.py      # Módulo principal
├── exemplo_uso.py      # Exemplo de uso
├── textos/            # Diretório dos textos salvos (criado automaticamente)
└── README.md          # Documentação
```

## Requisitos

- Python 3.6+
- Git configurado no sistema

## Funcionalidades do Menu Interativo

1. **Salvar novo texto** - Criar/editar arquivo de texto
2. **Ler texto existente** - Visualizar conteúdo salvo
3. **Listar todos os textos** - Ver todos os arquivos salvos
4. **Fazer commit manual** - Commit com mensagem personalizada
5. **Sair** - Encerrar o programa

---

*Para fazer commits e guardar texto de forma simples e organizada.*

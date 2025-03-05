# CrewAI Code Interpreter

Este repositório contém um interpretador de código baseado no CrewAI, permitindo execução interativa de comandos de IA.

## Requisitos

Antes de começar, certifique-se de ter o **Python 3.10+** instalado.
Utilizamos o `uv` para gerenciamento de dependências. Se ainda não tiver o `uv` instalado, você pode instalá-lo com:

```sh
pip install uv
```

## Instalação

1. Iniciar:

   ```sh
   uv init
   ```

2. Sincronize o ambiente:

   ```sh
   uv sync
   ```

3. Instale as dependências necessárias:
   ```sh
   uv add crewai
   uv add python-dotenv
   uv add crewai_tools
   #uv add langchain-community
   uv add open-interpreter
   uv add gradio
   uv add psycopg2
   uv add streamlit
   #uv add langchain
   ```

## Execução

Execute os seguintes comandos para rodar diferentes componentes do projeto:

- Para rodar o interpretador principal:

  ```sh
  uv run python main.py
  ```

- Para iniciar a interface do usuário (UI):

  ```sh
  uv run python main_ui.py
  ```

- Para iniciar a UI integrada ao Ollama:
  ```sh
  uv run python main_ui_ollama.py
  ```

## Estrutura do Projeto

```
/
├── main.py              # Script principal do interpretador
├── main_ui.py           # Interface UI principal
├── main_ui_ollama.py    # Interface UI integrada ao Ollama
├── .env                 # Variáveis de ambiente (exemplo: chaves de API)
├── requirements.txt     # Dependências (caso prefira usar pip)
├── README.md            # Documentação do projeto
```

## Contribuição

Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com melhorias.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

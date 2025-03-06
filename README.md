# CrewAI Code Interpreter

Este repositório contém os códigos que foram referenciados no blog.

## Requisitos

Antes de começar, certifique-se de ter o **Python 3.12+** instalado.
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
   uv add open-interpreter
   uv add gradio
   uv add psycopg2
   uv add streamlit
   ```

## Execução

Execute os seguintes comandos para rodar diferentes componentes do projeto:

- Para rodar o Redigir Blog:

  ```sh
  uv run python ./blogs/main.py
  ```

- Para rodar o SQL Query AI:

  ```sh
  uv run python ./query/main.py
  ```

- Para rodar Interpretador:

  ```sh
  uv run python ./interpretador/main.py
  ```

## Estrutura do Projeto

```
/
├── blogs                # Códigos do Agentes para redigir blogs
├── query                # Cógigos do Agente que utiliza linguagem natural para realizar consultas em uma base de dados
├── interpretador        # Códigos do Agente interpretador de código
├── llm_model.py         # Classe que encapsula os modelos LLM e SLM
├── llm_type.py          # Enum
```

## Contribuição

Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com melhorias.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

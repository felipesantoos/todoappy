# ToDoApPy
> Uma app de lista de afazeres feito em Python e SQLite.

Este projeto desenvolve um CRUD completo com a lingugem de programação Python e o SGDB SQLite.

# Como rodar este projeto
```shell
git clone https://github.com/felipesantoos/todoappy.git # Clona o repositório.
cd todoappy/ # Entra na pasta do projeto.
code . # Abre o projeto no VS Code.
python3 app.py # Executa o projeto.
```

# SQLite
- Python já tem suporte nativo ao SQLite.
- Só não é indicado para aplicações que recebem muitas conexões simultâneas.
- É utilizado nos celulares Android e iPhone.

# Implementação
- `connect(file_path)` retorna uma conexão com o banco de dados SQLite.
- `conn.execute(sql, tuple)` executa o comando SQL informado no 1º parâmetro misturado com os argumentos do 2º (opcional).
- `cursor` é um objeto retornado pelo `conn.execute(sql, tuple)` que nos permite iterar e ler os resultados da consulta.
- `conn.commit()` salva definitivamente as alterações realizadas no banco de dados.

# Tarefas
- [x] Criar conexão com o banco de dados.
- [x] Solicitar o dados que serão cadastrados ao usuário.
- [x] Inserir registros no banco de dados.
- [x] Visualizar registros do banco de dados.
- [x] Alterar registros do banco de dados.
- [x] Remover registros do banco de dados.

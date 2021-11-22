# ToDoApPy
> Uma app de lista de afazeres feito em Python e SQLite.

Este projeto desenvolve um CRUD completo com a lingugem de programação Python e o SGDB SQLite.

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
- [ ] Criar conexão com o banco de dados.
- [ ] Solicitar o dados que serão cadastrados ao usuário.
- [ ] Inserir registros no banco de dados.
- [ ] Visualizar registros do banco de dados.
- [ ] Alterar registros do banco de dados.

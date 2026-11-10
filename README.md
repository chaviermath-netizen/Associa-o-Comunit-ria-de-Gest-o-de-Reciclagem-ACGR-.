refactor(architecture): estruturação modular do backend em camadas com Flask e SQLAlchemy

- Modularização: Separação clara entre os modelos de dados ORM (User e Chamado), a lógica de controlo de rotas e as views HTML, garantindo a manutenibilidade do código.
- Persistência e Segurança: Utilização de SQLite com SQLAlchemy para isolar as transações e aplicação de hashes criptográficos (Werkzeug) nas credenciais de acesso.
- Conformidade: Alinhamento das rotas protegidas por decorators de sessão (@login_required) e estruturação das interfaces sob diretrizes de acessibilidade WCAG 2.1 AA.

- security(quality): validação de segurança, proteção de rotas e mitigação de vulnerabilidades

- Segurança de Credenciais: Implementação de hash criptográfico para as palavras-passe utilizando o Werkzeug, garantindo que nenhuma credencial seja armazenada em texto plano.
- Controlo de Acesso: Aplicação rigorosa de decoradores de sessão (`@login_required`) em todas as rotas sensíveis e formulários, bloqueando acessos anónimos.
- Proteção contra SQL Injection: Utilização de ORM (SQLAlchemy) com consultas parametrizadas para a persistência em SQLite, isolando a base de dados de injeções maliciosas.
- Usabilidade e Legibilidade: Refatoração dos alertas de feedback utilizando redundância visual múltipla (ícone, cor e texto descritivo), atendendo aos critérios de acessibilidade e clareza do sistema.

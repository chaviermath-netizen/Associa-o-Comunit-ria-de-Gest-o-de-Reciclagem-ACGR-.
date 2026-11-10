refactor(architecture): estruturação modular do backend em camadas com Flask e SQLAlchemy

- Modularização: Separação clara entre os modelos de dados ORM (User e Chamado), a lógica de controlo de rotas e as views HTML, garantindo a manutenibilidade do código.
- Persistência e Segurança: Utilização de SQLite com SQLAlchemy para isolar as transações e aplicação de hashes criptográficos (Werkzeug) nas credenciais de acesso.
- Conformidade: Alinhamento das rotas protegidas por decorators de sessão (@login_required) e estruturação das interfaces sob diretrizes de acessibilidade WCAG 2.1 AA.

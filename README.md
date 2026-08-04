# HelpDesk Pro

Sistema de gerenciamento de chamados técnicos desenvolvido em Python com Flask.

## Objetivo

Este projeto tem como objetivo simular um sistema de Help Desk utilizado em empresas para gerenciamento de solicitações de suporte técnico.

Além da implementação das funcionalidades, o projeto está sendo desenvolvido seguindo boas práticas de arquitetura, organização de código e versionamento com Git.

---

## Tecnologias

- Python 3.13
- Flask
- SQLite
- SQLAlchemy
- Bootstrap 5
- HTML5
- CSS3
- JavaScript

---

## Estrutura do Projeto

```
helpdesk-system/

├── app.py
├── config.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
│
├── database/
│     chamados.db
│
├── routes/
│     chamados.py
│     usuarios.py
│
├── static/
│     css/
│     js/
│
├── templates/
│     base.html
│     index.html
│     chamados.html
│     novo.html
│     editar.html
│     login.html
```

---

## Roadmap

- [x] Estrutura inicial do projeto
- [ ] Configuração do SQLAlchemy
- [ ] Criação do banco SQLite
- [ ] Modelagem das entidades
- [ ] CRUD de chamados
- [ ] Sistema de login
- [ ] Dashboard
- [ ] API REST
- [ ] Docker
- [ ] Deploy

---

## Licença

Projeto desenvolvido para fins de estudo e portfólio.

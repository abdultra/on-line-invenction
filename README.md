# on-line-invenction
on-line-invenction

---

Sistema de Gestão de Laboratório Clínico e Banco de Sangue

Este projeto é um sistema de gestão para um laboratório clínico e banco de sangue, com foco na organização de doações de sangue, transfusões e gerenciamento de estoque. O sistema foi desenvolvido utilizando o Django, um framework web Python, e pode ser usado por organizações de saúde para gerenciar os processos de doação e transfusão de sangue, além de manter o controle de estoque de sangue de forma eficiente.


---

Pré-requisitos

Antes de rodar o projeto, verifique se você tem as seguintes dependências instaladas:

Python 3.x

Django 4.x ou superior

MariaDB ou MySQL

Dependências do projeto (veja a seção "Instalação" para detalhes)



---

Instalação

Siga os passos abaixo para configurar o projeto em seu ambiente local.

1. Clone o repositório:

git clone https://github.com/abdultra/on-line-invenction.git

2. Crie um ambiente virtual:

python -m venv venv

3. Ative o ambiente virtual:

No Windows:


venv\Scripts\activate

No Linux/Mac:


source venv/bin/activate

4. Instale as dependências:

pip install -r requirements.txt

5. Configure o banco de dados

Este projeto usa MariaDB ou MySQL como banco de dados. Para configurá-lo:

Crie um banco de dados no MariaDB/MySQL:


CREATE DATABASE on_line_health;

Crie um arquivo .env na raiz do projeto para armazenar as credenciais do banco de dados:


DB_NAME=on_line_health
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306

Ou edite diretamente o arquivo settings.py do Django, configurando as credenciais do banco de dados.

6. Execute as migrações:

python manage.py migrate

7. Crie um superusuário (opcional, mas necessário para acessar o painel admin):

python manage.py createsuperuser


---

Uso

Depois de configurar o ambiente, você pode rodar o servidor local para testar o sistema.

1. Rodar o servidor de desenvolvimento:

python manage.py runserver

2. Acesse o painel admin

O painel de administração do Django pode ser acessado em http://127.0.0.1:8000/admin/ após rodar o servidor. Use as credenciais do superusuário que você criou para acessar a área administrativa.


---

Funcionalidades

Gestão de Doações: Cadastro de doadores, registro de doações de sangue e controle de tipos sanguíneos.

Gestão de Transfusões: Registro de transfusões realizadas, associando o paciente ao sangue doado.

Controle de Estoque de Sangue: O estoque de sangue é automaticamente atualizado com base nas doações e transfusões.

Administração de Usuários: Acesso completo ao sistema por meio do painel admin do Django.



---

Contribuindo

Se você deseja contribuir para o desenvolvimento do projeto, siga os passos abaixo:

1. Faça um fork do repositório.


2. Crie uma nova branch para sua funcionalidade (git checkout -b nova-feature).


3. Faça as alterações necessárias.


4. Comite as alterações (git commit -am 'Adiciona nova feature').


5. Envie para o repositório remoto (git push origin nova-feature).


6. Crie um pull request.




---

Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.


---

Tecnologias Usadas

Django: Framework web em Python utilizado para o desenvolvimento da aplicação.

MariaDB/MySQL: Banco de dados utilizado para armazenar as informações do sistema.

Bootstrap: Framework para design responsivo.

JavaScript: Para interatividade no front-end.

Python: Linguagem principal do projeto.



---

Autor

Abdul Daniel Trato.


---

Essa documentação fornece uma visão geral do projeto, suas funcionalidades, e como configurá-lo e usá-lo localmente. Você pode personalizar conforme necessário, incluindo mais detalhes específicos sobre o seu projeto.
# Site Rede Neural

## Como desenvolver?

1. Clone o repositório.
1. Crie um virtualenv com Python 3.6
1. Ative o virtualenv.
1. Instale as dependências.
1. Configure a instância com o .env
1. Execute os testes.
1. Execute o runserver.

```console
git clone git@github.com:RedeNeural/site.git
cd schedules
virtualenv env --python=python3 # python 3.6 ou mais atual
source env/bin/activate
pip install -r requirements_dev.txt
cp contrib/env-sample .env
coverage run --source='.' manage.py test -v 2 ; coverage report --show-missing
python manage.py runserver
```

## Qualidade do código

```console
pre-commit install
flake8 --config=.flake8
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
1. Envie as configurações para o heroku.
1. Define um SECRET_KEY segura para instância.
1. Defina DEBUG=True


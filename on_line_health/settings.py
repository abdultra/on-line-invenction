import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR=Path(__file__).resolve().parent.parent

# Configurações básicas
SECRET_KEY = 'gdtyuouujh577gfd+-@:;_"#@##"''""%[=\}=`yydvni8653rdgjifbvr753eu88hhfissoudoretirareu/-1336558cxcgtrdxDSTYYJVCFUIJVF:-__/))0986_4566&'

DEBUG=True
ALLOWED_HOSTS = []

# Aplicações instaladas
INSTALLED_APPS=[
	'blood_bank',
	'paciente',
	'home',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

# Middlewares
MIDDLEWARE=[
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs e WSGI
ROOT_URLCONF='on_line_health.urls'
WSGI_APPLICATION='on_line_health.wsgi.application'

# Banco de Dados (Melhorando para MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Nome do banco de dados
        'USER': 'trato',     # Nome do usuário
        'PASSWORD': 'root',  # Senha do usuário
        'HOST': 'localhost', # Endereço do banco de dados (localhost no caso)
        'PORT': '5432',      # Porta padrão do PostgreSQL
    }
}
# Validação de Senhas
AUTH_PASSWORD_VALIDATORS=[
	{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
	{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
	{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
	{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configurações de Idioma e Fuso Horário
LANGUAGE_CODE='pt-MZ'
TIME_ZONE='Africa/Maputo'
USE_I18N=True
USE_L10N=True
USE_TZ=True

# Configuração de arquivos estáticos e mídia
STATIC_URL='/static/'
STATICFILES_DIRS=[BASE_DIR/'static']
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/'media'

# Sistema de Templates
TEMPLATES=[
	{
		'BACKEND':'django.template.backends.django.DjangoTemplates',
		'DIRS':[BASE_DIR/'templates'],
		'APP_DIRS':True,
		'OPTIONS':{
			'context_processors':[
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

# Configurações de segurança
SECURE_BROWSER_XSS_FILTER=True
X_FRAME_OPTIONS='DENY'
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True

# Configuração padrão para chaves automáticas
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
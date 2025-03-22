import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Caminho base do projeto
BASE_DIR=Path(__file__).resolve().parent.parent

# Configurações básicas
SECRET_KEY=os.getenv('SECRET_KEY', 'sua_chave_secreta_super_segura')
DEBUG=os.getenv('DEBUG', 'False')=='True'
ALLOWED_HOSTS=os.getenv('ALLOWED_HOSTS', '').split(',')

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

	# Aplicações de terceiros
	'crispy_forms',
	'crispy_bootstrap5',

	# Suas aplicações
	'core',
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
DATABASES={
	'default':{
		'ENGINE':'django.db.backends.mysql',
		'NAME':os.getenv('DB_NAME'),
		'USER':os.getenv('DB_USER'),
		'PASSWORD':os.getenv('DB_PASSWORD'),
		'HOST':os.getenv('DB_HOST', 'localhost'),
		'PORT':os.getenv('DB_PORT', '3306'),
		'OPTIONS':{'charset':'utf8mb4'},
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
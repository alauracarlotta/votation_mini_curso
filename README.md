# Starting django project

Esse projeto tem a contribuição das aulas:

* [CANAL Hashtag Programação - Lira da Hastag - Explicação Estrutura básica de um projeto em Django](https://www.youtube.com/watch?v=4u0aI-90KnU)
* [CANAL Hashtag Programação - Daniel Candioto - Mini Curso](https://www.youtube.com/watch?v=kSrH89eBm_A&t=66s)
* [Link Projeto do Mini Curso](github.com)

## PRIMEIROS PASSOS

* Criar a máquina virtual do projeto
  * In: python3 -m venv .venv

* Subir a máquina virtual do projeto
  * In: source .venv/bin/activate

    _Cair a máquina virtual do projeto => In: deactivate_

* Instalar o django na máquina
  * In: pip install django

    _Checar que o danjo está instalado (erro) =>
    In: django-admin_
    Out:
        Type 'django-admin help __subcommand__' for help on a specific subcommand.

        Available subcommands:

        [django]
            check
            compilemessages
            createcachetable
            dbshell
            diffsettings
            dumpdata
            flush
            inspectdb
            loaddata
            makemessages
            makemigrations
            migrate
            optimizemigration
            runserver
            sendtestemail
            shell
            showmigrations
            sqlflush
            sqlmigrate
            sqlsequencereset
            squashmigrations
            startapp
            startproject
            test
            testserver
        Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).

* Startar o projeto
  * In: django-admin startproject <nome_do_projeto>

    * Será criada uma pasta com o nome do projeto e um arquivo de nome <manage.py> => Gerencia o projeto

* Subir o projeto
  * Entrar na pasta do projeto
    * In: cd <nome_da_pasta>
    * In: python manage.py runserver
    * Out:
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        September 23, 2024 - 19:30:33 => [__PODE VARIAR__]
        Django version 5.1.1, using settings 'rent_control.settings'
        Starting development server at [http://127.0.0.1:8000/]
        Quit the server with CONTROL-C.

  * Irá criar o banco de dados, o arquivo <db.sqlite3>
  * Esse arquivo, manage.py é muito importante pois geralmente é com ele que rodamos o projeto (sobe o servidor, gerencia o banco de dados)

## PARA ENTENDER - CRIANDO O PROJETO

PASTA <nome_do_projeto>

* ARQUIVOS CRIADOS:
  * __init__.py
        => Módulo do projeto. (Ativa a navegação de pastas)

  * asgi.py
        => Tanto asgi.py quanto wsgi.py serão files python referentes a que tipo de servidor será usado para por o seu projeto no ar. Geralmente usado no fim de um projeto.

  * settings.py
        => Todas as configs do seu projeto
        Ex: Qual é a pasta do meu projeto que tem os templates que eu vou usar?
            Qual é a chave token do meu projeto pra não acessarem o meu banco de dados?
            Quais são os apps instalados no seu site?
            Qual a linguagem que você usa no seu site?
                LANGUAGE_CODE = en-us ou pt-br
            Qual o time-zone (fuso horário)?
                TIME-ZONE = UTC

  * urls.py
        => Local a definir os links do seu site
  * wsgi.py
        => Tanto asgi.py quanto wsgi.py serão files python referentes a que tipo de servidor será usado para por o seu projeto no ar. Geralmente usado no fim de um projeto.

## PARA ENTENDER - CRIANDO OS APPS

Cada app é como se fosse uma parte do projeto: login, pagamento, etc

* Cada app do meu projeto
  * In: python manage.py startapp <nome_do_app>

  * Na pasta principal, assim que criado o app, devo ir em /<nome_do_pojeto>/settings.py
    * Adicionar em 'INSTALLED_APPS' o <nome_do_app> criado.
      EX:
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            '<nome_do_app>'
        ]

Assim que criado o app, o django cria os seguintes arquivos (recursos do framework):

* /migrations => Gerencia as modificações no banco de dados
* __init__ => => Módulo do projeto. (Ativa a navegação de pastas)
* admin => O que vai aparecer na tela do dono do site, o usuário do site
* app => Configura os apps do 'APP' (no caso houses é um app e houses pode ter vários apps. o padrão é cada app ter um app só.)
* models => Gerencia as informações que serão armazenadas no banco de dados. Quais tabelas, Quais campos, etc.
    Ex:
        Casas
        Categoria
        Usuários
        Endereços
        etc.
* tests => Gerencia os testes da aplicação
* views => Lógica por trás do seu site. (Lógica por trás das telas, das vizualisações)
    É NESSE ARQUIVO QUE VOCÊ IRÁ VINCULAR O BACKEND DO SITE COM OS TEMPLATES QUE É O FRONTEND DO SITE (html/css/javascript).
    A PASTA 'TEMPLATES' PODE SER CRIADA TANTO DENTRO DE CADA APP ASSIM COMO UM ÚNICO (na mesma hierarquia do manage.py)
    Ex:
        Quando o usuário clicar no link 'houses' o que eu quero que carregue pra ele? (Define as funções, classes, etc) Se ele não estiver logado, eu quero que carregue pra ele a página de login,...

***

## NESSE PROJETO

* PASSO 1:

### Criar a primeira página do site

=> file __views.py__
    1. Criar a vizualização do site, criando a def index
    2. Atrelar essa vizualisação a uma URL, nesse caso é necessário criar um arquilo urls.py para este aplicativo

=> file __urls.py__ (do app)
    In:  
        `from django.urls import path`  
        `from . import views`           >>>views do app vigente

        `urlpatterns = [
            path('', views.index, name='index')
        ]`

=> file __urls.py__ (do projeto)
    Incluir esse path no urls do projeto
    1. Abrir /<nome_do_pojeto>/urls.py
    2. Adicionar
        EX:  
            `from django.contrib import admin`  
            `from django.urls import include, path`  

            `urlpatterns = [
                path('poll/', include('poll.urls')),
                path('admin/', admin.site.urls),
            ]`
    
    3. Podemos verificar se o mesmo deu certo, subindo o servidor. Neste caso ainda ocorrerá um erro conforme a imagem a seguir:  

![Erro URL](assets/images/erro_url.png)

    Precisamos acessar a página criada que está em /poll (conforme url criada)

![URL com Sucesso](assets/images/url_com_sucesso.png)

* PASSO 2:

### Criando nosso banco de dados

=> file __settings.py__ (do projeto)
    1. Abrir /<nome_do_pojeto>/settings.py
    Mudamos de:
        * LANGUAGE_CODE = 'en-us'
        PARA:    LANGUAGE_CODE = 'pt-br'

        * TIME_ZONE = 'UTC'
        PARA:    TIME_ZONE = 'America/Sao_Paulo'

    2. Criar uma migração para jogar para o banco de dados
    In: python manage.py migrate

    Out:
        Operations to perform:
            Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying sessions.0001_initial... OK

    PODEMOS ABRIR O DB BROWSER FOR SQLITE E ENCONTRAREMOS O BANCO INICIALIZADO, com as tabelas criadas e tudo mais:

![DB Inicializado](assets/images/db_inicializado.png)

=> file __models.py.py__ (do app)

    3. Criar o modelo em models.py que vai definir como os nossos dados serão tratados e esse modelo irá gerar informações para o banco de dados: 

        Ex:  
        `from django.db import models`  

        `class Questions(models.Model):
            question_text = models.CharField(max_length=200)
            pub_date = models.DateTimeField('date published')

        class Choice(models.Model):
            question = models.ForeignKey(Questions, on_delete=models.CASCADE)
            choice_text = models.CharField(max_length=100)
            votes = models.IntegerField(default=0)
    
    4. Em seguida, da mesma maneira que fizemos a migração para todo o sistema, agora iremos fazer para as mudanças adicionadas nesse models.

        => file __apps.py__ (do app)
        Em apps.py conseguimos ver que o django criou o seguinte condigo:

            `from django.apps import AppConfig`  

            `class PollConfig(AppConfig):
                default_auto_field = 'django.db.models.BigAutoField'
                name = 'poll'`
    
    5. Iremos pegar as infos de apps.py e jogar para os apps instalados do projeto.
        => file __settings.py__ (do projeto) 
        Ex:
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            ]
        
        Iremos adicionar:
        In: 'poll.apps.PollConfig'

        Out:
            INSTALLED_APPS = [
                'poll.apps.PollConfig',
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            ]

    6. Usamos o comando para executar a migração, a criar essa migração. Sempre serão duas etapas:
        In: `python manage.py makemigrations`
        Out:
            poll\migrations\0001_initial.py
              - Create model Questions
              - Create model Choice
        
        In: `python manage.py migrate`
        Out:
            Operations to perform:
            Apply all migrations: admin, auth, contenttypes, poll, sessions
            Running migrations:
            Applying poll.0001_initial... OK
        
        Em nosso db podemos verificar:
![DB Tabela adicionada](assets/images/db_tabela_adicionada.png)
![DB Verificando Tabela](assets/images/db_verificando_tabela.png)
![DB Verificando Tabela Questions](assets/images/db_verificando_tabela_questions.png)
![DB Verificando Tabela Choice](assets/images/db_verificando_tabela_choice.png)

### CRIANDO NOSSAS PERGUNTAS

1. Entre no ambiente Shell
    In: `python manage.py shell`

    Out:
        Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> Abre um console interativo

    Irá interferir diretamente no banco:

    In: from poll.models import Questions, Choice
    In: Questions.objects.all()
    Out: <QuerySet []>  >>> Me trás todos os objetos que foram instanciados nessa classe Questions

    In: from django.utils import timezone
    In: q = Questions(question_text='Você é feliz?', pub_date=timezone.now())

    In: print(q)
    Out: Você é feliz?

    In: q.save()
    In: q.id
    Out: 1

    In: q.question_text
    Out: 'Você é feliz?'
    In: Questions.objects.all()
    Out: <QuerySet [<Questions: Question Object (1)>]>

2. Para não aparecer o <Queryset [<Questions: Object (1)>]> como está criamos uma função na models, para que a apresentação sejá descrita em string e não como object:

    class Questions(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

        PARA: `def __str__(self):`
                    `return self.question_text`

    class Choice(models.Model):
        question = models.ForeignKey(Questions, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=100)
        votes = models.IntegerField(default=0)

        PARA: `def __str__(self):`
                    `return self.choice_text`

    Voltando para o shell e executando a linha de código outra vez, o resultado será:

    In: Questions.objects.all()
    Out: <QuerySet [<Questions: Você é feliz?>]>

    Vide imagem:
    ![DB Pegunta Adicionada](assets/images/db_pergunta_adicionada.png)

3. Para pegar as perguntas mais recentes:
    Adiciono a linha referente ao tempo:

        from django.db import models
        from django.utils import timezone
        from datetime import datetime

        class Questions(models.Model):
            question_text = models.CharField(max_length=200)
            pub_date = models.DateTimeField('date published')
            
            def __str__(self):
                return self.question_text

            PARA: `def was_published_recently(self):`
                        `return self.pub_date >= timezone.now() - datetime.timedelta(days=1)`

        class Choice(models.Model):
            question = models.ForeignKey(Questions, on_delete=models.CASCADE)
            choice_text = models.CharField(max_length=100)
            votes = models.IntegerField(default=0)
            
            def __str__(self):
                return self.choice_text

### CRIANDO NOSSAS ALTERNATIVAS

    => File __models.py__ (do app)
    Na class Choice, temos:
    * question (ForeignKey => Atrela as opções a pergunta)
    * choice_text (Quais são os textos das alternativas)
    * votes (computabilidade dos votos por alternativa)

    No terminal, com shell:
    In: from poll.models import Questions, Choice

    In: Questions.objects.all()
    Out: <QuerySet [<Questions: Você é feliz?>]>

    In: q = Questions.objects.get(id=1)     => Salve em 'q' a pergunta de id 1
    In: print(q)
    Out: <Questions: Você é feliz?>

    In: q.choice_set.all()
    Out: <QuerySet []>

    In: q.choice_set.create(choice_text='Com certeza', votes=0)
    >>> Crie em 'q' (sob a pergunta já atrelada) a alternativa com texto 'x' e qtde de votos 'n'
    Out: <Choice: Com certeza>

    In: q.choice_set.create(choice_text='Não muito...', votes=0)
    Out: <Choice: Não muito...>

    In: q.choice_set.all()      => Todas as alternativas adicionadas
    Out: <QuerySet [<Choice: Com certeza>, <Choice: Não muito...>]>

## O TAL DO 'ADMIN'

1. Criamos um usuario administrador:
    In: `python manage.py createsuperuser`
    Out:
        Usuário (leave blank to use 'laura-carlotta'): admin
        Endereço de email: [alauracarlotta@gmail.com]
        Password:  
        Password (again):  
        Esta senha é muito curta. Ela precisa conter pelo menos 8 caracteres.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

    In: `python manage.py runserver`

    In: [http://127.0.0.1:8000/admin/] teremos o seguinte:

    ![Tela de Login do Admin](assets/images/admin-login.png)

    >>> Depois de logado, nosso sistema de administrador será da seguinte forma:

    ![Sistema do Admin](assets/images/admin-sistema.png)

2. Para adicionar nossas perguntas e respostas no admin também, faremos o seguinte:
    => File __admin.py__
        Adicionamos:
            `from django.contrib import admin`
            `from .models import Questions`

            `admin.site.register(Questions)`

## CRIANDO NOVAS VIEW

Vamos criar:

* Lista com todas as perguntas
* Sobre cada pergunta abrirá uma página com as alternativas
* Resultados das votações

1. Criamos todas as views que queremos:

    def index(request):
        return HttpResponse('Olá mundo!')

    def detail(request, question_id):
        return HttpResponse('Essa é a pergunta de número %s' %question_id)

    def results(request, question_id):
        return HttpResponse('Esses são os resultados da pergunta de número %s' %question_id)

    def vote(request, question_id):
        return HttpResponse('Você está votando na questão de número %s' %question_id)

2. Especificando cada uma:
    def index(request):
        latest_question_list = Questions.objects.order_by '-pub_date' [:5]
            # Ordena as últimas 5 perguntas com base na data de publicação;
        context = {'latest_question_list': latest_question_list}
            # monta a variavel em objeto para como vai aparecer lá na página;

        return render(request, 'poll/index.html', context) 
            # 'render' => 'renderiza' a página pra mim baseada em uma request na página poll/index.html (que será criada) e mostra o valor 'context'.

3. Para criar um template em django é necessário criá-lo da seguinte forma:
    => No Dir do app:
    * Cria a pasta 'template'
    * Dentro de 'template' cria a pasta com o nome do app
    * E dentro da pasta do app, cria o arquivo com nome de 'index.html'

    E construimos um html da seguinte forma:

    `<!DOCTYPE html>`
    `<html lang="pt-br">`
    `<head>`
        `<meta charset="UTF-8">`
        `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
        `<title>Enquete - poll</title>`
    `</head>`
    `<body>`
        <!-- Olha lá na lista que a gente criou -->
        `{% if latest_question_list %}`
            <!-- para cada item da lista -->
            `<ul>`
                `{% for question in latest_question_list %}`
                <!-- Crie o item -->
                    `<li>`
                        `<a href="{% url 'poll:vote' question_id %}">`
                            `{{ question.question_id}}`
                        `</a>`
                    `</li>`
                `{% endfor %}`
            `</ul>`
        <!-- Se não, mostre -->
        `{% else %}`
            `<p>No poll are avaliable.</p>`
        `{% endif %}`
    `</body>`
    `</html>`

4. No file __urls.py__, em urlpatterns adcionamos:
    `app_name = 'poll'`
    `urlpatterns = [`
        `path('', views.index, name='index'),`
        `path('<int:question_id>/results/', views.results, name='results'),`
        `path('<int:question_id>/vote/', views.vote, name='vote'),`
    `]`

    No file __views__.py

    `def index(request):`
        `latest_question_list = Questions.objects.order_by('-pub_date'):5`
        `context = {'latest_question_list': latest_question_list}`
        `return render(request, 'poll/index.html', context)`

5. Costruindo as outras páginas:

=> vote.html

`<!DOCTYPE html>`
`<html lang="en">`
`<head>`
    `<meta charset="UTF-8">`
    `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
    `<title>Vote na Enquete</title>`
`</head>`
`<body>`
    `<form action="{% url 'poll:vote' question.id %}" method="post">`
        `{% csrf_token %}`
        `<fieldset>`
            `<legend>`
                `<h1>{{ question.question_text }}</h1>`
            `</legend>`
            `{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}`
            `{% for choice in question.choice_set.all %}`
                `<input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">`
                `<label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>`
            `{% endfor %}`
        `</fieldset>`
        `<input type="submit" value="Vote">`
    `</form>`
`</body>`
`</html>`

=> No file __views__.py

`def vote(request, question_id):`
    `question = get_object_or_404(Questions, pk=question_id)`
    `try:`
        `selected_choice = question.choice_set.get(pk=request.POST['choice'])`
    `except KeyError:`
        `return render(request, 'poll/vote.html',{`
            `'question': question,`
            `'error_message': "You didn't select a choice"`
        `})`
    `else:`
        `selected_choice.votes += 1`
        `selected_choice.save()`
        `return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))`

=> results.html

`<!DOCTYPE html>`
`<html lang="en">`
`<head>`
    `<meta charset="UTF-8">`
    `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
    `<title>Resultado da Enquete - results</title>`
`</head>`
`<body>`
    `<h1>{{ question.question_text }}</h1>`
    `<ul>`
        `{% for choice in question.choice_set.all %}`
            `<li>`
                `{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}`
            `</li>`
        `{% endfor %}`
    `</ul>`
    `<a href="{% url 'poll:vote' question.id %}">Vote again? </a>`
    `<a href="{% url 'poll:index' %}">See other poll?</a>`
`</body>`
`</html>`

=> No file __views__.py

`def results(request, question_id):`
    `question = Questions(pk=question_id) # pk = primary key`
    `return render(request, 'poll/results.html', {'question': question})`

## Plus Well no admin

=> File __admin__.py

`from django.contrib import admin`
`from .models import Questions, Choice`

`class ChoiceTabularInline(admin.TabularInline):`
    `model = Choice`
    `extra = 0`

`@admin.register(Questions)`
`class QuestionAdmin(admin.ModelAdmin):`
    `inlines = [ChoiceTabularInline]`

    => Criamos de forma tabular a ligação no admin de perguntas/alternativas

## Plus Well para debug

pprint => Ajuda na identação de um file .json, por exemplo.
logger
import logging

logger = logging.getLogger(__name__)
    => Formas de debuggar o código.

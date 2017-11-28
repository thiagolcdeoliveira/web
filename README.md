# web
## Trabalho de web - Sistema desenvolvido com base no tutorial  do tango with Django 

### Linguagens Utilizadas 

* HTML5
* CSS3
* JS
* Python 

### Framework 

* Django 1.9

### Como instalar

* Configurar o ambiente
  * Intalar o Git
    * apt install git
  * Instalar a virtualenvwrapper
    * apt install python-pip
    * pip install virtualenvwrapper [Configuração](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  * Criar uma virtualenv
    * mkvirtualenv <nome_projeto>
      * Após criada ela executara o ambiente virtual, porém nas próximas vezes será necessario executar o comando workon <nome_projeto>
 * Instalar Postfix
    * pip install postfix
 * Instalar GetText
    * Obs: No windows [Configuração](http://gnuwin32.sourceforge.net/packages/gettext.htm), no Linux é pip que está no requirements.txt
    
### Respositório
* Baixar 
    * git clone https://github.com/thiagolcdeoliveira/web.git
    * ative a virtualenv criada
         * workon <nome_projeto>
    * Na raiz  do projeto (web) 
         * python manage.py makemigrations
         * python manage.py migrate
         * python manage.py runserver
    * acesse 
         * http://localhost:8000
 

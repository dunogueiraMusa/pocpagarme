# POC Pagar.me

Api rest em python com conteiner docker.

## Prerequisites :gear:	
```bash
$ git
$ Python
$ Editor de texto, de preferencia Pycharm
$ docker & docker compose
``` 
# Get the code
git clone  git@github.com:dunogueiraMusa/pocpagarme.git

``` 
### Start the app in Docker :whale:		
```bash
# build docker image
# docker-compose up

### Como foi feito 		
```bash
# Desenvolvido uma API Rest em Flask de consultas de usuários;
$ Get/users retornará os users contidos no "banco de dados"
$ POST deverá ser preenchido em formado JSON apenas com o nome, caso quiser colocar o ID será inserido também.
$ PUT Ao inserir Nome e ID, subistituirá o ID atual. 
$ DELETE Colocando o User & ID será deletado de imediato. 
$
#Porque Flask?
$ Flask escolhido por se tratar de ser microframework, que é mais leve, poderoso, simples e grande rapidez, focado em aplicações web.
$

## Uma API básica e simples.
$ A imagem docker foi desenvolvida junto do docker-compose de acordo com as configurações:
# Dockerfile 
$ Dockerfile foi realizado com FROM Python:3-alpine por ser mais leve, praticamente 1/3 do peso das demais imagens. 

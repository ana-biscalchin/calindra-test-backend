
# Teste Calindra Backend
Aplicação em Python3 que consome a API Geocoding do Google e calcula a distância euclidiana entre dois pontos dados como endereços em linguagem natural.

### Desafio
A ideia do desafio é simples, entender como você pensa na hora de abordar os
problemas. Nas linguagens e tecnologias que se sentir mais confortável.
Criar uma API Rest que:
1) Receba dois ou mais endereços (ex: Av. Rio Branco, 1 Centro, Rio de Janeiro RJ,
20090003; Praça Mal. Âncora, 122 Centro, Rio de Janeiro RJ, 20021200; Rua 19 de
Fevereiro, 34 Botafogo, Rio de Janeiro RJ, 22280030 ) como parâmetros de entrada
2) Resolva a geolocalização entre os endereços utilizando a API do Google
https://developers.google.com/maps/documentation/geocoding/start
3) Após isso, com a latitude e longitude em mãos dos endereços, implementar o algoritmo de
cálculo de distância Euclidiana e aplicar em todas as combinações de endereços.
4) Retorne as distâncias calculadas entre os todos os endereços e indique os endereços
mais próximos e também os endereços mais distantes.

### Resultado

A linguagem escolhida foi Python3.

Desenvolvi um menu de interação que recebe os endereços e calcula a distância euclidiana, mas para apenas dois endereços.

### Requisitos
Para que possamos fazer requisições existe uma chave da API de Geocoding do Google que pode ser obtida por meio de uma conta teste, você pode obter a sua usando as seguintes instruções: 

>   Para obter uma chave de API: Visite o [Google Cloud Platform Console](https://console.cloud.google.com/). 
    Clique no menu suspenso do projeto e selecione ou crie o projeto ao qual deseja adicionar uma chave de API. 
    Clique no botão de menu e selecione APIs e serviços> Credenciais. 
    Na página Credenciais, clique em Criar credenciais> Chave da API. 
    O diálogo de chave de API criada exibe sua chave de API recém-criada. Clique em Fechar. 
    A nova chave da API está listada na página Credenciais, em Chaves da API.

**Para fins de avaliação desse projeto irei enviar o arquivo .env  com a chave de acesso aos avaliadores.** 

Coloque sua chave em um arquivo *.env* como o ._env.example_ contido nesse repositório.

Também foram usadas duas bibliotecas: [python-decouple versão 3.3](https://pypi.org/project/python-decouple/) e [googlemaps versão 4.4.1](https://pypi.org/project/googlemaps/)


### Rodando localmente

Clone o repositório e entre na pasta:

    $ git clone git@github.com:ana-biscalchin/calindra-test-backend.git
    $ cd calindra-test-backend/


Instale as dependências: 

    $ pip3 install python-decouple googlemaps

Execute o programa: 

    $ python3 app.py

### Roadmap

 - Implementar o cálculo de distância euclidiana para mais de dois endereços;
 - Implementar a tecnologia Docker para executar a aplicação com mais facilidade.

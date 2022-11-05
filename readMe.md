# Solution Comentary

A imagem é uma imagem simples, com pixels de cores contanstes e com alto contraste entre eles.

![imagem](ORIGINAL_PIC.png)

A ideia principal para resolver as 3 primeiras task foi a mesma:
- *separar apenas o que é relevante em uma imagem com fundo branco*
- contar tudo o que não for branco.

Para tal, utilizei o básico da manipualação de imagem, pedindo para `openCV` abrir os dados da imagem como uma matriz e manipular cada index dessa matriz.

De forma simples, uma imagem é compreendida pelo computador como:
`[posicaoY][posicaoX][RGB]`

portanto, ao analizar cada indice da matriz eu estou, de fato, analizando o valor RGB de cada pixel.

## task 1 - Count the number of Stars

As estrelas são representadas pela cor branca, RGB(255, 255, 255)

Essa task foi resolvida com duas etapas:
-  varrer a imagem original e para cada pixel que não for branco, pinta-lo de branco e para cada pixel que for branco, pinta-lo de preto
  - Essa etapa me resulta em uma imagem de fundo branco com todas as estrelas em preto
  - ![task1](./OUTPUT_IMAGES/blackStarsOnWhite.png)
- Varrer a imagem produzina na etapa 1 e contar cada pixel preto na imagem.

## task 2 - Count the number of Meteors

As estrelas são representadas pela cor vermelha, RGB(255, 0, 0)

Essa task foi resolvida com duas etapas:
-  varrer a imagem original e para cada pixel que não for branco, pinta-lo de branco.
  - Essa etapa me resulta em uma imagem de fundo branco com todas os meteoros em preto.
  - ![task2](./OUTPUT_IMAGES/redMeteorsOnWhite.png)
- Varrer a imagem produzina na etapa 1 e contar cada pixel vermelho na imagem.

## Extra Step on Task 1 and 2 - meteor/star fill

Para não repetir a contagem de uma estrela ou metoro caso o mesmo fosse maior que um pixel, (fazendo com que 1 estrela fosse contada várias vezes). Assim que uma estrela/meteoro era encontrado, foi aplciado uma função recursiva que pinta tudo que não é branco nos vizinhos em x e vizinhos em y do pixel encontrado, para branco.


## Task 3 - Meteor Direction

Para essa etapa, quando um meteoro é encontrado na task 2, antes de pintar os vizinhos, foi contabilizado a altura do mesmo em X e em Y, e se a altura em X fosse maior que a altura em Y, o mesmo foi considerado um meteoro movendo-se na horizontal

para descobrir quantos meteoros cairam na agua, diminui a quantidade de meteoros total com a quantidade dos meteoros que estão na horizal.


## Task 4 - Read Text

A principio eu achei que poderia haver um texto escrito e escondido com a layer de opacidade

escrevi um código para varrer a imagem e tudo que tivesse opacidade 100% ficasse branco e tudo com opacidade abaixo de 255 ficasse preto, e, conforme podemos ver na imagem, nada apareceu:

![task4](OUTPUT_IMAGES/lowAlphaOnly.png)

Apos isto, pensei que fosse um `connect the dots` e escrevi um códiigo para deixar em uma mesma imagem, todas as estrelas e os meteros, como podemos ver abaixo:

![task4.1](OUTPUT_IMAGES/dotsOnWhite.png)

Infelizmente não consigo identificar nenhuma letra e uma simples chamada do `pytesseract` não me retornou nenhum texto.

Preciso de mais informações para poder completar essa etapa.


## Meteor Challenge (Part 1)


Tasks:

- Count the number of Stars
- Count the number of Meteors
- If the Meteors are falling perpendicularly to the Ground (Water level), count how many will fall on the Water
- (optional) Find the phrase that is hidden in the dots in the sky. 
  - HINT 1: 177 Characters
  - HINT 2: Most of the last tasks’ code can be reused for this one

Please, send us the result and code you used to solve the tasks above. Explain how you achieved the results in each question. Good work!!

Subject: [CHALLENGE] [METEOR] *your name*

[Sample] Answers:

Number of Stars

Number of Meteors

Meteors falling on the Water

(optional) Hidden Phrase



Pixel Ref:

    (pure white)    Stars
    (pure red)      Meteors
    (pure blue)     Water
    (pure black)    Ground






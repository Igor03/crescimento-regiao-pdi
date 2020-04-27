# crescimento-regiao-pdi

## Introdução
Implementação de um método de segmentação de imagens, utilizando Python3 e a bibliotecas como OpenCV e NumPy, utilizando uma adaptação do método de Crescimento de Regiões (Image Growing).

## Implementação
A solução apresentada foi implementada utilizando a linguagem Python. No entanto, outros bibliotecatas foram utilizadas. Uma destas bibliotecas é a [OpenCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html).
Esta biblioteca possui diversas funções que facilitam aplicação de técnicas de processamento digital de imagens (PDI) como aplicação de filtros. Outra módulo importante para a conclusão deste trabalho foi o [NumPy](https://numpy.org/doc/). Esta biblioteca
é amplamanete utilizada em aplicações com de computação científica pois fornece diversas funções para trabalho com arrays multidimensionais, como imagens.

### Crescimento de Região
O processo de Segmentação por Crescimento de Regiões é, de certa forma, bem simples.
Inicialmente é preciso selecionar um conjunto de pontos para compor o que chamamos de semente
que por sua vez, nada mais é que o conjunto de pixels que são inicialmente incorporadas à região
que será expandida. Esta expansão ocorre mediante a um critério que chamaremos de Critério de
Agrupamento. Após a definição do Critério de Agrupamento, a semente é expandida e, então, obtemos a região de interesse.

### Resultados
As imagens abaixo mostram alguns dos resultados obtidos em imagens após a aplicação do método proposto.

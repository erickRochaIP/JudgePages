# Judge Pages

## Introdução

Quando os mecanismos de pesquisa como o Google exibem os resultados da pesquisa, eles o fazem colocando as páginas mais “importantes” e de maior qualidade em uma posição superior nos resultados da pesquisa do que as páginas menos importantes. Mas como o mecanismo de pesquisa sabe quais páginas são mais importantes do que outras?

Uma heurística pode ser que uma página “importante” é aquela para a qual muitas outras páginas estão vinculadas, uma vez que é razoável imaginar que mais sites serão vinculados a uma página da web de qualidade superior do que a uma página da web de qualidade inferior. Portanto, poderíamos imaginar um sistema em que cada página receba uma classificação de acordo com o número de links recebidos de outras páginas, e classificações mais altas indicariam uma importância maior.

Mas essa definição não é perfeita: se alguém quiser fazer sua página parecer mais importante, então, sob esse sistema, ele poderia simplesmente criar muitas outras páginas com links para a página desejada para aumentar artificialmente sua classificação.

Por esse motivo, o algoritmo PageRank foi criado pelos co-fundadores do Google (incluindo Larry Page, para quem o algoritmo foi nomeado). No algoritmo do PageRank, um site é mais importante se estiver vinculado a outros sites importantes, e links de sites menos importantes têm seus links menos ponderados. Essa definição é um pouco circular, mas existem várias estratégias para calcular essas classificações.

## Como usar

### python pagerank.py corpus

corpus é o diretório que você quer ranquear

## Projeto original

Projeto 2 do Curso: [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/weeks/2/)
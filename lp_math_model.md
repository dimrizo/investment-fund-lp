Mathematical IP model for problem solution. For the development of this .md file, this solution has been used: https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b

| Indices | Description |
|:---:|:---:|
| <img src="https://render.githubusercontent.com/render/math?math=\large k\in[1,\ 3]">| Index used for products |
| <img src="https://render.githubusercontent.com/render/math?math=\large i\in[1,\ 3]">| Index used for factories |
| <img src="https://render.githubusercontent.com/render/math?math=\large j\in[1,\ 3]">| Index used for markets |

| Parameters | Description |
|:---:|---|
| <img src="https://render.githubusercontent.com/render/math?math=\Large {UPC}_{ki}">| Unit production cost of product k at factory i |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {TC}_{kij}">| Transportation cost of product k from factory i to market j |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {SUC}_{ki}">| Set-up cost for the production of product k at factory i |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {MaxOP}_{ki}">| Maximum Output production of product k at factory i |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {MinOP}_{ki}">| Minimum Output production of product k at factory i |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {CR}_{ki}">| Capacity required (in man-hours) for the production of product k at factory i |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {TC}_i">| Total capacity (in man-hours) available at each factory i |
| <img src="https://render.githubusercontent.com/render/math?math=\Large D_{kj}">| Demand for product k in market j |

| Decision variables | Description |
|:---:|---|
| <img src="https://render.githubusercontent.com/render/math?math=\Large X_{kij}">| Positive integer variable, takes the value of the amount of products k produced at factory i and transferred to market j  |
| <img src="https://render.githubusercontent.com/render/math?math=\Large P_{ki}">| Binary variable, takes the value of 1 if product k is produced at factory i, or 0 otherwise |

| Cosntraints | Numbering |
|:---:|:---:|
| <img src="https://render.githubusercontent.com/render/math?math=\sum_{j\ =\ 1}^{3\ }X_{kij}\le\ {MaxOP}_{ki}\ast\ P_{ki},\ \forall\ k,i\in[1,\ 3]">| 1 |
| <img src="https://render.githubusercontent.com/render/math?math=\sum_{j\ =\ 1}^{3\ }X_{kij}\geq\ {MinOP}_{ki}\ast\ P_{ki},\ \forall\ k,i\in[1,\ 3]">| 2 |
| <img src="https://render.githubusercontent.com/render/math?math=\sum_{k\ =\ 1}^{3\ }\sum_{j\ =\ 1}^{3}{(X_{kij}\ast{CR}_{ki})}\geq\ {TC}_i,\ \forall\ i\in[1,\ 3]">| 3 |
| <img src="https://render.githubusercontent.com/render/math?math=\sum_{i\ =\ 1}^{3\ }X_{kij}\geq\ D_{kj},\ \forall\ k,j\in[1,\ 3] ">| 4 |
| <img src="https://render.githubusercontent.com/render/math?math=\sum_{k\ =\ 1}^{\ 3\ }P_{ki}\le\ 2,\ \forall\ i\in[1,\ 3] ">| 5 |
| <img src="https://render.githubusercontent.com/render/math?math=\sum_{i\ =\ 1}^{\ 3\ }P_{ki}\le\ 2,\ \forall\ k\in[1,\ 3] ">| 6 |

| Objective function | Numbering |
|:---:|:---:|
| <img src="https://render.githubusercontent.com/render/math?math=MINIMIZE   \ \sum_{k\ =\ 1}^{3}\sum_{i\ =\ 1}^{3}{\sum_{j\ =\ 1}^{3}{(X_{kij}\ast({UPC}_{ki}%2B{TC}_{kij}))}\ }%2B\sum_{k=1}^{3}\sum_{i=1}^{3}{P_{ki}\ast{SUC}_{ki}}">| 7 |

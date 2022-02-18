Mathematical LP model for the investment problem solution. For the development of this .md file, this solution has been used: https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b

| Indices | Description |
|:---:|:---:|
| <img src="https://render.githubusercontent.com/render/math?math=\large i\in[1,\ 5]">| *Index used for investment project* |

| Parameters | Description |
|:---:|---|
| <img src="https://render.githubusercontent.com/render/math?math=\Large {PRR}_{i}">| *Return rate per investment project i* |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {TA}">| *Maximum total amount available to invest* |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {maxOI}">| *Maximum amount to invest in the Oil Industry* |
| <img src="https://render.githubusercontent.com/render/math?math=\Large {maxSI}">| *Maximum amount to invest in the Steel Industry* |

| Decision variables | Description |
|:---:|---|
| <img src="https://render.githubusercontent.com/render/math?math=\Large X_{i}">| *Positive continous variable, takes the value of the amount invested in each project.*  |

| Cosntraints | Numbering |
|:---:|:---:|
| <img src="https://render.githubusercontent.com/render/math?math=\sum_{i\ =\ 1}^{5\ }X_{i}\le\ TA">| *1* |
| <img src="https://render.githubusercontent.com/render/math?math=X_1%2BX_2\le\ maxOI">| *2* |
| <img src="https://render.githubusercontent.com/render/math?math=X_3%2BX_4\le\ maSI">| *3* |
| <img src="https://render.githubusercontent.com/render/math?math=X_5\geq 0.25 \ast\left(X_3%2BX_4\right)">| *4* |
| <img src="https://render.githubusercontent.com/render/math?math=X_2\le 0.6 \ast\left(X_1%2BX_2\right)">| *5* |

| Objective function | Numbering |
|:---:|:---:|
| <img src="https://render.githubusercontent.com/render/math?math=MAXIMIZE \sum_{i=1}^{5}{{\rm PRR}_i*X_i}">| *6* |

** Answers provided when Python script is run **

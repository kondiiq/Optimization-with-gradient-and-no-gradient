# Optimization-with-gradient-and-no-gradient-methods

The project consists of 4 stages 
<p align="center">
 Stage 1 
</p>
Preparation of a computer application that calculates the value of the target function.
Description of the optimization problem in the report - description of the objective function (including graph
surface and contour plot for functions of 2 variables). 
<p align="center">
Stage 2 
</p>
Preparation of a gradientless optimization method. Description of the method in the report. 
<p align="center">
Stage 3
</p>
Preparation of the gradient optimization method. Description of the method in the report.
<p align="center">
Stage 4
</p>
Compare the operation of different methods and the effect of different parameter settings. Description
conducted research in the report. 

## Table of contents
* [Qing function](#Qing-function)
* [Alpine function](#Alpine-function)
* [Technologies](#technologies)
* [Setup](#setup)



### Qing function

<br/>
<img src="https://render.githubusercontent.com/render/math?math=f(x_2) = \sum_{i=1}^{N} (x_{i}^{2} - i^{2})^{2}"/> <br/>
<img src="https://render.githubusercontent.com/render/math?math=With  restrictions :-500 \leq x_i \leq 500"/> <br/>
<img src="https://render.githubusercontent.com/render/math?math=x^{*} = ( \pm \sqrt{i}, ...,\pm \sqrt{i}), f(x^{*}) = 0"/> <br/>


### Alpine function
	
<br/>
<img src="https://render.githubusercontent.com/render/math?math=f(x_2) = \sum_{i=1}^{N} \mid x_{i} sin(x_{i}) + 0.1 x_i \mid" title="Alpine function" /> <br/>
<img src="https://render.githubusercontent.com/render/math?math=With  restrictions : -10 \leq x_i \leq 10" title="Alpine function search space" /> <br/>
<img src="https://render.githubusercontent.com/render/math?math=x^{*} = (0, ..., 0), f(x^{*}) = 0" title="Alpine function search space local global minimum" /> <br/>

## Technologies
Project is created with:
* Python: 3.9
* NumPy 1.22.2
* MatplotLib 3.5.1
	
## Setup
To run this project, install it locally using pip:

```
$ pip install --upgrade pip
$ pip install numpy
$ pip install matplotlib
$ git glone https://github.com/kondiiq/Optimization-with-gradient-and-no-gradient.git project
$ cd project
$ python3 QingFunc.py 
$ python3 AlpineFunc.py 
```

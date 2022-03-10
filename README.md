# Optimization-with-gradient-and-no-gradient-methods

## Table of contents
* [General info](#general-info)
* [Qing function](#Qing-function)
* [Alpine function](#Alpine-function)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.

### Qing function

<br/>
<img src="https://latex.codecogs.com/svg.latex?\Large;f(x_2) = \sum_{i=1}^{N} (x_{i}^{2} - i^{2})^{2}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> 
<img src="https://latex.codecogs.com/svg.latex?\Large;p.o :-500 \leq x_i \leq 500" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> 
<img src="https://latex.codecogs.com/svg.latex?\Large;x^{*} = ( \pm \sqrt{i}, ...,\pm \sqrt{i}), f(x^{*}) = 0" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> <br/>


### Alpine function
	
<br/>
<img src="https://latex.codecogs.com/svg.latex?\Large;f(x_2) = \sum_{i=1}^{N} \mid x_{i} sin(x_{i}) + 0.1 x_i \mid" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> <br/>
<img src="https://latex.codecogs.com/svg.latex?\Large;p.o : -10 \leq x_i \leq 10" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> <br/>
<img src="https://latex.codecogs.com/svg.latex?\Large;x^{*} = (0, ..., 0), f(x^{*}) = 0" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> <br/>

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
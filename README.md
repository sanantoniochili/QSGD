# Learning the N-input Parity Function with a Single Qubit and  Single Measurement Sampling

## This repository comprises Wolfram Mathematica scripts which produce the results presented in the homonymous article pre-print published [here](https://www.preprints.org/manuscript/202501.2126/v1).

The implementation in this repository is separated into four main sections, according to the optimization methods proposed in the article, namely:

- Gradient Descent
- Stochastic Gradient Descent
- Ensemble Stochastic Gradient Descent
- Doubly Stochastic Gradient Descent

Apart from local optimization, the scripts present the implementation of a variational quantum circuit with one qubit which is trained to solve the parity problem. The quantum circuit is called Single-Qubit Classifier (SQC) and is trained with each of the abovementioned methods, evaluated according to their accuracy. 

> [!NOTE]
> The input points are created with additional negligible noise of the order $10^5$ for avoiding zeros.


[Gradient Descent (GD)](Gradient_Descent_analytic_derivatives.nb)
======

The implementation solves the $N$ - input parity classification problem using Gradient Descent for NM random initializations and a fixed number TR of epochs. It provides statistical information on the achieved accuracy of this classification task. The learning rates in the list LG are the optimum values that we have empirically found  for $N$ = 6 .. 10. 

If someone would like to run the program for a different $N$, they should search to find the appropriate learning rate and input this value in the **KK**-th element of the list **LG**. Here you choose the input parameters of the program 

**KK**
: dimension of input 

**NM**
: number of random initializations of the parameters 

**TR**
: number of epocs 

**LG**
: the list of learning rates

**loko**
: list that accumulates all weights across the epocs

**koko**
: list that accumulates the value of loss function across the epocs


### Output

The script outputs statistics on the accuracy and the plot of the loss function (in log scale) vs the epocs. 

[Stochastic Gradient Descent (SGD)](Stochastic_Gradient_Descent_N=10_analytic_derivatives.nb)
===

The implementation solves the $N$ - input parity classification problem using Stochastic Gradient Descent for NM random initializations of $k$ input data in a batch and a fixed number TE of epochs. It provides statistical information on the achieved accuracy of this classification task. The learning rates in the list LG are the optimum values that we have empirically found  for $N$ = 6 .. 10. 

If someone would like to run the program for a different $N$, they should search to find the appropriate learning rate and input this value in the **KK**-th element of the list **LG**. Here you choose the input parameters of the program 

**KK**
: dimension of input 

**NM**
: number of random initializations of the parameters 

**TE**
: number of epocs 

**Z**
: the number of $k$ points in each batch

**stro**
: learning rate _(depends on Z)_

**LG**
: the list of learning rates

**loko**
: list that accumulates the final weights after optimization

**kloklo**
: list that accumulates the value of loss function across the steps

**Step**
: denotes every update of the weights


### Output

The script outputs statistics on the accuracy and the plot of the loss function (in log scale) vs the steps. 

[Ensemble Stochastic Gradient Descent (ESGD)](Ensemble_Stochastic_Gradient_Descent_N=10_numerical_derivatives.nb)
===

The implementation solves the $N$ - input parity classification problem using Ensemble Stochastic Gradient Descent for NM random initializations of $k$ input data in a batch and a fixed number TE of epochs. It provides statistical information on the achieved accuracy of this classification task. The learning rates in the list LG are the optimum values that we have empirically found  for $N$ = 6 .. 10. 

If someone would like to run the program for a different $N$, they should search to find the appropriate learning rate and input this value in the **KK**-th element of the list **LG**. Here you choose the input parameters of the program 

**KK**
: dimension of input 

**NM**
: number of random initializations of the parameters 

**TE**
: number of epocs 

**Z**
: the number of $k$ points in each batch

**stro**
: learning rate _(depends on Z)_

**Fg**
: the list of learning rates

**loko**
: list that accumulates the final weights after optimization

**kloklo**
: list that accumulates the value of loss function across the steps

**Step**
: denotes every update of the weights


### Output

The script outputs statistics on the accuracy and the plot of the loss function (in log scale) vs the steps. 

[Doubly Stochastic Gradient Descent (DSGD)](Ensemble_Stochastic_Gradient_Descent_N=10_numerical_derivatives.nb)
===

The implementation solves the $N$ - input parity classification problem using Ensemble Stochastic Gradient Descent for NM random initializations of $k$ input data in a batch and a fixed number TE of epochs. It provides statistical information on the achieved accuracy of this classification task. The learning rates in the list LG are the optimum values that we have empirically found  for $N$ = 6 .. 10. 

If someone would like to run the program for a different $N$, they should search to find the appropriate learning rate and input this value in the **KK**-th element of the list **LG**. Here you choose the input parameters of the program 

**KK**
: dimension of input 

**NM**
: number of random initializations of the parameters 

**TE**
: number of epocs 

**Z**
: the number of $k$ points in each batch

**stro**
: learning rate _(depends on Z)_

**Fg**
: the list of learning rates

**loko**
: list that accumulates the final weights after optimization

**kloklo**
: list that accumulates the value of loss function across the steps

**Step**
: denotes every update of the weights


### Output

The script outputs statistics on the accuracy and the plot of the loss function (in log scale) vs the steps. Τhe first plot depicts the stochastic loss ( negative log likelihood ), The second depicts an objective loss whose evaluation does not depend on single measurements, but on mean values.
# Augmentation_Package

This packages utilizes two augmentation methods namely.
They were taken from this paper: ``https://arxiv.org/abs/1910.04176``

1. Noise injection (aka radiation therapy): this simply upsamples a given list of embeddings with random noise.
2. Delta_S: Which takes in a given array and extrapolates data given a target label.

#### How To Install?
``!pip install SpaceAugmentation``

#### How do i use them?



First you need to import the library and instantiate it

````python

from aug import Augmentation

ag = Augmentation.Augmentation()

````


### Noise Injection:

```python 
l1, l2 = ag.add_noise(list_of_embeddings, list_of_labels)

```
l1 will be a new list with doubles the size including original embeddings + new embeddings
l2 will be new list of labels

##### Chnage the level of noise you want to inject

```python 
l1, l2 = ag.add_noise(list_of_embeddings, list_of_labels, noise_low= 0.0, nose_high= 0.1)

```

### Delta_S:
This stems from formula

``X_hat =( Xi − Xj ) + Xk``

``Xi is random sample 1`` ``Xj is random sample 2`` ``Xk is random sample 3``   

Sample a pair of sentences ``(Xi, Xj)`` from the ``target`` category.

DELTAS applies deltas from the same target category to another sample ``Xk``

```python 
 l1, l2 = ag.delta_S(list_of_embeddings, list_of_labels, target=0)
```
### NEW !
This lambda with delta_s fusion is a novel technique that has not been tested yet or introduced yet.

if lambda_ is used then we use the lambda_ value times the delta

``X_hat =( Xi − Xj ) * λ + Xk``

```python 
 l1, l2 = ag.delta_S(list_of_embeddings, list_of_labels, target=0, lambda_= 0.3)
```




More Features will be added soon. Enjoy!

# Métodos cuantitativos y simulación
### EJERCICIOS DE PROGRAMACIÓN
Utilizando SCILAB (o alguna herramienta similar), realiza un programa (script) que:

#### 1. Entradas:
Reciba un arreglo de observaciones. Este arreglo es de tamaño N y del tipo entero.


#### 2. Cálculos:
i. Determina la probabilidad de las distintas observaciones.
ii. Determina el Momento estadístico 1
iii. Determina el Momento estadístico 2
iv. Determina la Varianza
v. Determina el Momento estadístico 3
vi. Determina el Momento estadístico 4

#### 3. Salidas:
i. La lista de observaciones con sus probabilidades
Se debe desplegar en consola:
ii. Los valores de cada momento con etiquetas. Por ejemplo:

Los resultados de ingresar los siguientes datos en tu programa:

### Sample input

``` 1,1,2,1,3,4,2,1,3,2 ```

### Sample output

```
1,1,2,1,3,4,2,1,3,2
Possible 'K' values:
1
2
3
4

Probabilities:
1 - 0.4
2 - 0.3
3 - 0.2
4 - 0.1

M1 (Averge):
2.0

M2: (Dispersion)
5.0

VAR:
1.0

M3: (Asymmetry)
14.6

M4: (Curtosis)
47.0

```


### Sample input

``` 4,2,2,2,1,2,1,2,4,3,3,3,1,3,3,4,3,3,1,4,5,5,2,1,5,1,4,2,5,3,2,5,3,1,5,3,2,3,2,4,
3,3,2,3,1,3,1,3,5,2,1,1,5,5,5,2,5,2,1,4,5,3,3,1,1,3,2,1,4,1,4,3,3,3,5,4,1,5,4,1,2,2, 4,1,3,1,2,3,1,3,4,2,3,5,4,1,3,1,3,4 ```

### Sample output

```
Possible 'K' values:
1
2
3
4
5

Probabilities:
1 - 0.23
2 - 0.19
3 - 0.28
4 - 0.15
5 - 0.15

M1 (Averge):
2.8

M2: (Dispersion)
9.66

VAR:
1.82

M3: (Asymmetry)
37.66

M4: (Curtosis)
158.1

```

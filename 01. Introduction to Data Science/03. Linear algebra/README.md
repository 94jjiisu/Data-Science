# 1. Vectors and Matrices

## Regression

<img src='https://wikimedia.org/api/rest_v1/media/math/render/svg/704b31aa61dfc93d672f15bf02aa6d168be49643'>

<br>

<img src= "https://wikimedia.org/api/rest_v1/media/math/render/svg/917759911692e98ba477c3d669356525a84aace6" width="400">


## Dimensionality Reduction: PCA, SVD
사이즈가 큰 데이터셋을 사이즈가 작은 부분으로 나누는 작업

## Scalar, Vector

- 스칼라와 벡터는 선형 대수를 구성하는 기본 단위
- 스칼라는 단순히 변수로 저장되어 있는 숫자이며, 벡터 혹은 매트릭스에 곱해지는 경우 해당 값에 곱한 값으로 결정됨
- 벡터는 파이썬에서 주로 list 로 사용되며, 데이터프레임의 행/열로서 사용되기도 함
- 매트릭스는 벡터의 모음으로 간주될 수도 있음


### Scalar

단일 숫자이며, 변수에 저장 할때는 일반적으로 소문자를 이용하여 표기

실수와 정수 모두 가능

### Vector
- n 차원의 벡터는 컴포넌트라 불리는 n개의 원소를 가지는 순서를 갖는 모음 (컴포넌트는 스칼라로 간주되지 않음)
- 벡터는 일반적으로 위의 회살표 (→) 를 갖는 소문자의 형태로 표현됨

예시: $\vec{v}$ 

$$
\begin{align}
   \vec{a} = 
   \begin{bmatrix}
           8\\
           9
    \end{bmatrix}
    \qquad
    \vec{b} =
    \begin{bmatrix}
          -4\\
           7\\
           1
    \end{bmatrix}
    \qquad
    \vec{c} =
    \begin{bmatrix}
           5.5332
    \end{bmatrix}
    \qquad
    \vec{d} =
    \begin{bmatrix}
           Pl\\
           x\\
           y\\
           \frac{2}{3}
    \end{bmatrix}
\end{align}
$$

위의 벡터들은 각각 2, 3, 1, 4차원을 가지고 있음

벡터의 길이(length)는 벡터의 차원수와 동일

### 벡터의 크기

벡터의 크기는 모든 원소의 제곱을 더한 후 루트를 씌운 값

벡터 크기의 특징

> $||x|| \geq 0$ 
>
> $||x|| = 0$ (모든 원소가 0)
>
> 삼각 부등식: $|| x + y ||\leq ||x|| + ||y||$


### 벡터의 내적 ( Dot Product )

두 벡터 $\vec{a}$ 와 $\vec{b}$ 의 내적은, 각 구성요소를 곱한 뒤 합한 값과 같음 

> v = [1, 2, 3, 4]
>
> x = [5, 6, 7, 8]
>
> v $\cdot$ x = 1 * 5 + 2 * 6 + 3 * 7 + 4 * 8 
> 
> = 70 

- 내적은 교환법칙이 적용됨: $ a \cdot b = b \cdot a$
- 내적은 분배법칙이 적용됨: $a \cdot (b + c) = a \cdot b + a \cdot c$
- 벡터의 내적을 위해서는 두 벡터의 길이가 반드시 동일해야 함 

### Matrix transpose (전치행렬)
매트릭스의 전치는, 행과 열을 바꾸는 것을 의미

대각선 부분의 구성요소를 고정시키고 이를 기준으로 나머지 구성요소들을 **뒤집는다**

$B^T$


### 정사각 매트릭스(square matrix)

- 정사각 매트릭스는, 정방 매트릭스 라고도 불리며, 보통 선형대수 강의에서 처음 몇 주간 배우게 되는 아주 기초적인 매트릭스임

- 이름에서 내포 하고 있듯, 이들은 행과 열의 수가 동일한 매트릭스임

$$\begin{align}
A =
\begin{bmatrix}
  a_{1,1}
\end{bmatrix}
\qquad
B =
\begin{bmatrix}
b_{1,1} & b_{1,2} \\
b_{2,1} & b_{2,2}
\end{bmatrix}
\qquad
C =
\begin{bmatrix}
c_{1,1} & c_{1,2} & c_{1,3} \\
c_{2,1} & c_{2,2} & c_{2,3} \\
c_{3,1} & c_{3,2} & c_{3,3} 
\end{bmatrix}
\end{align}
$$

### 정사각 매트릭스의 특별한 케이스

**Diagonal (대각):** 대각선 부분에만 값이 있고, 나머지는 전부 0

$$
\begin{align}
D =
\begin{bmatrix}
a_{1,1} & 0 & 0 \\
0 & a_{2,2} & 0 \\
0 & 0 & a_{3,3} 
\end{bmatrix}
\end{align}
$$

**Upper Triangular (상삼각):** 대각선 위쪽 부분에만 값이 있고, 나머지는 전부 0

$$
\begin{align}
U =
\begin{bmatrix}
b_{1,1} & b_{1,2} & b_{1,3} \\
0 & b_{2,2} & b_{2,3} \\
0 & 0 & b_{3,3} 
\end{bmatrix}
\end{align}
$$

**Lower Triangular (하삼각):** upper triangular 와 반대로, 대각선 아래에만 값이 있음

$$
\begin{align}
L =
\begin{bmatrix}
c_{1,1} & 0 & 0 \\
c_{2,1} & c_{2,2} & 0 \\
c_{3,1} & c_{3,2} & c_{3,3} 
\end{bmatrix}
\end{align}
$$

**Identity (단위 매트릭스):** 

- Diagonal 매트릭스 중에서, 모든 값이 1인 경우. 임의의 정사각 매트릭스에 단위 행렬을 곱하면, 그 결과값은 원본 정사각 매트릭스로 나오며, 
- 반대로 임의의 매트릭스에 대해서 곱했을때 단위 매트릭스가 나오게 하는 매트릭스를 역행렬 (Inverse)라고 부름

$AI == A$, $AA^{-1} = I$

$$
\begin{align}
I_1 =
\begin{bmatrix}
  1
\end{bmatrix}
\qquad
I_2 =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\qquad
I_3 =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 
\end{bmatrix}
\end{align}
$$

**Symmetric (대칭):** 대각선을 기준으로 위 아래의 값이 대칭인 경우

$$
\begin{align}
S =
\begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 5 \\
3 & 5 & 6 
\end{bmatrix}
\end{align}
$$

### Determinant

행렬식은 모든 정사각 매트릭스가 갖는 속성으로, $det(A)$ 혹은 $|A|$로 표기됨

2x2 매트릭스를 기준으로, 행렬식은 다음과 같이 (**AD-BC**) 계산 할 수 있음:

$$
\begin{align}
\qquad
\begin{bmatrix}
8 & 12 \\
9 & 16
\end{bmatrix}
\end{align}
$$

> 8 * 16 - 12 * 9 = 20
> 
> |x| = det(x) = 20

더 큰 차원의 매트릭스 행렬식은, 재귀적으로 (recursively) 부분을 이루는 행렬식을 구하는 것으로 계산 할 수 있음

ex)

<center><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/14f2f2a449d6d152ee71261e47551aa0a31c801e" width=500></center>


### Inverse

 - 역행렬을 계산하는 방법은 여러가지가 있으며, 행렬의 *역수* 와 같이 표현 할 수 있음
 - 즉 행렬과 그 역행렬의 값은 항상 1 (단위 매트릭스) 입니다. 2x2 매트릭스를 기준으로, 역행렬을 계산하는 방식중 하나는 아래와 같음:
 
$$
 \begin{align}
A = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\qquad
A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}
d & -b\\
-c & a
\end{bmatrix}
\end{align}
$$

### 매트릭스에 역행렬을 곱하면

앞서 말했듯, 매트릭스에 그 역행렬을 곱하면, 단위 매트릭스가 됨

이것이 중요한 이유는 매트릭스의 **곱**은 있지만 **나눗셈**은 선형대수에 존재하지 않기 때문에 

대신 그 행렬의 역행렬을 **곱**하기 때문

$$
\begin{align}
A^{-1}A = I 
\end{align}
$$

### 행렬식이 0인 경우
 
- 행렬식이 0인 정사각 매트릭스는 "특이" (singular) 매트릭스라고 불리기도 함
- 이들은 2개의 행 혹은 열이 선형의 관계를 (M[,i]= M[,j] * N) 이루고 있을때 발생함

- 이를 표현하는 다른 방법은, **매트릭스의 행과 열이 선형의 의존 관계가 있는 경우 매트릭스의 행렬식은 0이다.** 라고 표현 할 수 있음

$$
\begin{align}
S =
\begin{bmatrix}
10 & 33 & 2 \\
25 & 66 & 5 \\
30 & 99 & 6 
\end{bmatrix}
\end{align}
$$


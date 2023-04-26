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

---

# 2. Linear algebra

## Variance

분산은 데이터가 얼마나 퍼져있는지를 측정하는 방법

각 값들의 평균으로부터 차이의 제곱 평균

$$
\begin{align}
v = \frac{\sum{(X_{i} - \overline{X})^{2}} }{N}
\end{align}
$$

* 모집단의 분산 $\sigma^2$ 는 모집단의 파라미터 이며
* 샘플의 분산 $s^2$ 는 샘플의 통계량(estimated attribute) 임 
* 샘플 분산 $s^2$ 는 모집단의 분산 $\sigma^2$ 의 추정치
* 샘플의 분산을 계산 할때는 N-1 로 나누어야 함

## 표준편차

분산을 구할 때 제곱 값들을 더했기 때문에 평균에 비해 스케일이 커지는 문제가 있음

이를 해결하기 위해 루트를 씌워 스케일을 낮춤

## Covariance

$$
\begin{align}
Cov(X, Y) = E[(X - E[X])(Y - E[Y])]
\end{align}
$$

* 공분산이란, 1개의 변수 값이 변화할 때 다른 변수가 어떠한 연관성을 나타내며 변하는지를 측정하는 것

## Correlation coefficient


* 공분산의 스케일 문제를 조정한 것이 상관계수
* 공분산을 두 변수의 표준편차로 각각 나눠준 것

$$   
\begin{align}
cor(X,Y) = r = \frac{cov(X,Y)}{\sigma_{X}\sigma_{Y}} 
\end{align}
$$


## Pearson correlation coefficient
* numeric data


## Spearman correlation coefficient
* categorical data
* rank
* non-parametric data

## Orthogonality (직교)

* 서로 수직, 직교하는 벡터는 서로 상관 관계가 전혀 없음
* 내적값은 0
  

## Unit vectors (단위 벡터)
  * 단위 길이(1) 를 갖는 모든 벡터

모든 벡터는 단위 벡터의 선형 조합으로 표기됨

## Span
* 주어진 두 벡터의(합이나 차와 같은) 조합으로 만들 수 있는 모든 가능한 벡터의 집합

## Linearly Dependent Vector (선형 관계의 벡터)
* 두 벡터가 같은 선상에 있는 경우, 이 벡터들은 선형 관계에 있다고 표현
* 이 두 벡터들은 조합을 통해서 선 외부의 새로운 벡터를 생성할 수 없음

## Linearly Independent Vector (선형 관계가 없는 벡터)
* 같은 선상에 있지 않은 벡터들은 선형적으로 독립되어 있다고 표현
* 주어진 공간의 모든 벡터를 조합을 통해 만들어 낼 수 있음 ($\mathbb{R}$)


## Basis (기저 벡터)
* 벡터 공간 $V$ 의 basis는, $V$ 라는 공간을 채울 수 있는 선형 관계에 있지 않은 벡터들의 모음 (span 의 역개념)

## Orthogonal Basis
* Basis 에 추가로 직교 조건이 붙는, 주어진 공간을 채울 수 있는 서로 수직인 벡터들

## Orthonormal Basis
* Orthogonal Basis에 추가로 Normalized 조건이 붙은 것으로, 길이가 서로 1인 벡터들

## Gram-Schmidt 프로세스
* 주어진 벡터들을 Orthonormal 하게 수정하는 과정

## Rank
* 매트릭스의 rank란, 매트릭스의 열을 이루고 있는 벡터들로 만들 수 있는 span (공간)의 차원
* 매트릭스의 차원과는 다를 수 있으며, 그 이유는 행과 열을 이루고 있는 벡터들 가운데 서로 선형 관계가 있을 수도 있기 때문
* Rank를 확인하는 방법은 여러가지가 있음


## Gaussian Elimination
* 주어진 매트릭스를 'Row-Echelon form' 으로 바꾸는 계산 과정
* 'Row-Echelon form' 이란 각 행에 대해 왼쪽에 1, 그 이후 부분은 0으로 이뤄진 형태

## Projection
$$
\begin{align}proj_{L}(\vec{w})\end{align}
$$

## Linear Projection을 공부하는 이유
* feature 수를 줄여 data를 저장하기 위한 메모리 이득
* 정보의 손실은 단점

---

# 3. Dimentionality Reduction

## Vector transformations
* 선형 변환은 임의의 두 벡터를 더하거나 혹은 스칼라 값을 곱하는 것을 의미

* Transformation
  * matrix를 곱하는 것을 통해 벡터(데이터)를 다른 위치로 옮긴다는 의미


## Eigenvector (고유벡터)
* transformation에 영향을 받지 않는 회전축(벡터)을 공간의 고유벡터 라고 부름

## Eigenvalue (고유값)


* $\lambda$ 로 표현

$$
\begin{align}
T(v) = \lambda v
\end{align}
$$

* 고유벡터는 주어진 transformation에 대해서 크기만 변하고 방향은 변하지 않음
* 이 때 변화하는 크기는 스칼라 값이 됨
* 이 스칼라 값을 고유값이라 부름
* 고유벡터와 고유값은 항상 쌍을 이루고 있음

$T \cdot v = v' = \lambda \cdot v$ 

$$
\begin{align}
\begin{bmatrix} a & b \\ c & d \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} ax+by \\ cx+dy \end{bmatrix} = \lambda \begin{bmatrix} x \\ y \end{bmatrix}
\end{align}
$$

<br>

### 고유값이 쓰이는 이유

## The Curse of Dimentionality (차원의 저주)

### 피쳐의 수가 많은 데이터셋을 모델링하거나 분석할 때 생기는 여러 문제점들

* 사람의 뇌는 3차원 이상의 정보를 공간적으로 다루기 어려움
* 여러 차원의 데이터셋을 다루는 데 이슈가 됨
* 데이터셋에서 모든 feature가 동일하게 중요하지 않음
* 효율과 비효율의 문제
* Overfitting

**일반적으로 feature의 수를 $P$, sample의 수를 $N$ 이라 할 때**
**$P$ $\geq$ $N$ 인 경우 매우 높은 overfitting 이슈가 생긴다고 할 수 있음**

## Dimension Reduction
* 데이터에서 적절한 처리를 통해 충분한 의미를 유지하면서 더 작은 부분만 선택


## Feature Selection
* 데이터셋에서 덜 중요한 feature를 제거하는 방법
* 선택된 feature 해석이 쉬움
* feature들 간의 연관성을 고려해야 함
* Lasso, Genetic algorithm

## Feature Extraction
* 기존에 있는 feature 혹은 그들을 바탕으로 조합된 feature를 사용하는 것
* feature들 간의 연관성이 고려됨
* feature수를 많이 줄일 수 있음
* feature 해석이 어려움
* PCA

## Principal Component Analysis (PCA)
* 고차원 데이터를 효과적으로 분석하기 위한 기법
* 낮은 차원으로 차원 축소
* 고차원 데이터를 효과적으로 시각화 + clustering
* 원래 고차원 데이터의 정보(분산)를 최대한 유지하는 벡터를 찾고, 해당 벡터에 대해 데이터를 **(Linear) Projection**
* 데이터에 대해 독립적인 축을 찾는데 사용할 수 있음
* 데이터의 분포가 정규성을 띄지 않는 경우 적용이 어려움
  * 이 경우는 커널 PCA 를 사용 가능
* 분류 / 예측 문제에 대해서 데이터의 label을 고려하지 않기 때문에 효과적인 분리가 어려움
  * 이 경우는 PLS 사용 가능

1. 데이터를 준비
2. 각 열에 대해서 평균을 빼고, 표준편차로 나누어서 Normalize를 함
3. Z의 분산-공분산 매트릭스를 계산 ($Z^TZ$)
4. 분산-공분산 매트릭스의 고유벡터와 고유값을 계산
5. 데이터를 고유벡터에 Projection 시킴 (matmul)

---

# 4. Clustering

## Scree Plot

<img src='https://i.imgur.com/zyWQBjA.png' width = 400>
<img src='https://i.imgur.com/f60GoIo.png' width = 400>
<img src='https://www.researchgate.net/profile/Raul_Ramirez-Velarde/publication/275541304/figure/fig1/AS:392017420013568@1470475644164/PCA-Scree-plot-and-cumulative-variance-plots.png' width = 400>

## Machine Learning

### Supervised Learning (지도 학습)
지도 학습은 트레이닝 데이터에 label(답)이 있을 때 사용할 수 있음

* Classification
* Regression

### Unsupervised Learning (비지도 학습)
* Clustering
  * 데이터의 연관된 feature를 바탕으로 유사한 그룹을 생성
* Dimensionality Reduction
  * 높은 차원을 갖는 데이터셋을 사용하여 feature selection / extraction 등을 통해 차원을 줄이는 방법
* Association Rule Learning (연관 규칙 학습)
  * 데이터셋의 feature들의 관계를 발견하는 방법 (feature - feature) 

### Reinforcement Learning (강화 학습)
기계가 좋은 행동에 대해서는 보상, 그렇지 않은 행동에는 페널티라는 피드백을 통해 행동에 대해 학습해 나가는 형태

<br>
<img src='https://jixta.files.wordpress.com/2015/11/machinelearningalgorithms.png?w=816&h=521&zoom=2'>
<br>

## Clustering
비지도 학습의 한 종류

## 목적
Clustering이 대답 가능한 질문은 주어진 데이터들이 **얼마나, 어떻게 유사한지** 임

따라서 주어진 데이터셋을 요약, 정리하는데 있어 매우 효율적인 방법으로 사용되고 있음

그러나 동시에 **정답을 보장하지 않는다**는 이슈가 있어 production의 수준, 혹은 예측을 위한 모델링에 쓰이기보단 EDA를 위한 방법으로 많이 쓰임

## Hierarchical Clustering (계층적 군집화)
* Agglomerative clustering (병합 군집화)
  * 개별 포인트에서 시작 후 점점 크게 합쳐감
* Point Assignment
  * 시작 시에 cluster의 수를 정한 다음, 데이터들을 하나씩 cluster에 배정시킴
* Hard vs Soft clustering
  * Hard Clustering에서 데이터는 하나의 cluster에만 할당됨
  * Soft Clustering에서 데이터는 여러 cluster에 확률을 가지고 할당됨
  * 일반적으로 부르는 clustering은 Hard Clustering임


## Similarity
* Euclidean
* Cosine
* Jaccard
* Edit Distance
* Etc.

## K-means Clustering

Process

**n 차원의 데이터에 대해서**

1. k 개의 랜덤한 데이터를 cluster의 중심점으로 설정
2. 해당 cluster에 근접해 있는 데이터를 cluster로 할당
3. 변경된 cluster에 대해서 중심점을 새로 계산
4. cluster에 유의미한 변화가 없을 때 까지 2-3을 반복

### Centroid(중심점) 계산
K-means는 centroid-based clustering 알고리즘으로도 불림
Centroid란, 주어진 cluster 내부에 있는 모든 점들의 중심부분에 위치한 (가상의)점

## K-means에서 K를 결정하는 방법
* The Eyeball Method
  * 사람의 주관적인 판단을 통해 임의로 지정하는 방법
* Metrics
  * 객관적인 지표를 설정하여 최적화된 k를 선택하는 방법


### Elbow methods
* sum of squared distances 기울기가 급격히 완만해지는 부분을 k로 사용 가능

```python
sum_of_squared_distances = []
K = range(1, 15)
for k in K:
    km = KMeans(n_clusters = k)
    km = km.fit(points)
    sum_of_squared_distances.append(km.inertia_)


plt.plot(K, sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()
```

k-means 에서 centroid를 어떻게 선택하느냐에 따라 clustering결과가 안좋거나 끝없이 반복해야 하는 경우도 있음


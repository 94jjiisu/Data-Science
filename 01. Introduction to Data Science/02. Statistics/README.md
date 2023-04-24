# 1. Hypothesis test

## 통계량

### 기술통계량
- count, mean, variance, std dev, min, 1Q, median, 3Q, max, kurtosis, skewness 등의 데이터를 설명하는 값

### 추론통계량
- population, parameter, estimator, std dev, std error
- 표준오차로 통계량을 추정

### Sampling

* **simple random sampling**

모집단에서 샘플링을 무작위로 수행

* **systematic sampling**

모집단에서 샘플링을 할 때 규칙을 가지고 추출

* **stratified random sampling**

모집단을 미리 여러 그룹으로 나누고 그 그룹별로 무작위 추출

* **cluster sampling**

모집단을 미리 여러 그룹으로 나누고 이후 특정 그룹을 무작위로 선택

### 가설 검정

**주어진 상황에 대해서 하고자 하는 주장이 맞는지 아닌지를 판정하는 과정**
**모집단의 실제 값에 대한 샘플으 통계치를 사용해서 통계적으로 유의한지 아닌지 여부를 판정함**

**표본 평균의 표준 오차**
- 표본의 수가 더욱 많아질수록, 추측은 더 정확해지고 높은 신뢰도를 바탕으로 모집단에 대해 예측할 수 있도록 함

## Student T-test

- **$\alpha$(유의 수준): 제 1종 오류의 위험성을 부담하는 최대 확률, 보통 0.05 사용**
- **신뢰수준: 1 - 유의수준, 신뢰구간을 100번 구했을 때, 해당 신뢰구간에 모평균이 95번 포함됨**

<br>

- **p-value(유의 확률; significance probability)**

- p-value 는, 주어진 가설에 대해서 '얼마나 근거가 있는지'에 대한 값을 0과 1사이의 값으로 scale한 지표

- 귀무가설이 맞다고 가정할 때 얻은 결과보다 극단적인 결과가 실제로 관측될 확률

- 귀무가설이 맞다는 전제 하에, 표본에서 실제로 관측된 통계치와 '같거나 더 극단적인' 통계치가 관측될 확률

- 귀무가설을 가정하였을 때 표본 이상으로 극단적인 결과를 얻을 확률

**p-value가 낮다는 것은, 귀무가설이 틀렸을 확률이 높다**

**p-value < 0.05  ->  귀무가설 기각, 대립가설 채택:**

- 어떤 사건이 우연히 발생할 확률이 0.05보다 작을 가능성은 거의 없으며 만약 발생하더라도
- 그것은 우연히 일어난 것(귀무가설)이 아니라 유의(대립가설)했기 때문에 일어났다고 해석함

### One sample t-test

```python
stats.ttest_1samp(x, n)
```

**1개의 sample 값들의 평균이 특정한 값과 동일한지 비교**

- 모집단에 대한 정보와 표본의 데이터를 비교
- 정규화 과정을 거쳐 주어진 데이터가 평균은 0, 표준편차가 1인 데이터로 스케일링 됨
- 귀무가설은 '평균은 x 이다'

**p-value가 기준치에 못 미칠 때**

- 실험을 다시 한다
- 데이터를 다시 뽑는다
- 샘플링을 다시 한다
- 기존의 경험/인사이트를 바탕으로 가설에 대한 결론을 내린다

### Two sample t-test

```python
stats.ttest_ind(x1, x2)
```

**2개의 sample 값들의 평균이 서로 동일한지 비교**

- 귀무가설은 '두 확률은 같다'

## ANOVA

**Compare mean for multi-samples**

**여러 그룹간의 평균의 차이가 통계적으로 유의한지 판단하는 방법**

### **분산분석의 전제 조건**

- **정규성: shapiro-wilk test**

각 변수는 정규 분포를 따라야 한다

```python
stats.shapiro(data)

stats.skew(data, bias=Flase)
```

shapiro-wilk test는 p-value가 나오기 상당히 까다로운 검정

검정 결과는 대립가설을 기각하고, 귀무가설을 채택해야 함

- 귀무가설: 데이터가 정규분포를 따른다
- 대립가설: 데이터가 정규분포를 따르지 않는다

실무적인 방법은 변수의 왜도의 절대값이 2를 넘지 않으면 보통 실험을 실시함

또는 변수의 값을 로그 변환하여 정규분포의 모양으로 맞춰주고 실행

- **등분산성(barlett test, levene test)**

각 변수의 분산은 동일한 수준의 분산을 가져야 한다

검정 결과는 대립가설을 기각하고, 귀무가설을 채택해야 함

- 각 변수의 분산은 동일한 수준의 분산을 가져야 한다
- 귀무가설: 변수 간 분산에 유의미한 차이가 없다
- 대립가설: 변수 간 분산에 유의미한 차이가 있다

```python
from scipy.stats import bartlett, levene
stats.bartlett( Data A
         , Data B
         , Data C
        )
 
 
stats.levene(Data A         
         , Data B
         , Data C            
        )
```

- **독립성**
독립성 검정은 숫자보다는 실험 설계에서 결정되어야 할 변수


### one-way ANOVA test

**종속변인 1개, 독립변인의 집단도 1개**

**한가지 변수의 변화가 결과 변수에 미치는 영향을 확인**

- scipy

```python
f_val, p_val = stats.f_oneway(x1, x2, x3)
print(f_val, p_val)
```

- statsmodel 라이브러리가 좀 더 많고 규격화된 정보를 제공함
- statsmodel

```python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df = pd.DataFrame(data, columns=['value', 'treatment'])   

model = ols('value ~ C(treatment)', df).fit()
print(anova_lm(model))
```

### two-way ANOVA test

**독립변인의 수가 두 개 이상일 때 집단 간 차이가 유의한지를 검정**

**교호작용, 한 변수의 변화가 결과에 미치는 영향이 다른 변수의 수준에 따라 달라지는지를 확인하기 위해 사용**

**교호작용(Interaction): 한 요인의 효과가 다른 요인의 수준에 의존하는 경우, 교호작용도가 평행선으로 나타나면 교호작용이 없다는 것을 나타냄**

```python
df = pd.DataFrame(data, columns=['head_size', 'fetus', 'observer'])

formula = 'head_size ~ C(fetus) + C(observer) + C(fetus):C(observer)'
lm = ols(formula, df).fit()
print(anova_lm(lm))
```

### 사후분석
- 집단 간 평균이 다른건 알겠는데, 누가 더 높은지 모르는 상황
- 누가 진짜 제일 높은지 확인하고 싶고, 진짜로 의도한 그룹이 더 높은지 낮은지 최종 확인

**Turkey HSD**

**BONFERRONI**

- **one-way 사후분석**

```python
model = ols('posterior ~ C(group)', temp_df).fit()
anova_lm(model)

## Turkey HSD 방식
comp = mc.MultiComparison(temp_df['posterior'], temp_df['group'])
result = comp.tukeyhsd()
result.summary()
 
 
## BONFERRONI 방식
comp = mc.MultiComparison(temp_df['posterior'], temp_df['group'])
tbl, a1, a2 = comp.allpairtest(stats.ttest_ind, method= "bonf")
tbl
```

#### Turkey HSD 해석
p-value가 유의하게 나온 조합에서 두 변인의 평균의 차이가 있음

**그래프로 시각화 하는 방법**

```python
result.plot_simultaneous(ylabel= 'Group', xlabel= 'Score Difference')
```

---

간단한 정규성 확인 방법(scipy)

```python
from scipy.stats import normaltest
normaltest(data)
```
---
<br>

# 2. Chi-squared Tests


## 비모수적 방법(Non-Parametric Methods)

모집단이 특정 확률 분포를 따른다는 전제를 하지 않는 방식

모수 추정이 필요하지 않기 때문에 비모수라고 부름

* Categorical Data를 위한 모델링
* 혹은 극단적 outliers가 있는 경우, 매우 유효한 방식
* distribution free method 라고 부르기도 함

<br>

* Chi_square  

* Spearman correlation  

* Run test  

* Kolmogorov Smirnov

* Mann-Whitney U  

* Wilcoxon  

* Kruskal-Wallis  


...etc

### Kruskal-Wallis Test (비모수적 평균 비교법)

```python
# Kruskal-Wallis H-test - 2개 이상 그룹의 중위 랭크를 통한 차이 비교 ( extended X2 )
# 샘플 수가 > 5 일때 좋음 
from scipy.stats import kruskal

x1 = [1, 3, 4, 8, 9]
y1 = [1, 4, 6, 7, 7]
kruskal(x1, y1) # 약간은 다르지만, "유의한" 차이는 아님
```
KruskalResult(statistic=0.01111111111111548, pvalue=0.91605107228188)

```python
x2 = [12, 15, 18]
y2 = [24, 25, 26]
z = [40, 40]  # 3번째 그룹은 사이즈가 다름
kruskal(x2, y2, z)
```
KruskalResult(statistic=6.325301204819277, pvalue=0.042313436212501186)

---

## $\chi^2$ Tests

### One sample $\chi^2$ test (적합도 검정)

주어진 데이터가 특정 예상되는 분포와 동일한 분포를 나타내는지 검정

**귀무가설: 분포는 같다**

**대립가설: 분포는 다르다**

Exp = sum(obs) / count

$\chi^{2}=\sum \dfrac{\left( observed_{i}-expected_{i}\right) ^{2}}{\left( expected_{i}\right) }$

### chi2 statistics to p-value

**stats.chi2.cdf**

```python
from scipy import stats

x2 = 0.00139
1 - stats.chi2.cdf(x2, df = ((2-1)*(2-1)) ) # pvalue : 0.97, 연관이 있다.
```

```python
from scipy.stats import chisquare  

s_obs = np.array([[18, 22, 20, 15, 23, 22]]) # Similar
print('--- Similar ---')
chisquare(s_obs, axis=None) # One sample chi-square
```
> --- Similar ---
Power_divergenceResult(statistic=2.3000000000000003, pvalue=0.8062668698851285)

```python
ns_obs = np.array([[5, 23, 26, 19, 24, 23]])

print('--- not Similar ---')
chisquare(ns_obs, axis=None)
```

> --- not Similar ---
Power_divergenceResult(statistic=14.8, pvalue=0.011251979028327346)

### Two sample $\chi^2$ test (독립성 검정)

**귀무가설: 변수들은 서로 독립이다**

**대립가설: 변수들은 서로 독립이 아니다**

```python
print(exp) # 데이터 표

from scipy.stats import chi2_contingency

print('---')
print(chi2_contingency(obs)) # correction 파라미터가 True로 설정 :  Yates’ correction 시행함 : pvalue는 약간 다름

print('---')
print(chi2_contingency(obs, correction = False)) # 위에서 계산한 것과 동일
```
correlation 파라미터가 True이고 자유도가 1이라면 관측치는 0.5씩 기대값으로 옮기는 Yates' correction이 적용되어 검정통계량이 낮게 나옴

### chi2_contingency 결과 해석

1: $\chi^2$ statistic 

2: p-value 

3: degree of freedom 

4: expected value for Observed

### 자유도 (Degrees of Freedom)

해당 파라미터를 결정짓기 위한 독립적으로 정해질 수 있는 값의 수

**1-sample (적합도 검정), DF = # categories-1**

**2-sample (독립성 검정), DF = (#행 - 1)*(#열 - 1)**

**DF: (2-1)*(2-1) = 1**

---
<br>

# 3. Confidential Intervals

## F-statistic

여러 그룹들이 하나의 분포에서부터 왔다 라는 가정의 지표

**F = 그룹간 분산 / 그룹 내 분산**

```python
from scipy.stats import f_oneway

f_oneway(g1, g2, g3) # pvalue = 0.11 
```
> F_onewayResult(statistic=2.6009238802972483, pvalue=0.11524892355706169)

---

### Law of large numbers (큰 수의 법칙)

sample 데이터의 수가 커질 수록, sample의 통계치는 점점 모집단의 모수와 같아진다

```python
dat = []

for i in np.arange(start = 5, stop = 995, step = 5) :
  s = np.random.choice(population, i)
  dat.append(s.var())
dat

(pd
 .DataFrame(dat)
 .plot
 .line(color = '#4000c7')
 .axhline(y = 100, color = '#00da75')
 );
 ```

 - **method chaining**

### Central Limit Theorem, CLT, (중심극한정리)

sample 데이터의 수가 많아질수록, sample의 평균은 정규분포에 근사한 형태로 나타난다

### Point estimate VS Interval estimate (점추정, 구간추정)

예측 하는 '구간' 이 넓어질 수록 맞을 확률(신뢰도)은 증가

### 신뢰도
> 신뢰도가 95% 라는 의미는 표본을 100번 뽑았을 때 95번은 신뢰구간 내에 모집단의 평균이 포함된다는 뜻

```python
from scipy.stats import t

# 표본의 크기
n = len(sample)
# 자유도
dof = n-1
# 평균의 평균
mean = np.mean(sample)
# 표본의 표준편차
sample_std = np.std(sample, ddof = 1)
# 표준 오차
std_err = sample_std / n ** 0.5 # sample_std / sqrt(n)

CI = t.interval(.95, dof, loc = mean, scale = std_err) # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html
print("95% 신뢰구간: ", CI)
```

---

<br>

# 4. Bayesian

## The Law of Conditional Probability (조건부확률)

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

## Bayes Theorem

$$P(A|B) = {{P(A \cap B)} \over {P(B)}} $$

$$P(B|A) = {{P(B \cap A)} \over {P(A)}} $$
Since 

$$P(A \cap B) = P(B \cap A),$$

Therefore

$$P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

$p(A|B)$ -> 사후 확률 (B라는 정보가 업데이트 된 이후의 사(이벤트)후 확률)

$p(A)$ -> 사전 확률 B라는 정보가 업데이트 되기 전의 사전확률

$p(B|A)$ -> data 

여기서 조건이 붙지 않은 확률 은 **사전확률("Prior")**, 조건이 붙은 부분은 **사후확률("Updated")**로 다시 표현 할 수 있음


### Repeated testing

ex) 암 진단

- TPR : **T**rue **P**ositive **R**ate (= 민감도, true accept rate)
1인 케이스에 대해 1로 잘 예측한 비율.(암환자를 암이라고 진단 함)

- FPR : **F**alse **P**ositive **R**ate (= 1-특이도, false accept rate)
0인 케이스에 대해 1로 잘못 예측한 비율.(암환자가 아닌데 암이라고 진단 함)

<br>

![Bayes Theorem Drug Test Example](https://wikimedia.org/api/rest_v1/media/math/render/svg/95c6524a3736c43e4bae139713f3df2392e6eda9)

- 1차 계산
```python
# 베이지안 계산을 위해서는 4개의 변수가 필요합니다.

p_pos_used = 0.99 # True positive rate (TPR, Sensitivity)
p_used = 0.005 # prior probability
p_pos_not_used = 0.01 # False positive rate (FPR)
p_not_used = 1 - p_used # 1 - p_used  

numerator = p_pos_used * p_used 

denominator = (p_pos_used * p_used) + (p_pos_not_used * p_not_used)

posterior_probability = numerator / denominator

posterior_probability
```
> 0.33221476510067116


- 2차 계산

```python
p_pos_used = 0.99 # TPR
p_used = 0.332 # prior probability
p_pos_not_used = 0.01 # FPR
p_not_used = 1 - p_used # 1 - p_used  

numerator = p_pos_used * p_used 

denominator = (p_pos_used * p_used) + (p_pos_not_used * p_not_used)

posterior_probability = numerator / denominator

posterior_probability
```
> 0.980081106870229


- 3차 계산
```python
p_pos_used = 0.99 # TPR 
p_used = 0.98008 # prior probability
p_pos_not_used = 0.01 # FPR
p_not_used = 1 - p_used # 1 - p_used  

numerator = p_pos_used * p_used 

denominator = (p_pos_used * p_used) + (p_pos_not_used * p_not_used)

posterior_probability = numerator / denominator

posterior_probability #99.979%

# p_value = 1 - posterior_probability
```
> 0.9997947404084419


### Bayesian CIL
```python
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bayes_mvs.html#scipy.stats.bayes_mvs

mean_CI, _, _ = stats.bayes_mvs(coinflips, alpha = .95) # mean , variance, std
```

### Bayesian Optimize

```python
!pip3 install bayesian-optimization

def black_box_func(x, y):
  return -x ** 2 - (y-1) ** 2 + 1

pbounds = {'x' : (2, 4), 'y': (-3, 3)}

from bayes_opt import BayesianOptimization

optimizer = BayesianOptimization(f = black_box_func, 
                                 pbounds = pbounds, 
                                 random_state = 1)

optimizer.maximize(init_points = 2, n_iter = 10) 

print(optimizer.max)
```

베이지안 최적화는 머신러닝에서 하이퍼파라미터 최적값 탐색에 사용되는 기법임

- Bayesian Optimization 은 어느 입력값(x)를 받는 미지의 목적 함수(f(x))를 상정하여,

- 해당 함숫값(f(x))을 최대로 만드는 최적해를 찾는 것을 목적으로 함

  - 즉, 목적 함수(탐색대상함수)와 하이퍼파라미터 쌍(pair)을 대상으로 Surrogate Model(대체 모델) 을 만들고,
  
  - 순차적으로 하이퍼 파라미터를 업데이트해 가면서 평가를 통해 최적의 하이퍼파라미터 조합을 탐색함
  
  - 이 때의 목점 함수를 black-box function 이라고 함
  
- Bayesian Optimization 에는 두 가지 필수 요소가 존재함

  - 먼저 Surrogate Model 은, 현재까지 조사된 입력값-함숫결과값 점들 (x1, f(x1)),...,(xt, f(xt)) 을 바탕으로, 미지의 목적 함수의 형태에 대한 확률적인 추정을 수행하는 모델을 지칭함

  - 그리고 Acquisition Function 은, 목적 함수에 대한 현재까지의 확률적 추정 결과를 바탕으로, ‘최적 입력값을 찾는 데 있어 가장 유용할 만한’ 다음 입력값 후보를 추천해 주는 함수를 지칭함


![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb33tsP%2FbtraMpvxJG0%2FSn7uQK7k910IQ7cP3ZM9vk%2Fimg.png)

**대략적인 수행 과정**

- 위의 파란색 선은, 우리가 찾으려고 하는 목적함수 f(x) 를 나타내고,
  
- 검정색 점선은, 지금까지 관측한 데이터를 바탕으로 우리가 예측한 estimated function 을 의미
  
- 검정색 점선 주변에 있는 파란 영역은, 목적함수 f(x) 가 존재할만한 confidence bound(function의 variance) 를 의미
  
- 밑에 있는 EI(x) 는, Acquisition function 을 의미하며, 다음 입력값 후보 추천 시 사용
  
    - Acquisition function 값이 컸던 지점을 확인하고, 해당 지점의 hyperparameter 를 다음 입력 값으로 사용
  
- hyperparamter 에 따라 estimated function 을 계속 update 하면, estimation function 과 목적 함수 f(x) 가 흡사해짐
  
- 관측한 지점 중 best point 을 argmax f(x) 로 선택
  

**자세한 수행 과정**

1. 입력값, 목적 함수 및 그 외 설정값들을 정의

   1. 입력값 x : 여러가지 hyperparameter
   
   2. 목적 함수 f(x) : 설정한 입력값을 적용해 학습한, 딥러닝 모델의 성능 결과 수치(e.g. 정확도)
   
   3. 입력값 x 의 탐색 대상 구간 : (a,b)
   
   4. 입력값-함숫결과값 점들의 갯수 : n
   
   5. 조사할 입력값-함숫결과값 점들의 갯수 : N
   

2. 설정한 탐색 대상 구간 (a,b) 내에서 처음 n 개의 입력값들을 랜덤하게 샘플링하여 선택

3. 선택한 n 개의 입력값 x1, x2, ..., xn 을 각각 모델의 hyperparameter 로 설정하여 딥러닝 모델을 학습한 뒤, 학습이 완료된 모델의 성능 결과 수치를 계산
   1. 이들을 각각 함숫결과값 f(x1), f(x2), ..., f(xn) 으로 간주

<br>

4. 입력값-함숫결과값 점들의 모음 (x1, f(x1)), (x2, f(x2)), ..., (xn, f(xn)) 에 대하여 Surrogate Model 로 확률적 추정을 수행

5. 조사된 입력값-함숫결과값 점들이 총 N 개에 도달할 때까지, 아래의 과정을 반복적으로 수행

   1. 기존 입력값-함숫결과값 점들의 모음 (x1, f(x1)),(x2, f(x2)), ..., (xt, f(xt)) 에 대한 Surrogate Model 의 확률적 추정 결과를 바탕으로, 입력값 구간 (a,b) 내에서의 EI 의 값을 계산하고, 그 값이 가장 큰 점을 다음 입력값 후보 x1 로 선정
   2. 다음 입력값 후보 x1 를 hyperparameter 로 설정하여 딥러닝 모델을 학습한 뒤, 학습이 완료된 모델의 성능 결과 수치를 계산하고, 이를 f(x1) 값으로 간주
   3. 새로운 점 (x2, f(x2)) 을 기존 입력값-함숫결과값 점들의 모음에 추가하고, 갱신된 점들의 모음에 대하여 Surrogate Model 로 확률적 추정을 다시 수행
   
<br>

6. 총 N 개의 입력값-함숫결과값 점들에 대하여 확률적으로 추정된 목적 함수 결과물을 바탕으로, 평균 함수 μ(x) 을 최대로 만드는 최적해를 최종 선택. 추후 해당값을 hyperparameter 로 사용하여 딥러닝 모델을 학습하면, 일반화 성능이 극대화된 모델을 얻을 수 있음


https://wooono.tistory.com/102
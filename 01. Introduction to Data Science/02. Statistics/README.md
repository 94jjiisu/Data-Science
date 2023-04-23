# 1. Hypothesis test

## 통계량

### 기술통계량
- count, mean, variance, std dev, min, 1Q, median, 3Q, max, kurtosis, skewness 등의 데이터를 설명하는 값

### 추론통계량
- population, parameter, estimator, std dev, std error
- 표준오차로 통계량을 추정

### Sampling

* **simple random sampling**
- 모집단에서 샘플링을 무작위로 수행

* **systematic sampling**
- 모집단에서 샘플링을 할 때 규칙을 가지고 추출

* **stratified random sampling**
- 모집단을 미리 여러 그룹으로 나누고 그 그룹별로 무작위 추출

* **cluster sampling**
- 모집단을 미리 여러 그룹으로 나누고 이후 특정 그룹을 무작위로 선택

### 가설 검정

**주어진 상황에 대해서 하고자 하는 주장이 맞는지 아닌지를 판정하는 과정**
**모집단의 실제 값에 대한 샘플으 통계치를 사용해서 통계적으로 유의한지 아닌지 여부를 판정함**

**표본 평균의 표준 오차**
- 표본의 수가 더욱 많아질수록, 추측은 더 정확해지고 높은 신뢰도를 바탕으로 모집단에 대해 예측할 수 있도록 함

## Student T-test

- **$alpha$(유의 수준): 제 1종 오류의 위험성을 부담하는 최대 확률, 보통 0.05 사용**
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

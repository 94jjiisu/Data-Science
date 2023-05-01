# 1. Interpretable ML 1

> ML 모델을 해석한다는 것

- 모델의 의사결정에 대한 이유를 제시
- 모델이 주요하게 학습한 규칙 및 피쳐를 찾기

> ML 모델을 해석하는 것이 중요한 이유

1. 모델의 검증 데이터셋에 대한 성능만으로 충분하지 않을 수 있음
   - 데이터는 항상 변하며 전부 알 수 없다
   - 평가지표가 완전하지 않다
2. 모델을 해석하는 것은 모델 성능 개선에 도움이 됨
   - 특성의 선택
3. 모델이 결정을 내린 이유가 요구되는 상황이 존재

**모델을 해석함으로써 우리는 모델의 신뢰도를 높이고 부작용을 줄일 수 있음**

## Feature Importance

- 특성 중요도는 모델의 예측값에 대한 각 특성들의 중요도를 수치로 보여줌

### Feature Importance(Mean decrease impurity, MDI)

- 트리기반 모델에서는 각 스텝에서 특정 피쳐에 의해 노드를 분할하여 노드의 불순도를 감소시킴
- 평균적으로 불순도를 크게 감소시키는 피쳐들은 중요하다고 할 수 있음
- MDI 기반 feature importance는 빠르고 간편하다는 장점이 있음

> Feature Importance의 문제점: High Cardinality
- MDI 기반 feature importance는 high cardinality 특성에 높은 값을 부여하는 문제가 있음
- 매 노드 분할 시 cardinality가 높은 특성이 분할 기준 특성이 될 가능성이 높기 때문

### Drop-Column Importance
- 각 특성을 사용하지 않고(drop) 모델을 학습한 후, 평가 성능을 모든 특성을 사용한 모델의 평가 성능과 비교
- 특성을 제거했을 때 평가 성능이 크게 하락했다면 해당 특성이 매우 중요한 것
- 이론적으로는 좋지만 매 특성을 drop한 후 fit을 다시 해야 하기 때문에 특성 n개 일 시 n+1 번 학습해야 해서 매우 느림

### Permutation Importance
- 모델을 재학습시키지 않고, 기존 모델에서 각 특성에 노이즈를 주어 모델이 해당 특성을 의사결정에 사용하지 못하게 만들었을 때 성능이 얼마나 감소하는지 확인
- 노이즈를 주는 간단한 방법이 그 특성값들을 샘플들 내에서 섞는 것(shuffle, permutation)

> Permutation Importance의 장 단점
- 장점
  - 재학습이 필요 없음
  - 모든 모델에 범용적으로 적용 가능
  - Feature Importance보다 high cardinality 특성에 덜 치우친 결과를 냄

- 단점
  - 강한 상관관계가 있는 특성들이 존재할 때, 잘못된 결과 도출 가능

* permutation은 해당 특성의 전체 분포를 변화시키지 않음
* 특성값들의 순서만 변경

### eli5
- eli5 라이브러리에서 Permutation Importance 사용 가능

**특성 중요도를 파악한 후, 중요도가 낮은 특성은 drop 하는 방식으로 특성 선택을 진행할 수 있음**

- 불필요하게 많은 특성들은 오히려 과적합을 유발하고, 모델의 학습 속도를 저하시킴

## Individual Conditional Expectation(ICE) plot
**pdpbox**

> ICE plot을 사용하면 특정 관측치(데이터포인트)에서의 특정 특성의 변화에 따른 모델의 예측 양상 변화를 확인할 수 있음

- 데이터셋, 분석할 데이터의 index, 변화를 확인할 특성 이름, 바꿔넣어 볼 특성의 범위를 입력하면 해당 범위 내에서 모델의 예측 양상의 변화를 반환하는 함수를 작성

## Partial Dependent Plot

- ICE plot을 사용하면 특정 데이터에 대해 특성의 변화에 따른 모델의 예측 양상 변화를 살펴볼 수 있음
- 하지만 하나의 ICE plot으로 모델이 해당 특성에 대해 전반적으로 어떻게 분석하고 이해하고 있는지 판단할 수 없음
- PDP는 입력 데이터들에 대한 ICE plot의 평균으로 구할 수 있음

**PDP는 특정 특성에 대한 모델의 복잡한 반응 양상을 이해하기 쉽게 시작화해 준다는 장점이 있음**

> PDP 해석 시 유의할 점
- PDP는 각 특성 간의 독립성을 전제로 하기 때문에 강한 상관관계가 있는 특성에 대해서는 결과가 좋지 못할 수 있음
- PDP를 해석할 때는 살펴보고자 하는 특성값의 분포를 주의 깊게 살펴보아야 함
  - 학습하지 못한 데이터에 대해 예측하고자 한다면 이상한 예측값을 내놓을 수 있음


> pdpbox 라이브러리의 pdp_isolate 을 사용하면 하나의 특성에 대한 PDP를 시각화 가능

>2개 특성의 변화에 대한 PDP는 heatmap 형태로 시각화 가능

plotly 라이브러리를 사용해 3D 형태로 시각화도 가능

- 범주형 특성에 대해서도 PDP 작성 가능

## Model-Specific vs Model-Agnostic

- Model-Specific ML 해석법은 사용하는 모델에 종속적
- Model-Agnostic 방법들은 모든 모델에 범용적으로 적용 가능

### Model-Specific
- 선형 모델의 회귀 계수
- 트리 모델의 시각화 분기
- 별도 과정 없이 손쉽게 사용할 수 있지만, 소로 다른 모델이 각기 특성을 어떻게 이해하고 있는지를 비교해 보기 어려움


### Model-Agnostic
- Drop-Column Importance, Permutation Importance, ICE plot, PDP 등
- Model-Agnostic한 해석법을 사용할 경우 머신러닝 개발자는 문제 해결을 위해 제한 없이 다양한 모델을 시도해 볼 수 있고, 서로 비교해볼 수 있음

## Global vs Local
- Global한 방법들은 모델의 평균적인 작동 양상을 설명하며, Local한 방법들은 특정 데이터 조건에서 모델의 반응을 보여줌

### Global Methods
- 모델의 평균적인 예측 양상을 해석할 수 있는 방법들
- Permutation Importance, PDP 등은 각 특성의 변화에 따른 모델 예측의 평균적인 변화를 보여줌
- 이런 방법들을 Global한 모델 해석법이라 함
- Global 방법을 사용하면 큰 틀에서 모델의 작동을 이해하기 쉬운 형태로 해석할 수 있지만, 대부분의 경우에서 Global한 방법들은 특성 간의 독립성을 가정하기 때문에 특성 간 상관관계가 강할 경우 해석이 틀릴 수 있음

### Local Methods
- ICE plot은 데이터셋에서의 특정 관측치에 대한 모델의 예측 양상 변화를 보여줌
- 이런 방법들을 Local한 모델 해석법이라고 함
- Local한 방법을 사용하면 모델의 일반적인 상황에서의 예측을 손쉽게 이해하기는 어렵지만, 특성 간의 상관관계를 파악하거나 모델의 비정상적인 예측 패턴 등을 파악할 수 있음

# 2. ML Problem Framing

## 정보 누수(Data Leakage)

1. 학습 데이터가 예측 시 못 쓰는 피쳐를 반영하는 경우(Column axis)
2. 학습 과정에서 평가 데이터의 정보가 활용되는 경우(Row axis)
   - 학습 / 검증 / 평가 데이터를 미리 나눈 후 scaling 등 전처리를 진행
   - scaling, encoding 과정에 유의
     - fit_transform은 학습 데이터에 대해서만 사용
     - 검증 데이터에 대해서는 transform만 사용
   - pipeline 사용으로 실수 줄이기

## 타겟의 분포가 불균형일 때

1. class_weight
   - 각 클래스의 데이터에 대해 서로 다른 가중치를 부여해 학습
   - 소수 클래스에 더 큰 가중치 부여

2. sampling
   - oversampling
   - undersampling

## 회귀 문제 - 분포 변환
- 타겟의 분포가 비대칭 형태인지 확인
- 선형 회귀 모델은 특성 변수들에 따른 타겟 변수의 분포가 정규분포일때 좋은 성능
- 타겟 변수가 skewed 일 경우 예측에 부정적 영향
- 로그 변환: $log(1 + x)$
- 지수 변환: $exp(x) - 1$

# 3. Classification Problem

## Classification with Extremely Imbalanced Target Distribution

- 타겟 분포가 극단적으로 불균형한 상황
- 데이터의 split 작업은 Oversampling, Undersampling 등의 작업을 적용하기 이전에 진행되어야 함
  - 평가용 데이터는 말 그대로 실제 상황에서 모델의 성능을 측정하기 위한 것
  - 평가용 데이터의 분포에 조작을 가하면 현실 세계의 데이터의 분포와 멀어져 의미가 없어지게 됨

**xgboost 라이브러리에서는 `scale_pos_weight` 파라미터를 ${NumNegSamples}/{NumPosSamples}$ 로 지정하여 두 클래스의 가중치를 균일하게 조정해 줄 수 있음**
  - 타겟 불균형 문제가 매우 심각할 때(일반적으로 > 99%)는 $ \sqrt{{NumNegSamples}/{NumPosSamples}}$로 지정하기도 함
  > scale_pos_weight=(y_val == 0).sum() / (y_val == 1).sum()``
  
**sklearn의 모델에서는 `class_weight`를 `balanced`로 하여 가중치를 균일하게 맞춰줄 수 있음**

## Undersampling
- `imblearn` 라이브러리의 undersampling 기능 사용 가능
- Undersampling은 두 클래스의 비율을 동일하게 맞춰 주는 강력한 방법이지만, 다수 클래스의 데이터에서 많은 정보 손실이 발생한다는 단점이 있음
- **검증 데이터셋에는 Undersampling이 적용되지 않아야 함**
- 불균형 문제가 심각할 때, class_weight 를 사용해도 여전히 결과가 좋지 않을 때가 있음
- 이럴 때 undersampling은 oversampling에 비해 안정적이면서도 강력하게 두 class 의 균형을 맞추는 방법
- 하지만 학습에 사용된 데이터의 수가 크게 감소하기 때문에, 학습 자체가 이루어지지 않거나 예상보다 낮은 성능 결과를 반환할 수 있음

## Oversampling
- `imblearn` 라이브러리의 oversampling 기능 사용 가능
- Oversampling은 소수 클래스의 기존 데이터들과 유사한 합성 데이터를 만들어서 데이터 수를 늘리는 방식
- 마찬가지로 검증 데이터셋에는 oversampling이 적용되지 않아야 함


## Oversampling + Undersampling
- oversampling은 기존 데이터를 기반으로 새로운 데이터를 합성하므로, 생선된 합성 데이터들이 `noisy` 하다는 문제가 있음
- 이를 해결하는 방법 중 새로운 데이터를 oversampling으로 합성한 후, 생성된 데이터들 중 노이즈가 큰 데이터들을 undersampling으로 정리하는 방법이 있음
- imblearn 라이브러리에서 `SMOTEENN`, `SMOTETomek` 등 combination 방법 사용 가능

## Ensemble for Imbalanced Dataset
- 타겟 불균형 문제에 앙상블 기법이 적용될 수도 있음
- Undersampling 과 Bagging 을 함께 적용할 수 있음
  - 여러 번 Undersampling을 수행하여 각 분류기를 만든 후, 분류기들의 결과를 평균내면 다수 데이터에서의 정보 손실을 줄일 수 있음
- `imblearn` 라이브러리의 `BalacedBaggingClassifier` 로 사용 가능
# Sprint Challenge 31x

# Part 1.1 데이터베이스 생성

## schema.png 와 동일하게 데이터베이스를 생성합니다.

> Hint : 각 테이블에서 id 가 primary key 입니다.

구현해야 하는 테이블 목록은 다음과 같습니다:

- User
- Product
- User_Product

# Part 1.2 The Northwind Database

- 아래는 northwind_small의 ER (Entity-Relationship) 다이어그램입니다. 선 색상은 시각적인 구분일 뿐 의미는 없습니다.

  ![Imgur](https://i.imgur.com/G6phEg0.png)

- 아래의 코드로 DB내 모든 테이블들의 이름을 확인할 수 있습니다

  ```sql
  -- northwind_small 내의 모든 table들의 이름을 불러옵니다 --
  SELECT name
    FROM sqlite_master
  WHERE type='table'
  ORDER BY name;
  ```

- CF. 데이터베이스의 테이블들은 모두 단수형입니다 (s가 붙지않습니다). 각 테이블들의 schema는 다음의 코드로 확인 가능합니다

  ```sql
  -- Customer 테이블 schema 확인--
  SELECT sql FROM sqlite_master WHERE name="Customer";
  ```

## 아래의 조건에 맞는 쿼리문을 작성하세요

> 모든 문제는 SQL 만을 사용해서 풀어주세요.
- Part_1.py 에 좀 더 자세하게 작성되어 있습니다.

1. 데이터베이스에서 가장 비싼 제품 (개별 가격당) 10개를 불러오세요
   - 제품이름
2. 고용 당시 직원의 평균 연령은 몇살인가요?
3. 1번 문제에 제품을 만든 회사들도 같이 출력하세요
4. 제품의 종류를 가장 많이 가지고 있는 카테고리는 무엇일까요? (카테고리 이름 하나만 출력합니다)
5. 각 도시별로 직원의 평균 연령이 어떻게 다른가요?
6. 어느 직원이 가장 많은 영역을 차지하고 있나요?
 - 직원 id, 직원 Lastname, 총 영역 수를 쿼리 결과에 포함합니다.

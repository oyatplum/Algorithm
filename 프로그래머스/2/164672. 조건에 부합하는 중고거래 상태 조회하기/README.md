# [level 2] 조건에 부합하는 중고거래 상태 조회하기 - 164672 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/164672) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2025년 07월 31일 10:30:18

### 문제 설명

<p>다음은 중고거래 게시판 정보를 담은 <code>USED_GOODS_BOARD</code> 테이블입니다. <code>USED_GOODS_BOARD</code> 테이블은 다음과 같으며 <code>BOARD_ID</code>, <code>WRITER_ID</code>, <code>TITLE</code>, <code>CONTENTS</code>, <code>PRICE</code>, <code>CREATED_DATE</code>, <code>STATUS</code>, <code>VIEWS</code>은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>BOARD_ID</td>
<td>VARCHAR(5)</td>
<td>FALSE</td>
</tr>
<tr>
<td>WRITER_ID</td>
<td>VARCHAR(50)</td>
<td>FALSE</td>
</tr>
<tr>
<td>TITLE</td>
<td>VARCHAR(100)</td>
<td>FALSE</td>
</tr>
<tr>
<td>CONTENTS</td>
<td>VARCHAR(1000)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRICE</td>
<td>NUMBER</td>
<td>FALSE</td>
</tr>
<tr>
<td>CREATED_DATE</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
<tr>
<td>STATUS</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>VIEWS</td>
<td>NUMBER</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>USED_GOODS_BOARD</code> 테이블에서 2022년 10월 5일에 등록된 중고거래 게시물의 게시글 ID, 작성자 ID, 게시글 제목, 가격, 거래상태를 조회하는 SQL문을 작성해주세요. 거래상태가 SALE 이면 판매중, RESERVED이면 예약중, DONE이면 거래완료 분류하여 출력해주시고, 결과는 게시글 ID를 기준으로 내림차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p><code>USED_GOODS_BOARD</code> 테이블이 다음과 같을 때</p>
<table class="table">
        <thead><tr>
<th>BOARD_ID</th>
<th>WRITER_ID</th>
<th>TITLE</th>
<th>CONTENTS</th>
<th>PRICE</th>
<th>CREATED_DATE</th>
<th>STATUS</th>
<th>VIEWS</th>
</tr>
</thead>
        <tbody><tr>
<td>B0007</td>
<td>s2s2123</td>
<td>커피글라인더</td>
<td>새상품처럼 깨끗합니다.</td>
<td>7000</td>
<td>2022-10-04</td>
<td>DONE</td>
<td>210</td>
</tr>
<tr>
<td>B0008</td>
<td>hong02</td>
<td>자전거 판매합니다</td>
<td>출퇴근용으로 구매했다가 사용하지 않아서 내놔요</td>
<td>40000</td>
<td>2022-10-04</td>
<td>SALE</td>
<td>301</td>
</tr>
<tr>
<td>B0009</td>
<td>yawoong67</td>
<td>선반 팝니다</td>
<td>6단 선반. 환불 반품 안됩니다.</td>
<td>12000</td>
<td>2022-10-05</td>
<td>DONE</td>
<td>202</td>
</tr>
<tr>
<td>B0010</td>
<td>keel1990</td>
<td>철제선반5단</td>
<td>철제선반 5단 조립식 팜</td>
<td>10000</td>
<td>2022-10-05</td>
<td>SALE</td>
<td>194</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>BOARD_ID</th>
<th>WRITER_ID</th>
<th>TITLE</th>
<th>PRICE</th>
<th>STATUS</th>
</tr>
</thead>
        <tbody><tr>
<td>B0010</td>
<td>keel1990</td>
<td>철제선반5단</td>
<td>10000</td>
<td>판매중</td>
</tr>
<tr>
<td>B0009</td>
<td>yawoong67</td>
<td>선반 팝니다</td>
<td>12000</td>
<td>거래완료</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
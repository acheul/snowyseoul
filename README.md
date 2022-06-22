# **snowyseoul**
<br/>

## A small package for ChosunPop
+ **인구사 연구를 위한 간편한 메소드들 Small methods for historic demography data** <br/>
+ 띄어쓰기 없는 역사자료 텍스트의 편리한 분해를 위한 패키지 (slice_by_idx, slice_by_str) (will be removed) <br/>
+ 한자로 표기된 숫자의 아라비안 십진법 전환 (Chi2Fig) <br/>
+ 간지(干支) 산출을 위한 메소드 (ganji, ganji_gap, years_of_ganji) <br/>

+ (NEW) 동일인 조회를 위한 메소드 (restricted) <br/>

<br/>

## Get snowyseoul
> pip install git+https://github.com/acheul/snowyseoul.git  
> from chosun_pop import *

<br/>

## Exampes

### Chi2Fig  
  
* 한문으로 표기된 숫자를 아라비안 십진법 표기로 전환

```python
Chi2Fig('三百二十一')
```
    >> 321
```python
# 이체자도 가능하다.
Chi2Fig('壹肆百參拾貳')
```
    >> 432

### ganji, ganji_gap, years_of_ganji

```python
# ganji

print(ganji(2021))
print(ganji(2021, kr=True))
```

    >> 辛丑
    >> 신축
    


```python
# 기원전도 가능하다.

print(ganji(-200))
```

    >> 辛丑
    


```python
# ganji_gap

print(ganji_gap("을축", "갑자"))
```

    >> year_gap:  1 or 61 ...
    >> Korean_age:  2 or 62 ...
    >> None
    


```python
# years_of_ganji # ganji의 역기능. # 일단 16~21세기 내에서 추출.

years_of_ganji("신축")
```




    >> [1541, 1601, 1661, 1721, 1781, 1841, 1901, 1961, 2021, 2081]


### (NEW) Display Identical Personnels from the data (restricted usage)
+ 예시
<style type="text/css">
#T_ab3fd_row0_col0, #T_ab3fd_row0_col1, #T_ab3fd_row0_col2, #T_ab3fd_row0_col3, #T_ab3fd_row0_col4, #T_ab3fd_row0_col5, #T_ab3fd_row0_col6, #T_ab3fd_row0_col7, #T_ab3fd_row0_col8, #T_ab3fd_row0_col9, #T_ab3fd_row0_col10, #T_ab3fd_row0_col11, #T_ab3fd_row0_col12, #T_ab3fd_row0_col13, #T_ab3fd_row0_col14, #T_ab3fd_row0_col15, #T_ab3fd_row0_col16, #T_ab3fd_row0_col17, #T_ab3fd_row0_col18, #T_ab3fd_row0_col19, #T_ab3fd_row0_col20, #T_ab3fd_row0_col21, #T_ab3fd_row0_col22, #T_ab3fd_row0_col23, #T_ab3fd_row0_col24, #T_ab3fd_row0_col25, #T_ab3fd_row0_col26, #T_ab3fd_row0_col27, #T_ab3fd_row0_col28, #T_ab3fd_row0_col29, #T_ab3fd_row0_col30, #T_ab3fd_row0_col31, #T_ab3fd_row0_col32, #T_ab3fd_row0_col33, #T_ab3fd_row0_col34, #T_ab3fd_row0_col35, #T_ab3fd_row0_col36, #T_ab3fd_row0_col37, #T_ab3fd_row0_col38, #T_ab3fd_row0_col39, #T_ab3fd_row0_col40, #T_ab3fd_row0_col41, #T_ab3fd_row0_col42, #T_ab3fd_row0_col43, #T_ab3fd_row0_col44, #T_ab3fd_row0_col45, #T_ab3fd_row0_col46, #T_ab3fd_row0_col47, #T_ab3fd_row0_col48, #T_ab3fd_row0_col49, #T_ab3fd_row0_col50, #T_ab3fd_row0_col51, #T_ab3fd_row0_col52, #T_ab3fd_row0_col53, #T_ab3fd_row0_col54 {
  color: white;
  background-color: rgba(140.54901960784315, 162.63529411764705, 82.32156862745099, 1.0);
}
#T_ab3fd_row1_col0, #T_ab3fd_row1_col1, #T_ab3fd_row1_col2, #T_ab3fd_row1_col3, #T_ab3fd_row1_col4, #T_ab3fd_row1_col5, #T_ab3fd_row1_col6, #T_ab3fd_row1_col7, #T_ab3fd_row1_col8, #T_ab3fd_row1_col9, #T_ab3fd_row1_col10, #T_ab3fd_row1_col11, #T_ab3fd_row1_col12, #T_ab3fd_row1_col13, #T_ab3fd_row1_col14, #T_ab3fd_row1_col15, #T_ab3fd_row1_col16, #T_ab3fd_row1_col17, #T_ab3fd_row1_col18, #T_ab3fd_row1_col19, #T_ab3fd_row1_col20, #T_ab3fd_row1_col21, #T_ab3fd_row1_col22, #T_ab3fd_row1_col23, #T_ab3fd_row1_col24, #T_ab3fd_row1_col25, #T_ab3fd_row1_col26, #T_ab3fd_row1_col27, #T_ab3fd_row1_col28, #T_ab3fd_row1_col29, #T_ab3fd_row1_col30, #T_ab3fd_row1_col31, #T_ab3fd_row1_col32, #T_ab3fd_row1_col33, #T_ab3fd_row1_col34, #T_ab3fd_row1_col35, #T_ab3fd_row1_col36, #T_ab3fd_row1_col37, #T_ab3fd_row1_col38, #T_ab3fd_row1_col39, #T_ab3fd_row1_col40, #T_ab3fd_row1_col41, #T_ab3fd_row1_col42, #T_ab3fd_row1_col43, #T_ab3fd_row1_col44, #T_ab3fd_row1_col45, #T_ab3fd_row1_col46, #T_ab3fd_row1_col47, #T_ab3fd_row1_col48, #T_ab3fd_row1_col49, #T_ab3fd_row1_col50, #T_ab3fd_row1_col51, #T_ab3fd_row1_col52, #T_ab3fd_row1_col53, #T_ab3fd_row1_col54 {
  color: white;
  background-color: rgba(231.90588235294118, 186.72941176470587, 82.32156862745099, 1.0);
}
#T_ab3fd_row2_col0, #T_ab3fd_row2_col1, #T_ab3fd_row2_col2, #T_ab3fd_row2_col3, #T_ab3fd_row2_col4, #T_ab3fd_row2_col5, #T_ab3fd_row2_col6, #T_ab3fd_row2_col7, #T_ab3fd_row2_col8, #T_ab3fd_row2_col9, #T_ab3fd_row2_col10, #T_ab3fd_row2_col11, #T_ab3fd_row2_col12, #T_ab3fd_row2_col13, #T_ab3fd_row2_col14, #T_ab3fd_row2_col15, #T_ab3fd_row2_col16, #T_ab3fd_row2_col17, #T_ab3fd_row2_col18, #T_ab3fd_row2_col19, #T_ab3fd_row2_col20, #T_ab3fd_row2_col21, #T_ab3fd_row2_col22, #T_ab3fd_row2_col23, #T_ab3fd_row2_col24, #T_ab3fd_row2_col25, #T_ab3fd_row2_col26, #T_ab3fd_row2_col27, #T_ab3fd_row2_col28, #T_ab3fd_row2_col29, #T_ab3fd_row2_col30, #T_ab3fd_row2_col31, #T_ab3fd_row2_col32, #T_ab3fd_row2_col33, #T_ab3fd_row2_col34, #T_ab3fd_row2_col35, #T_ab3fd_row2_col36, #T_ab3fd_row2_col37, #T_ab3fd_row2_col38, #T_ab3fd_row2_col39, #T_ab3fd_row2_col40, #T_ab3fd_row2_col41, #T_ab3fd_row2_col42, #T_ab3fd_row2_col43, #T_ab3fd_row2_col44, #T_ab3fd_row2_col45, #T_ab3fd_row2_col46, #T_ab3fd_row2_col47, #T_ab3fd_row2_col48, #T_ab3fd_row2_col49, #T_ab3fd_row2_col50, #T_ab3fd_row2_col51, #T_ab3fd_row2_col52, #T_ab3fd_row2_col53, #T_ab3fd_row2_col54 {
  color: white;
  background-color: rgba(231.90588235294118, 150.58823529411765, 156.61176470588236, 1.0);
}
#T_ab3fd_row3_col0, #T_ab3fd_row3_col1, #T_ab3fd_row3_col2, #T_ab3fd_row3_col3, #T_ab3fd_row3_col4, #T_ab3fd_row3_col5, #T_ab3fd_row3_col6, #T_ab3fd_row3_col7, #T_ab3fd_row3_col8, #T_ab3fd_row3_col9, #T_ab3fd_row3_col10, #T_ab3fd_row3_col11, #T_ab3fd_row3_col12, #T_ab3fd_row3_col13, #T_ab3fd_row3_col14, #T_ab3fd_row3_col15, #T_ab3fd_row3_col16, #T_ab3fd_row3_col17, #T_ab3fd_row3_col18, #T_ab3fd_row3_col19, #T_ab3fd_row3_col20, #T_ab3fd_row3_col21, #T_ab3fd_row3_col22, #T_ab3fd_row3_col23, #T_ab3fd_row3_col24, #T_ab3fd_row3_col25, #T_ab3fd_row3_col26, #T_ab3fd_row3_col27, #T_ab3fd_row3_col28, #T_ab3fd_row3_col29, #T_ab3fd_row3_col30, #T_ab3fd_row3_col31, #T_ab3fd_row3_col32, #T_ab3fd_row3_col33, #T_ab3fd_row3_col34, #T_ab3fd_row3_col35, #T_ab3fd_row3_col36, #T_ab3fd_row3_col37, #T_ab3fd_row3_col38, #T_ab3fd_row3_col39, #T_ab3fd_row3_col40, #T_ab3fd_row3_col41, #T_ab3fd_row3_col42, #T_ab3fd_row3_col43, #T_ab3fd_row3_col44, #T_ab3fd_row3_col45, #T_ab3fd_row3_col46, #T_ab3fd_row3_col47, #T_ab3fd_row3_col48, #T_ab3fd_row3_col49, #T_ab3fd_row3_col50, #T_ab3fd_row3_col51, #T_ab3fd_row3_col52, #T_ab3fd_row3_col53, #T_ab3fd_row3_col54 {
  color: white;
  background-color: rgba(57.22352941176471, 59.23137254901961, 121.47450980392156, 1.0);
}
</style>
<table id="T_ab3fd_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >year</th>
      <th class="col_heading level0 col1" >面名</th>
      <th class="col_heading level0 col2" >면명</th>
      <th class="col_heading level0 col3" >里名</th>
      <th class="col_heading level0 col4" >리명</th>
      <th class="col_heading level0 col5" >主戶</th>
      <th class="col_heading level0 col6" >주호</th>
      <th class="col_heading level0 col7" >戶內位相</th>
      <th class="col_heading level0 col8" >호내위상</th>
      <th class="col_heading level0 col9" >職役</th>
      <th class="col_heading level0 col10" >직역</th>
      <th class="col_heading level0 col11" >姓</th>
      <th class="col_heading level0 col12" >名</th>
      <th class="col_heading level0 col13" >성</th>
      <th class="col_heading level0 col14" >명</th>
      <th class="col_heading level0 col15" >年齡</th>
      <th class="col_heading level0 col16" >干支</th>
      <th class="col_heading level0 col17" >간지</th>
      <th class="col_heading level0 col18" >出入</th>
      <th class="col_heading level0 col19" >處</th>
      <th class="col_heading level0 col20" >출입</th>
      <th class="col_heading level0 col21" >처</th>
      <th class="col_heading level0 col22" >加入</th>
      <th class="col_heading level0 col23" >가입</th>
      <th class="col_heading level0 col24" >本</th>
      <th class="col_heading level0 col25" >本貫</th>
      <th class="col_heading level0 col26" >본</th>
      <th class="col_heading level0 col27" >본관</th>
      <th class="col_heading level0 col28" >主居</th>
      <th class="col_heading level0 col29" >주거</th>
      <th class="col_heading level0 col30" >主職役</th>
      <th class="col_heading level0 col31" >주직역</th>
      <th class="col_heading level0 col32" >主姓名</th>
      <th class="col_heading level0 col33" >주성명</th>
      <th class="col_heading level0 col34" >父職役</th>
      <th class="col_heading level0 col35" >부직역</th>
      <th class="col_heading level0 col36" >父名</th>
      <th class="col_heading level0 col37" >부명</th>
      <th class="col_heading level0 col38" >母職役</th>
      <th class="col_heading level0 col39" >모직역</th>
      <th class="col_heading level0 col40" >母名</th>
      <th class="col_heading level0 col41" >모명</th>
      <th class="col_heading level0 col42" >所生</th>
      <th class="col_heading level0 col43" >祖職役</th>
      <th class="col_heading level0 col44" >조직역</th>
      <th class="col_heading level0 col45" >祖名</th>
      <th class="col_heading level0 col46" >조명</th>
      <th class="col_heading level0 col47" >曾祖職役</th>
      <th class="col_heading level0 col48" >증조직역</th>
      <th class="col_heading level0 col49" >曾祖名</th>
      <th class="col_heading level0 col50" >증조명</th>
      <th class="col_heading level0 col51" >外祖職役</th>
      <th class="col_heading level0 col52" >외조직역</th>
      <th class="col_heading level0 col53" >外祖名</th>
      <th class="col_heading level0 col54" >외조명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ab3fd_level0_row0" class="row_heading level0 row0" >222949</th>
      <td id="T_ab3fd_row0_col0" class="data row0 col0" >1828</td>
      <td id="T_ab3fd_row0_col1" class="data row0 col1" >新等</td>
      <td id="T_ab3fd_row0_col2" class="data row0 col2" >신등</td>
      <td id="T_ab3fd_row0_col3" class="data row0 col3" >陽田</td>
      <td id="T_ab3fd_row0_col4" class="data row0 col4" >양전</td>
      <td id="T_ab3fd_row0_col5" class="data row0 col5" >權克成</td>
      <td id="T_ab3fd_row0_col6" class="data row0 col6" >권극성</td>
      <td id="T_ab3fd_row0_col7" class="data row0 col7" >主戶</td>
      <td id="T_ab3fd_row0_col8" class="data row0 col8" >주호</td>
      <td id="T_ab3fd_row0_col9" class="data row0 col9" >幼學</td>
      <td id="T_ab3fd_row0_col10" class="data row0 col10" >유학</td>
      <td id="T_ab3fd_row0_col11" class="data row0 col11" >權</td>
      <td id="T_ab3fd_row0_col12" class="data row0 col12" >克成</td>
      <td id="T_ab3fd_row0_col13" class="data row0 col13" >권</td>
      <td id="T_ab3fd_row0_col14" class="data row0 col14" >극성</td>
      <td id="T_ab3fd_row0_col15" class="data row0 col15" >45</td>
      <td id="T_ab3fd_row0_col16" class="data row0 col16" >甲辰</td>
      <td id="T_ab3fd_row0_col17" class="data row0 col17" >갑진</td>
      <td id="T_ab3fd_row0_col18" class="data row0 col18" ></td>
      <td id="T_ab3fd_row0_col19" class="data row0 col19" ></td>
      <td id="T_ab3fd_row0_col20" class="data row0 col20" ></td>
      <td id="T_ab3fd_row0_col21" class="data row0 col21" ></td>
      <td id="T_ab3fd_row0_col22" class="data row0 col22" ></td>
      <td id="T_ab3fd_row0_col23" class="data row0 col23" ></td>
      <td id="T_ab3fd_row0_col24" class="data row0 col24" >本</td>
      <td id="T_ab3fd_row0_col25" class="data row0 col25" >安東</td>
      <td id="T_ab3fd_row0_col26" class="data row0 col26" >본</td>
      <td id="T_ab3fd_row0_col27" class="data row0 col27" >안동</td>
      <td id="T_ab3fd_row0_col28" class="data row0 col28" ></td>
      <td id="T_ab3fd_row0_col29" class="data row0 col29" ></td>
      <td id="T_ab3fd_row0_col30" class="data row0 col30" ></td>
      <td id="T_ab3fd_row0_col31" class="data row0 col31" ></td>
      <td id="T_ab3fd_row0_col32" class="data row0 col32" ></td>
      <td id="T_ab3fd_row0_col33" class="data row0 col33" ></td>
      <td id="T_ab3fd_row0_col34" class="data row0 col34" ></td>
      <td id="T_ab3fd_row0_col35" class="data row0 col35" ></td>
      <td id="T_ab3fd_row0_col36" class="data row0 col36" >正萬</td>
      <td id="T_ab3fd_row0_col37" class="data row0 col37" >정만</td>
      <td id="T_ab3fd_row0_col38" class="data row0 col38" ></td>
      <td id="T_ab3fd_row0_col39" class="data row0 col39" ></td>
      <td id="T_ab3fd_row0_col40" class="data row0 col40" ></td>
      <td id="T_ab3fd_row0_col41" class="data row0 col41" ></td>
      <td id="T_ab3fd_row0_col42" class="data row0 col42" ></td>
      <td id="T_ab3fd_row0_col43" class="data row0 col43" >成均進士</td>
      <td id="T_ab3fd_row0_col44" class="data row0 col44" >성균진사</td>
      <td id="T_ab3fd_row0_col45" class="data row0 col45" >煒</td>
      <td id="T_ab3fd_row0_col46" class="data row0 col46" >위</td>
      <td id="T_ab3fd_row0_col47" class="data row0 col47" >學生</td>
      <td id="T_ab3fd_row0_col48" class="data row0 col48" >학생</td>
      <td id="T_ab3fd_row0_col49" class="data row0 col49" >必隨</td>
      <td id="T_ab3fd_row0_col50" class="data row0 col50" >필수</td>
      <td id="T_ab3fd_row0_col51" class="data row0 col51" >學生</td>
      <td id="T_ab3fd_row0_col52" class="data row0 col52" >학생</td>
      <td id="T_ab3fd_row0_col53" class="data row0 col53" >金柱</td>
      <td id="T_ab3fd_row0_col54" class="data row0 col54" >김주</td>
    </tr>
    <tr>
      <th id="T_ab3fd_level0_row1" class="row_heading level0 row1" >222950</th>
      <td id="T_ab3fd_row1_col0" class="data row1 col0" >1828</td>
      <td id="T_ab3fd_row1_col1" class="data row1 col1" >新等</td>
      <td id="T_ab3fd_row1_col2" class="data row1 col2" >신등</td>
      <td id="T_ab3fd_row1_col3" class="data row1 col3" >陽田</td>
      <td id="T_ab3fd_row1_col4" class="data row1 col4" >양전</td>
      <td id="T_ab3fd_row1_col5" class="data row1 col5" >權克成</td>
      <td id="T_ab3fd_row1_col6" class="data row1 col6" >권극성</td>
      <td id="T_ab3fd_row1_col7" class="data row1 col7" >妻</td>
      <td id="T_ab3fd_row1_col8" class="data row1 col8" >처</td>
      <td id="T_ab3fd_row1_col9" class="data row1 col9" ></td>
      <td id="T_ab3fd_row1_col10" class="data row1 col10" ></td>
      <td id="T_ab3fd_row1_col11" class="data row1 col11" >河</td>
      <td id="T_ab3fd_row1_col12" class="data row1 col12" >氏</td>
      <td id="T_ab3fd_row1_col13" class="data row1 col13" >하</td>
      <td id="T_ab3fd_row1_col14" class="data row1 col14" >씨</td>
      <td id="T_ab3fd_row1_col15" class="data row1 col15" >40</td>
      <td id="T_ab3fd_row1_col16" class="data row1 col16" ></td>
      <td id="T_ab3fd_row1_col17" class="data row1 col17" ></td>
      <td id="T_ab3fd_row1_col18" class="data row1 col18" ></td>
      <td id="T_ab3fd_row1_col19" class="data row1 col19" ></td>
      <td id="T_ab3fd_row1_col20" class="data row1 col20" ></td>
      <td id="T_ab3fd_row1_col21" class="data row1 col21" ></td>
      <td id="T_ab3fd_row1_col22" class="data row1 col22" ></td>
      <td id="T_ab3fd_row1_col23" class="data row1 col23" ></td>
      <td id="T_ab3fd_row1_col24" class="data row1 col24" >籍</td>
      <td id="T_ab3fd_row1_col25" class="data row1 col25" >晉州</td>
      <td id="T_ab3fd_row1_col26" class="data row1 col26" >적</td>
      <td id="T_ab3fd_row1_col27" class="data row1 col27" >진주</td>
      <td id="T_ab3fd_row1_col28" class="data row1 col28" ></td>
      <td id="T_ab3fd_row1_col29" class="data row1 col29" ></td>
      <td id="T_ab3fd_row1_col30" class="data row1 col30" ></td>
      <td id="T_ab3fd_row1_col31" class="data row1 col31" ></td>
      <td id="T_ab3fd_row1_col32" class="data row1 col32" ></td>
      <td id="T_ab3fd_row1_col33" class="data row1 col33" ></td>
      <td id="T_ab3fd_row1_col34" class="data row1 col34" >學生</td>
      <td id="T_ab3fd_row1_col35" class="data row1 col35" >학생</td>
      <td id="T_ab3fd_row1_col36" class="data row1 col36" >應斗</td>
      <td id="T_ab3fd_row1_col37" class="data row1 col37" >응두</td>
      <td id="T_ab3fd_row1_col38" class="data row1 col38" ></td>
      <td id="T_ab3fd_row1_col39" class="data row1 col39" ></td>
      <td id="T_ab3fd_row1_col40" class="data row1 col40" ></td>
      <td id="T_ab3fd_row1_col41" class="data row1 col41" ></td>
      <td id="T_ab3fd_row1_col42" class="data row1 col42" ></td>
      <td id="T_ab3fd_row1_col43" class="data row1 col43" >學生</td>
      <td id="T_ab3fd_row1_col44" class="data row1 col44" >학생</td>
      <td id="T_ab3fd_row1_col45" class="data row1 col45" >潤益</td>
      <td id="T_ab3fd_row1_col46" class="data row1 col46" >윤익</td>
      <td id="T_ab3fd_row1_col47" class="data row1 col47" >宣武郞</td>
      <td id="T_ab3fd_row1_col48" class="data row1 col48" >선무랑</td>
      <td id="T_ab3fd_row1_col49" class="data row1 col49" >涑</td>
      <td id="T_ab3fd_row1_col50" class="data row1 col50" >속</td>
      <td id="T_ab3fd_row1_col51" class="data row1 col51" >學生</td>
      <td id="T_ab3fd_row1_col52" class="data row1 col52" >학생</td>
      <td id="T_ab3fd_row1_col53" class="data row1 col53" >辛桂復</td>
      <td id="T_ab3fd_row1_col54" class="data row1 col54" >신계복</td>
    </tr>
    <tr>
      <th id="T_ab3fd_level0_row2" class="row_heading level0 row2" >222951</th>
      <td id="T_ab3fd_row2_col0" class="data row2 col0" >1828</td>
      <td id="T_ab3fd_row2_col1" class="data row2 col1" >新等</td>
      <td id="T_ab3fd_row2_col2" class="data row2 col2" >신등</td>
      <td id="T_ab3fd_row2_col3" class="data row2 col3" >陽田</td>
      <td id="T_ab3fd_row2_col4" class="data row2 col4" >양전</td>
      <td id="T_ab3fd_row2_col5" class="data row2 col5" >權克成</td>
      <td id="T_ab3fd_row2_col6" class="data row2 col6" >권극성</td>
      <td id="T_ab3fd_row2_col7" class="data row2 col7" >子</td>
      <td id="T_ab3fd_row2_col8" class="data row2 col8" >자</td>
      <td id="T_ab3fd_row2_col9" class="data row2 col9" ></td>
      <td id="T_ab3fd_row2_col10" class="data row2 col10" ></td>
      <td id="T_ab3fd_row2_col11" class="data row2 col11" >權</td>
      <td id="T_ab3fd_row2_col12" class="data row2 col12" >文道</td>
      <td id="T_ab3fd_row2_col13" class="data row2 col13" >권</td>
      <td id="T_ab3fd_row2_col14" class="data row2 col14" >문도</td>
      <td id="T_ab3fd_row2_col15" class="data row2 col15" >?</td>
      <td id="T_ab3fd_row2_col16" class="data row2 col16" ></td>
      <td id="T_ab3fd_row2_col17" class="data row2 col17" ></td>
      <td id="T_ab3fd_row2_col18" class="data row2 col18" ></td>
      <td id="T_ab3fd_row2_col19" class="data row2 col19" ></td>
      <td id="T_ab3fd_row2_col20" class="data row2 col20" ></td>
      <td id="T_ab3fd_row2_col21" class="data row2 col21" ></td>
      <td id="T_ab3fd_row2_col22" class="data row2 col22" ></td>
      <td id="T_ab3fd_row2_col23" class="data row2 col23" ></td>
      <td id="T_ab3fd_row2_col24" class="data row2 col24" ></td>
      <td id="T_ab3fd_row2_col25" class="data row2 col25" ></td>
      <td id="T_ab3fd_row2_col26" class="data row2 col26" ></td>
      <td id="T_ab3fd_row2_col27" class="data row2 col27" ></td>
      <td id="T_ab3fd_row2_col28" class="data row2 col28" ></td>
      <td id="T_ab3fd_row2_col29" class="data row2 col29" ></td>
      <td id="T_ab3fd_row2_col30" class="data row2 col30" ></td>
      <td id="T_ab3fd_row2_col31" class="data row2 col31" ></td>
      <td id="T_ab3fd_row2_col32" class="data row2 col32" ></td>
      <td id="T_ab3fd_row2_col33" class="data row2 col33" ></td>
      <td id="T_ab3fd_row2_col34" class="data row2 col34" ></td>
      <td id="T_ab3fd_row2_col35" class="data row2 col35" ></td>
      <td id="T_ab3fd_row2_col36" class="data row2 col36" ></td>
      <td id="T_ab3fd_row2_col37" class="data row2 col37" ></td>
      <td id="T_ab3fd_row2_col38" class="data row2 col38" ></td>
      <td id="T_ab3fd_row2_col39" class="data row2 col39" ></td>
      <td id="T_ab3fd_row2_col40" class="data row2 col40" ></td>
      <td id="T_ab3fd_row2_col41" class="data row2 col41" ></td>
      <td id="T_ab3fd_row2_col42" class="data row2 col42" ></td>
      <td id="T_ab3fd_row2_col43" class="data row2 col43" ></td>
      <td id="T_ab3fd_row2_col44" class="data row2 col44" ></td>
      <td id="T_ab3fd_row2_col45" class="data row2 col45" ></td>
      <td id="T_ab3fd_row2_col46" class="data row2 col46" ></td>
      <td id="T_ab3fd_row2_col47" class="data row2 col47" ></td>
      <td id="T_ab3fd_row2_col48" class="data row2 col48" ></td>
      <td id="T_ab3fd_row2_col49" class="data row2 col49" ></td>
      <td id="T_ab3fd_row2_col50" class="data row2 col50" ></td>
      <td id="T_ab3fd_row2_col51" class="data row2 col51" ></td>
      <td id="T_ab3fd_row2_col52" class="data row2 col52" ></td>
      <td id="T_ab3fd_row2_col53" class="data row2 col53" ></td>
      <td id="T_ab3fd_row2_col54" class="data row2 col54" ></td>
    </tr>
    <tr>
      <th id="T_ab3fd_level0_row3" class="row_heading level0 row3" >222952</th>
      <td id="T_ab3fd_row3_col0" class="data row3 col0" >1828</td>
      <td id="T_ab3fd_row3_col1" class="data row3 col1" >新等</td>
      <td id="T_ab3fd_row3_col2" class="data row3 col2" >신등</td>
      <td id="T_ab3fd_row3_col3" class="data row3 col3" >陽田</td>
      <td id="T_ab3fd_row3_col4" class="data row3 col4" >양전</td>
      <td id="T_ab3fd_row3_col5" class="data row3 col5" >權克成</td>
      <td id="T_ab3fd_row3_col6" class="data row3 col6" >권극성</td>
      <td id="T_ab3fd_row3_col7" class="data row3 col7" >奴婢</td>
      <td id="T_ab3fd_row3_col8" class="data row3 col8" >노비</td>
      <td id="T_ab3fd_row3_col9" class="data row3 col9" >婢</td>
      <td id="T_ab3fd_row3_col10" class="data row3 col10" >비</td>
      <td id="T_ab3fd_row3_col11" class="data row3 col11" ></td>
      <td id="T_ab3fd_row3_col12" class="data row3 col12" >長守</td>
      <td id="T_ab3fd_row3_col13" class="data row3 col13" ></td>
      <td id="T_ab3fd_row3_col14" class="data row3 col14" >장수</td>
      <td id="T_ab3fd_row3_col15" class="data row3 col15" ></td>
      <td id="T_ab3fd_row3_col16" class="data row3 col16" ></td>
      <td id="T_ab3fd_row3_col17" class="data row3 col17" ></td>
      <td id="T_ab3fd_row3_col18" class="data row3 col18" ></td>
      <td id="T_ab3fd_row3_col19" class="data row3 col19" ></td>
      <td id="T_ab3fd_row3_col20" class="data row3 col20" ></td>
      <td id="T_ab3fd_row3_col21" class="data row3 col21" ></td>
      <td id="T_ab3fd_row3_col22" class="data row3 col22" ></td>
      <td id="T_ab3fd_row3_col23" class="data row3 col23" ></td>
      <td id="T_ab3fd_row3_col24" class="data row3 col24" ></td>
      <td id="T_ab3fd_row3_col25" class="data row3 col25" ></td>
      <td id="T_ab3fd_row3_col26" class="data row3 col26" ></td>
      <td id="T_ab3fd_row3_col27" class="data row3 col27" ></td>
      <td id="T_ab3fd_row3_col28" class="data row3 col28" ></td>
      <td id="T_ab3fd_row3_col29" class="data row3 col29" ></td>
      <td id="T_ab3fd_row3_col30" class="data row3 col30" ></td>
      <td id="T_ab3fd_row3_col31" class="data row3 col31" ></td>
      <td id="T_ab3fd_row3_col32" class="data row3 col32" ></td>
      <td id="T_ab3fd_row3_col33" class="data row3 col33" ></td>
      <td id="T_ab3fd_row3_col34" class="data row3 col34" ></td>
      <td id="T_ab3fd_row3_col35" class="data row3 col35" ></td>
      <td id="T_ab3fd_row3_col36" class="data row3 col36" ></td>
      <td id="T_ab3fd_row3_col37" class="data row3 col37" ></td>
      <td id="T_ab3fd_row3_col38" class="data row3 col38" ></td>
      <td id="T_ab3fd_row3_col39" class="data row3 col39" ></td>
      <td id="T_ab3fd_row3_col40" class="data row3 col40" ></td>
      <td id="T_ab3fd_row3_col41" class="data row3 col41" ></td>
      <td id="T_ab3fd_row3_col42" class="data row3 col42" ></td>
      <td id="T_ab3fd_row3_col43" class="data row3 col43" ></td>
      <td id="T_ab3fd_row3_col44" class="data row3 col44" ></td>
      <td id="T_ab3fd_row3_col45" class="data row3 col45" ></td>
      <td id="T_ab3fd_row3_col46" class="data row3 col46" ></td>
      <td id="T_ab3fd_row3_col47" class="data row3 col47" ></td>
      <td id="T_ab3fd_row3_col48" class="data row3 col48" ></td>
      <td id="T_ab3fd_row3_col49" class="data row3 col49" ></td>
      <td id="T_ab3fd_row3_col50" class="data row3 col50" ></td>
      <td id="T_ab3fd_row3_col51" class="data row3 col51" ></td>
      <td id="T_ab3fd_row3_col52" class="data row3 col52" ></td>
      <td id="T_ab3fd_row3_col53" class="data row3 col53" ></td>
      <td id="T_ab3fd_row3_col54" class="data row3 col54" ></td>
    </tr>
  </tbody>
</table>
<style type="text/css">
#T_5c1a5_row0_col0, #T_5c1a5_row0_col1, #T_5c1a5_row0_col2, #T_5c1a5_row0_col3, #T_5c1a5_row0_col4, #T_5c1a5_row0_col5, #T_5c1a5_row0_col6, #T_5c1a5_row0_col7, #T_5c1a5_row0_col8, #T_5c1a5_row0_col9, #T_5c1a5_row0_col10, #T_5c1a5_row0_col11, #T_5c1a5_row0_col12, #T_5c1a5_row0_col13, #T_5c1a5_row0_col14, #T_5c1a5_row0_col15, #T_5c1a5_row0_col16, #T_5c1a5_row0_col17, #T_5c1a5_row0_col18, #T_5c1a5_row0_col19, #T_5c1a5_row0_col20, #T_5c1a5_row0_col21, #T_5c1a5_row0_col22, #T_5c1a5_row0_col23, #T_5c1a5_row0_col24, #T_5c1a5_row0_col25, #T_5c1a5_row0_col26, #T_5c1a5_row0_col27, #T_5c1a5_row0_col28, #T_5c1a5_row0_col29, #T_5c1a5_row0_col30, #T_5c1a5_row0_col31, #T_5c1a5_row0_col32, #T_5c1a5_row0_col33, #T_5c1a5_row0_col34, #T_5c1a5_row0_col35, #T_5c1a5_row0_col36, #T_5c1a5_row0_col37, #T_5c1a5_row0_col38, #T_5c1a5_row0_col39, #T_5c1a5_row0_col40, #T_5c1a5_row0_col41, #T_5c1a5_row0_col42, #T_5c1a5_row0_col43, #T_5c1a5_row0_col44, #T_5c1a5_row0_col45, #T_5c1a5_row0_col46, #T_5c1a5_row0_col47, #T_5c1a5_row0_col48, #T_5c1a5_row0_col49, #T_5c1a5_row0_col50, #T_5c1a5_row0_col51, #T_5c1a5_row0_col52, #T_5c1a5_row0_col53, #T_5c1a5_row0_col54 {
  color: white;
  background-color: rgba(140.54901960784315, 162.63529411764705, 82.32156862745099, 1.0);
}
#T_5c1a5_row1_col0, #T_5c1a5_row1_col1, #T_5c1a5_row1_col2, #T_5c1a5_row1_col3, #T_5c1a5_row1_col4, #T_5c1a5_row1_col5, #T_5c1a5_row1_col6, #T_5c1a5_row1_col7, #T_5c1a5_row1_col8, #T_5c1a5_row1_col9, #T_5c1a5_row1_col10, #T_5c1a5_row1_col11, #T_5c1a5_row1_col12, #T_5c1a5_row1_col13, #T_5c1a5_row1_col14, #T_5c1a5_row1_col15, #T_5c1a5_row1_col16, #T_5c1a5_row1_col17, #T_5c1a5_row1_col18, #T_5c1a5_row1_col19, #T_5c1a5_row1_col20, #T_5c1a5_row1_col21, #T_5c1a5_row1_col22, #T_5c1a5_row1_col23, #T_5c1a5_row1_col24, #T_5c1a5_row1_col25, #T_5c1a5_row1_col26, #T_5c1a5_row1_col27, #T_5c1a5_row1_col28, #T_5c1a5_row1_col29, #T_5c1a5_row1_col30, #T_5c1a5_row1_col31, #T_5c1a5_row1_col32, #T_5c1a5_row1_col33, #T_5c1a5_row1_col34, #T_5c1a5_row1_col35, #T_5c1a5_row1_col36, #T_5c1a5_row1_col37, #T_5c1a5_row1_col38, #T_5c1a5_row1_col39, #T_5c1a5_row1_col40, #T_5c1a5_row1_col41, #T_5c1a5_row1_col42, #T_5c1a5_row1_col43, #T_5c1a5_row1_col44, #T_5c1a5_row1_col45, #T_5c1a5_row1_col46, #T_5c1a5_row1_col47, #T_5c1a5_row1_col48, #T_5c1a5_row1_col49, #T_5c1a5_row1_col50, #T_5c1a5_row1_col51, #T_5c1a5_row1_col52, #T_5c1a5_row1_col53, #T_5c1a5_row1_col54 {
  color: white;
  background-color: rgba(231.90588235294118, 186.72941176470587, 82.32156862745099, 1.0);
}
#T_5c1a5_row2_col0, #T_5c1a5_row2_col1, #T_5c1a5_row2_col2, #T_5c1a5_row2_col3, #T_5c1a5_row2_col4, #T_5c1a5_row2_col5, #T_5c1a5_row2_col6, #T_5c1a5_row2_col7, #T_5c1a5_row2_col8, #T_5c1a5_row2_col9, #T_5c1a5_row2_col10, #T_5c1a5_row2_col11, #T_5c1a5_row2_col12, #T_5c1a5_row2_col13, #T_5c1a5_row2_col14, #T_5c1a5_row2_col15, #T_5c1a5_row2_col16, #T_5c1a5_row2_col17, #T_5c1a5_row2_col18, #T_5c1a5_row2_col19, #T_5c1a5_row2_col20, #T_5c1a5_row2_col21, #T_5c1a5_row2_col22, #T_5c1a5_row2_col23, #T_5c1a5_row2_col24, #T_5c1a5_row2_col25, #T_5c1a5_row2_col26, #T_5c1a5_row2_col27, #T_5c1a5_row2_col28, #T_5c1a5_row2_col29, #T_5c1a5_row2_col30, #T_5c1a5_row2_col31, #T_5c1a5_row2_col32, #T_5c1a5_row2_col33, #T_5c1a5_row2_col34, #T_5c1a5_row2_col35, #T_5c1a5_row2_col36, #T_5c1a5_row2_col37, #T_5c1a5_row2_col38, #T_5c1a5_row2_col39, #T_5c1a5_row2_col40, #T_5c1a5_row2_col41, #T_5c1a5_row2_col42, #T_5c1a5_row2_col43, #T_5c1a5_row2_col44, #T_5c1a5_row2_col45, #T_5c1a5_row2_col46, #T_5c1a5_row2_col47, #T_5c1a5_row2_col48, #T_5c1a5_row2_col49, #T_5c1a5_row2_col50, #T_5c1a5_row2_col51, #T_5c1a5_row2_col52, #T_5c1a5_row2_col53, #T_5c1a5_row2_col54 {
  color: white;
  background-color: rgba(231.90588235294118, 150.58823529411765, 156.61176470588236, 1.0);
}
#T_5c1a5_row4_col0, #T_5c1a5_row4_col1, #T_5c1a5_row4_col2, #T_5c1a5_row4_col3, #T_5c1a5_row4_col4, #T_5c1a5_row4_col5, #T_5c1a5_row4_col6, #T_5c1a5_row4_col7, #T_5c1a5_row4_col8, #T_5c1a5_row4_col9, #T_5c1a5_row4_col10, #T_5c1a5_row4_col11, #T_5c1a5_row4_col12, #T_5c1a5_row4_col13, #T_5c1a5_row4_col14, #T_5c1a5_row4_col15, #T_5c1a5_row4_col16, #T_5c1a5_row4_col17, #T_5c1a5_row4_col18, #T_5c1a5_row4_col19, #T_5c1a5_row4_col20, #T_5c1a5_row4_col21, #T_5c1a5_row4_col22, #T_5c1a5_row4_col23, #T_5c1a5_row4_col24, #T_5c1a5_row4_col25, #T_5c1a5_row4_col26, #T_5c1a5_row4_col27, #T_5c1a5_row4_col28, #T_5c1a5_row4_col29, #T_5c1a5_row4_col30, #T_5c1a5_row4_col31, #T_5c1a5_row4_col32, #T_5c1a5_row4_col33, #T_5c1a5_row4_col34, #T_5c1a5_row4_col35, #T_5c1a5_row4_col36, #T_5c1a5_row4_col37, #T_5c1a5_row4_col38, #T_5c1a5_row4_col39, #T_5c1a5_row4_col40, #T_5c1a5_row4_col41, #T_5c1a5_row4_col42, #T_5c1a5_row4_col43, #T_5c1a5_row4_col44, #T_5c1a5_row4_col45, #T_5c1a5_row4_col46, #T_5c1a5_row4_col47, #T_5c1a5_row4_col48, #T_5c1a5_row4_col49, #T_5c1a5_row4_col50, #T_5c1a5_row4_col51, #T_5c1a5_row4_col52, #T_5c1a5_row4_col53, #T_5c1a5_row4_col54 {
  color: white;
  background-color: rgba(57.22352941176471, 59.23137254901961, 121.47450980392156, 1.0);
}
</style>
<table id="T_5c1a5_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >year</th>
      <th class="col_heading level0 col1" >面名</th>
      <th class="col_heading level0 col2" >면명</th>
      <th class="col_heading level0 col3" >里名</th>
      <th class="col_heading level0 col4" >리명</th>
      <th class="col_heading level0 col5" >主戶</th>
      <th class="col_heading level0 col6" >주호</th>
      <th class="col_heading level0 col7" >戶內位相</th>
      <th class="col_heading level0 col8" >호내위상</th>
      <th class="col_heading level0 col9" >職役</th>
      <th class="col_heading level0 col10" >직역</th>
      <th class="col_heading level0 col11" >姓</th>
      <th class="col_heading level0 col12" >名</th>
      <th class="col_heading level0 col13" >성</th>
      <th class="col_heading level0 col14" >명</th>
      <th class="col_heading level0 col15" >年齡</th>
      <th class="col_heading level0 col16" >干支</th>
      <th class="col_heading level0 col17" >간지</th>
      <th class="col_heading level0 col18" >出入</th>
      <th class="col_heading level0 col19" >處</th>
      <th class="col_heading level0 col20" >출입</th>
      <th class="col_heading level0 col21" >처</th>
      <th class="col_heading level0 col22" >加入</th>
      <th class="col_heading level0 col23" >가입</th>
      <th class="col_heading level0 col24" >本</th>
      <th class="col_heading level0 col25" >本貫</th>
      <th class="col_heading level0 col26" >본</th>
      <th class="col_heading level0 col27" >본관</th>
      <th class="col_heading level0 col28" >主居</th>
      <th class="col_heading level0 col29" >주거</th>
      <th class="col_heading level0 col30" >主職役</th>
      <th class="col_heading level0 col31" >주직역</th>
      <th class="col_heading level0 col32" >主姓名</th>
      <th class="col_heading level0 col33" >주성명</th>
      <th class="col_heading level0 col34" >父職役</th>
      <th class="col_heading level0 col35" >부직역</th>
      <th class="col_heading level0 col36" >父名</th>
      <th class="col_heading level0 col37" >부명</th>
      <th class="col_heading level0 col38" >母職役</th>
      <th class="col_heading level0 col39" >모직역</th>
      <th class="col_heading level0 col40" >母名</th>
      <th class="col_heading level0 col41" >모명</th>
      <th class="col_heading level0 col42" >所生</th>
      <th class="col_heading level0 col43" >祖職役</th>
      <th class="col_heading level0 col44" >조직역</th>
      <th class="col_heading level0 col45" >祖名</th>
      <th class="col_heading level0 col46" >조명</th>
      <th class="col_heading level0 col47" >曾祖職役</th>
      <th class="col_heading level0 col48" >증조직역</th>
      <th class="col_heading level0 col49" >曾祖名</th>
      <th class="col_heading level0 col50" >증조명</th>
      <th class="col_heading level0 col51" >外祖職役</th>
      <th class="col_heading level0 col52" >외조직역</th>
      <th class="col_heading level0 col53" >外祖名</th>
      <th class="col_heading level0 col54" >외조명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_5c1a5_level0_row0" class="row_heading level0 row0" >232239</th>
      <td id="T_5c1a5_row0_col0" class="data row0 col0" >1837</td>
      <td id="T_5c1a5_row0_col1" class="data row0 col1" >新等</td>
      <td id="T_5c1a5_row0_col2" class="data row0 col2" >신등</td>
      <td id="T_5c1a5_row0_col3" class="data row0 col3" >陽田</td>
      <td id="T_5c1a5_row0_col4" class="data row0 col4" >양전</td>
      <td id="T_5c1a5_row0_col5" class="data row0 col5" >權福成</td>
      <td id="T_5c1a5_row0_col6" class="data row0 col6" >권복성</td>
      <td id="T_5c1a5_row0_col7" class="data row0 col7" >主戶</td>
      <td id="T_5c1a5_row0_col8" class="data row0 col8" >주호</td>
      <td id="T_5c1a5_row0_col9" class="data row0 col9" >幼學</td>
      <td id="T_5c1a5_row0_col10" class="data row0 col10" >유학</td>
      <td id="T_5c1a5_row0_col11" class="data row0 col11" >權</td>
      <td id="T_5c1a5_row0_col12" class="data row0 col12" >福成</td>
      <td id="T_5c1a5_row0_col13" class="data row0 col13" >권</td>
      <td id="T_5c1a5_row0_col14" class="data row0 col14" >복성</td>
      <td id="T_5c1a5_row0_col15" class="data row0 col15" >54.0</td>
      <td id="T_5c1a5_row0_col16" class="data row0 col16" >甲辰</td>
      <td id="T_5c1a5_row0_col17" class="data row0 col17" >갑진</td>
      <td id="T_5c1a5_row0_col18" class="data row0 col18" ></td>
      <td id="T_5c1a5_row0_col19" class="data row0 col19" ></td>
      <td id="T_5c1a5_row0_col20" class="data row0 col20" ></td>
      <td id="T_5c1a5_row0_col21" class="data row0 col21" ></td>
      <td id="T_5c1a5_row0_col22" class="data row0 col22" ></td>
      <td id="T_5c1a5_row0_col23" class="data row0 col23" ></td>
      <td id="T_5c1a5_row0_col24" class="data row0 col24" >本</td>
      <td id="T_5c1a5_row0_col25" class="data row0 col25" >安東</td>
      <td id="T_5c1a5_row0_col26" class="data row0 col26" >본</td>
      <td id="T_5c1a5_row0_col27" class="data row0 col27" >안동</td>
      <td id="T_5c1a5_row0_col28" class="data row0 col28" ></td>
      <td id="T_5c1a5_row0_col29" class="data row0 col29" ></td>
      <td id="T_5c1a5_row0_col30" class="data row0 col30" ></td>
      <td id="T_5c1a5_row0_col31" class="data row0 col31" ></td>
      <td id="T_5c1a5_row0_col32" class="data row0 col32" ></td>
      <td id="T_5c1a5_row0_col33" class="data row0 col33" ></td>
      <td id="T_5c1a5_row0_col34" class="data row0 col34" >學生</td>
      <td id="T_5c1a5_row0_col35" class="data row0 col35" >학생</td>
      <td id="T_5c1a5_row0_col36" class="data row0 col36" >正句</td>
      <td id="T_5c1a5_row0_col37" class="data row0 col37" >정구</td>
      <td id="T_5c1a5_row0_col38" class="data row0 col38" ></td>
      <td id="T_5c1a5_row0_col39" class="data row0 col39" ></td>
      <td id="T_5c1a5_row0_col40" class="data row0 col40" ></td>
      <td id="T_5c1a5_row0_col41" class="data row0 col41" ></td>
      <td id="T_5c1a5_row0_col42" class="data row0 col42" ></td>
      <td id="T_5c1a5_row0_col43" class="data row0 col43" >通德郞</td>
      <td id="T_5c1a5_row0_col44" class="data row0 col44" >통덕랑</td>
      <td id="T_5c1a5_row0_col45" class="data row0 col45" >頻</td>
      <td id="T_5c1a5_row0_col46" class="data row0 col46" >빈</td>
      <td id="T_5c1a5_row0_col47" class="data row0 col47" >通訓大夫北淸鎭管行洪原縣監</td>
      <td id="T_5c1a5_row0_col48" class="data row0 col48" >통훈대부북청진관행홍원현감</td>
      <td id="T_5c1a5_row0_col49" class="data row0 col49" >必恒</td>
      <td id="T_5c1a5_row0_col50" class="data row0 col50" >필항</td>
      <td id="T_5c1a5_row0_col51" class="data row0 col51" >學生</td>
      <td id="T_5c1a5_row0_col52" class="data row0 col52" >학생</td>
      <td id="T_5c1a5_row0_col53" class="data row0 col53" >白尙晶</td>
      <td id="T_5c1a5_row0_col54" class="data row0 col54" >백상정</td>
    </tr>
    <tr>
      <th id="T_5c1a5_level0_row1" class="row_heading level0 row1" >232240</th>
      <td id="T_5c1a5_row1_col0" class="data row1 col0" >1837</td>
      <td id="T_5c1a5_row1_col1" class="data row1 col1" >新等</td>
      <td id="T_5c1a5_row1_col2" class="data row1 col2" >신등</td>
      <td id="T_5c1a5_row1_col3" class="data row1 col3" >陽田</td>
      <td id="T_5c1a5_row1_col4" class="data row1 col4" >양전</td>
      <td id="T_5c1a5_row1_col5" class="data row1 col5" >權福成</td>
      <td id="T_5c1a5_row1_col6" class="data row1 col6" >권복성</td>
      <td id="T_5c1a5_row1_col7" class="data row1 col7" >妻</td>
      <td id="T_5c1a5_row1_col8" class="data row1 col8" >처</td>
      <td id="T_5c1a5_row1_col9" class="data row1 col9" ></td>
      <td id="T_5c1a5_row1_col10" class="data row1 col10" ></td>
      <td id="T_5c1a5_row1_col11" class="data row1 col11" >河</td>
      <td id="T_5c1a5_row1_col12" class="data row1 col12" >氏</td>
      <td id="T_5c1a5_row1_col13" class="data row1 col13" >하</td>
      <td id="T_5c1a5_row1_col14" class="data row1 col14" >씨</td>
      <td id="T_5c1a5_row1_col15" class="data row1 col15" >49.0</td>
      <td id="T_5c1a5_row1_col16" class="data row1 col16" >己酉</td>
      <td id="T_5c1a5_row1_col17" class="data row1 col17" >기유</td>
      <td id="T_5c1a5_row1_col18" class="data row1 col18" ></td>
      <td id="T_5c1a5_row1_col19" class="data row1 col19" ></td>
      <td id="T_5c1a5_row1_col20" class="data row1 col20" ></td>
      <td id="T_5c1a5_row1_col21" class="data row1 col21" ></td>
      <td id="T_5c1a5_row1_col22" class="data row1 col22" ></td>
      <td id="T_5c1a5_row1_col23" class="data row1 col23" ></td>
      <td id="T_5c1a5_row1_col24" class="data row1 col24" >本</td>
      <td id="T_5c1a5_row1_col25" class="data row1 col25" >晉州</td>
      <td id="T_5c1a5_row1_col26" class="data row1 col26" >본</td>
      <td id="T_5c1a5_row1_col27" class="data row1 col27" >진주</td>
      <td id="T_5c1a5_row1_col28" class="data row1 col28" ></td>
      <td id="T_5c1a5_row1_col29" class="data row1 col29" ></td>
      <td id="T_5c1a5_row1_col30" class="data row1 col30" ></td>
      <td id="T_5c1a5_row1_col31" class="data row1 col31" ></td>
      <td id="T_5c1a5_row1_col32" class="data row1 col32" ></td>
      <td id="T_5c1a5_row1_col33" class="data row1 col33" ></td>
      <td id="T_5c1a5_row1_col34" class="data row1 col34" >學生</td>
      <td id="T_5c1a5_row1_col35" class="data row1 col35" >학생</td>
      <td id="T_5c1a5_row1_col36" class="data row1 col36" >應斗</td>
      <td id="T_5c1a5_row1_col37" class="data row1 col37" >응두</td>
      <td id="T_5c1a5_row1_col38" class="data row1 col38" ></td>
      <td id="T_5c1a5_row1_col39" class="data row1 col39" ></td>
      <td id="T_5c1a5_row1_col40" class="data row1 col40" ></td>
      <td id="T_5c1a5_row1_col41" class="data row1 col41" ></td>
      <td id="T_5c1a5_row1_col42" class="data row1 col42" ></td>
      <td id="T_5c1a5_row1_col43" class="data row1 col43" >學生</td>
      <td id="T_5c1a5_row1_col44" class="data row1 col44" >학생</td>
      <td id="T_5c1a5_row1_col45" class="data row1 col45" >潤益</td>
      <td id="T_5c1a5_row1_col46" class="data row1 col46" >윤익</td>
      <td id="T_5c1a5_row1_col47" class="data row1 col47" >學生</td>
      <td id="T_5c1a5_row1_col48" class="data row1 col48" >학생</td>
      <td id="T_5c1a5_row1_col49" class="data row1 col49" >涑</td>
      <td id="T_5c1a5_row1_col50" class="data row1 col50" >속</td>
      <td id="T_5c1a5_row1_col51" class="data row1 col51" >學生</td>
      <td id="T_5c1a5_row1_col52" class="data row1 col52" >학생</td>
      <td id="T_5c1a5_row1_col53" class="data row1 col53" >辛桂復</td>
      <td id="T_5c1a5_row1_col54" class="data row1 col54" >신계복</td>
    </tr>
    <tr>
      <th id="T_5c1a5_level0_row2" class="row_heading level0 row2" >232241</th>
      <td id="T_5c1a5_row2_col0" class="data row2 col0" >1837</td>
      <td id="T_5c1a5_row2_col1" class="data row2 col1" >新等</td>
      <td id="T_5c1a5_row2_col2" class="data row2 col2" >신등</td>
      <td id="T_5c1a5_row2_col3" class="data row2 col3" >陽田</td>
      <td id="T_5c1a5_row2_col4" class="data row2 col4" >양전</td>
      <td id="T_5c1a5_row2_col5" class="data row2 col5" >權福成</td>
      <td id="T_5c1a5_row2_col6" class="data row2 col6" >권복성</td>
      <td id="T_5c1a5_row2_col7" class="data row2 col7" >子</td>
      <td id="T_5c1a5_row2_col8" class="data row2 col8" >자</td>
      <td id="T_5c1a5_row2_col9" class="data row2 col9" ></td>
      <td id="T_5c1a5_row2_col10" class="data row2 col10" ></td>
      <td id="T_5c1a5_row2_col11" class="data row2 col11" >權</td>
      <td id="T_5c1a5_row2_col12" class="data row2 col12" >翼平</td>
      <td id="T_5c1a5_row2_col13" class="data row2 col13" >권</td>
      <td id="T_5c1a5_row2_col14" class="data row2 col14" >익평</td>
      <td id="T_5c1a5_row2_col15" class="data row2 col15" >28.0</td>
      <td id="T_5c1a5_row2_col16" class="data row2 col16" >庚午</td>
      <td id="T_5c1a5_row2_col17" class="data row2 col17" >경오</td>
      <td id="T_5c1a5_row2_col18" class="data row2 col18" ></td>
      <td id="T_5c1a5_row2_col19" class="data row2 col19" ></td>
      <td id="T_5c1a5_row2_col20" class="data row2 col20" ></td>
      <td id="T_5c1a5_row2_col21" class="data row2 col21" ></td>
      <td id="T_5c1a5_row2_col22" class="data row2 col22" ></td>
      <td id="T_5c1a5_row2_col23" class="data row2 col23" ></td>
      <td id="T_5c1a5_row2_col24" class="data row2 col24" ></td>
      <td id="T_5c1a5_row2_col25" class="data row2 col25" ></td>
      <td id="T_5c1a5_row2_col26" class="data row2 col26" ></td>
      <td id="T_5c1a5_row2_col27" class="data row2 col27" ></td>
      <td id="T_5c1a5_row2_col28" class="data row2 col28" ></td>
      <td id="T_5c1a5_row2_col29" class="data row2 col29" ></td>
      <td id="T_5c1a5_row2_col30" class="data row2 col30" ></td>
      <td id="T_5c1a5_row2_col31" class="data row2 col31" ></td>
      <td id="T_5c1a5_row2_col32" class="data row2 col32" ></td>
      <td id="T_5c1a5_row2_col33" class="data row2 col33" ></td>
      <td id="T_5c1a5_row2_col34" class="data row2 col34" ></td>
      <td id="T_5c1a5_row2_col35" class="data row2 col35" ></td>
      <td id="T_5c1a5_row2_col36" class="data row2 col36" ></td>
      <td id="T_5c1a5_row2_col37" class="data row2 col37" ></td>
      <td id="T_5c1a5_row2_col38" class="data row2 col38" ></td>
      <td id="T_5c1a5_row2_col39" class="data row2 col39" ></td>
      <td id="T_5c1a5_row2_col40" class="data row2 col40" ></td>
      <td id="T_5c1a5_row2_col41" class="data row2 col41" ></td>
      <td id="T_5c1a5_row2_col42" class="data row2 col42" ></td>
      <td id="T_5c1a5_row2_col43" class="data row2 col43" ></td>
      <td id="T_5c1a5_row2_col44" class="data row2 col44" ></td>
      <td id="T_5c1a5_row2_col45" class="data row2 col45" ></td>
      <td id="T_5c1a5_row2_col46" class="data row2 col46" ></td>
      <td id="T_5c1a5_row2_col47" class="data row2 col47" ></td>
      <td id="T_5c1a5_row2_col48" class="data row2 col48" ></td>
      <td id="T_5c1a5_row2_col49" class="data row2 col49" ></td>
      <td id="T_5c1a5_row2_col50" class="data row2 col50" ></td>
      <td id="T_5c1a5_row2_col51" class="data row2 col51" ></td>
      <td id="T_5c1a5_row2_col52" class="data row2 col52" ></td>
      <td id="T_5c1a5_row2_col53" class="data row2 col53" ></td>
      <td id="T_5c1a5_row2_col54" class="data row2 col54" ></td>
    </tr>
    <tr>
      <th id="T_5c1a5_level0_row3" class="row_heading level0 row3" >232242</th>
      <td id="T_5c1a5_row3_col0" class="data row3 col0" >1837</td>
      <td id="T_5c1a5_row3_col1" class="data row3 col1" >新等</td>
      <td id="T_5c1a5_row3_col2" class="data row3 col2" >신등</td>
      <td id="T_5c1a5_row3_col3" class="data row3 col3" >陽田</td>
      <td id="T_5c1a5_row3_col4" class="data row3 col4" >양전</td>
      <td id="T_5c1a5_row3_col5" class="data row3 col5" >權福成</td>
      <td id="T_5c1a5_row3_col6" class="data row3 col6" >권복성</td>
      <td id="T_5c1a5_row3_col7" class="data row3 col7" >婦</td>
      <td id="T_5c1a5_row3_col8" class="data row3 col8" >부</td>
      <td id="T_5c1a5_row3_col9" class="data row3 col9" ></td>
      <td id="T_5c1a5_row3_col10" class="data row3 col10" ></td>
      <td id="T_5c1a5_row3_col11" class="data row3 col11" >河</td>
      <td id="T_5c1a5_row3_col12" class="data row3 col12" >氏</td>
      <td id="T_5c1a5_row3_col13" class="data row3 col13" >하</td>
      <td id="T_5c1a5_row3_col14" class="data row3 col14" >씨</td>
      <td id="T_5c1a5_row3_col15" class="data row3 col15" >29.0</td>
      <td id="T_5c1a5_row3_col16" class="data row3 col16" >己巳</td>
      <td id="T_5c1a5_row3_col17" class="data row3 col17" >기사</td>
      <td id="T_5c1a5_row3_col18" class="data row3 col18" ></td>
      <td id="T_5c1a5_row3_col19" class="data row3 col19" ></td>
      <td id="T_5c1a5_row3_col20" class="data row3 col20" ></td>
      <td id="T_5c1a5_row3_col21" class="data row3 col21" ></td>
      <td id="T_5c1a5_row3_col22" class="data row3 col22" ></td>
      <td id="T_5c1a5_row3_col23" class="data row3 col23" ></td>
      <td id="T_5c1a5_row3_col24" class="data row3 col24" >本</td>
      <td id="T_5c1a5_row3_col25" class="data row3 col25" >晉州</td>
      <td id="T_5c1a5_row3_col26" class="data row3 col26" >본</td>
      <td id="T_5c1a5_row3_col27" class="data row3 col27" >진주</td>
      <td id="T_5c1a5_row3_col28" class="data row3 col28" ></td>
      <td id="T_5c1a5_row3_col29" class="data row3 col29" ></td>
      <td id="T_5c1a5_row3_col30" class="data row3 col30" ></td>
      <td id="T_5c1a5_row3_col31" class="data row3 col31" ></td>
      <td id="T_5c1a5_row3_col32" class="data row3 col32" ></td>
      <td id="T_5c1a5_row3_col33" class="data row3 col33" ></td>
      <td id="T_5c1a5_row3_col34" class="data row3 col34" ></td>
      <td id="T_5c1a5_row3_col35" class="data row3 col35" ></td>
      <td id="T_5c1a5_row3_col36" class="data row3 col36" ></td>
      <td id="T_5c1a5_row3_col37" class="data row3 col37" ></td>
      <td id="T_5c1a5_row3_col38" class="data row3 col38" ></td>
      <td id="T_5c1a5_row3_col39" class="data row3 col39" ></td>
      <td id="T_5c1a5_row3_col40" class="data row3 col40" ></td>
      <td id="T_5c1a5_row3_col41" class="data row3 col41" ></td>
      <td id="T_5c1a5_row3_col42" class="data row3 col42" ></td>
      <td id="T_5c1a5_row3_col43" class="data row3 col43" ></td>
      <td id="T_5c1a5_row3_col44" class="data row3 col44" ></td>
      <td id="T_5c1a5_row3_col45" class="data row3 col45" ></td>
      <td id="T_5c1a5_row3_col46" class="data row3 col46" ></td>
      <td id="T_5c1a5_row3_col47" class="data row3 col47" ></td>
      <td id="T_5c1a5_row3_col48" class="data row3 col48" ></td>
      <td id="T_5c1a5_row3_col49" class="data row3 col49" ></td>
      <td id="T_5c1a5_row3_col50" class="data row3 col50" ></td>
      <td id="T_5c1a5_row3_col51" class="data row3 col51" ></td>
      <td id="T_5c1a5_row3_col52" class="data row3 col52" ></td>
      <td id="T_5c1a5_row3_col53" class="data row3 col53" ></td>
      <td id="T_5c1a5_row3_col54" class="data row3 col54" ></td>
    </tr>
    <tr>
      <th id="T_5c1a5_level0_row4" class="row_heading level0 row4" >232243</th>
      <td id="T_5c1a5_row4_col0" class="data row4 col0" >1837</td>
      <td id="T_5c1a5_row4_col1" class="data row4 col1" >新等</td>
      <td id="T_5c1a5_row4_col2" class="data row4 col2" >신등</td>
      <td id="T_5c1a5_row4_col3" class="data row4 col3" >陽田</td>
      <td id="T_5c1a5_row4_col4" class="data row4 col4" >양전</td>
      <td id="T_5c1a5_row4_col5" class="data row4 col5" >權福成</td>
      <td id="T_5c1a5_row4_col6" class="data row4 col6" >권복성</td>
      <td id="T_5c1a5_row4_col7" class="data row4 col7" >奴婢</td>
      <td id="T_5c1a5_row4_col8" class="data row4 col8" >노비</td>
      <td id="T_5c1a5_row4_col9" class="data row4 col9" >婢</td>
      <td id="T_5c1a5_row4_col10" class="data row4 col10" >비</td>
      <td id="T_5c1a5_row4_col11" class="data row4 col11" ></td>
      <td id="T_5c1a5_row4_col12" class="data row4 col12" >長守</td>
      <td id="T_5c1a5_row4_col13" class="data row4 col13" ></td>
      <td id="T_5c1a5_row4_col14" class="data row4 col14" >장수</td>
      <td id="T_5c1a5_row4_col15" class="data row4 col15" ></td>
      <td id="T_5c1a5_row4_col16" class="data row4 col16" ></td>
      <td id="T_5c1a5_row4_col17" class="data row4 col17" ></td>
      <td id="T_5c1a5_row4_col18" class="data row4 col18" >逃</td>
      <td id="T_5c1a5_row4_col19" class="data row4 col19" ></td>
      <td id="T_5c1a5_row4_col20" class="data row4 col20" >도</td>
      <td id="T_5c1a5_row4_col21" class="data row4 col21" ></td>
      <td id="T_5c1a5_row4_col22" class="data row4 col22" ></td>
      <td id="T_5c1a5_row4_col23" class="data row4 col23" ></td>
      <td id="T_5c1a5_row4_col24" class="data row4 col24" ></td>
      <td id="T_5c1a5_row4_col25" class="data row4 col25" ></td>
      <td id="T_5c1a5_row4_col26" class="data row4 col26" ></td>
      <td id="T_5c1a5_row4_col27" class="data row4 col27" ></td>
      <td id="T_5c1a5_row4_col28" class="data row4 col28" ></td>
      <td id="T_5c1a5_row4_col29" class="data row4 col29" ></td>
      <td id="T_5c1a5_row4_col30" class="data row4 col30" ></td>
      <td id="T_5c1a5_row4_col31" class="data row4 col31" ></td>
      <td id="T_5c1a5_row4_col32" class="data row4 col32" ></td>
      <td id="T_5c1a5_row4_col33" class="data row4 col33" ></td>
      <td id="T_5c1a5_row4_col34" class="data row4 col34" ></td>
      <td id="T_5c1a5_row4_col35" class="data row4 col35" ></td>
      <td id="T_5c1a5_row4_col36" class="data row4 col36" ></td>
      <td id="T_5c1a5_row4_col37" class="data row4 col37" ></td>
      <td id="T_5c1a5_row4_col38" class="data row4 col38" ></td>
      <td id="T_5c1a5_row4_col39" class="data row4 col39" ></td>
      <td id="T_5c1a5_row4_col40" class="data row4 col40" ></td>
      <td id="T_5c1a5_row4_col41" class="data row4 col41" ></td>
      <td id="T_5c1a5_row4_col42" class="data row4 col42" ></td>
      <td id="T_5c1a5_row4_col43" class="data row4 col43" ></td>
      <td id="T_5c1a5_row4_col44" class="data row4 col44" ></td>
      <td id="T_5c1a5_row4_col45" class="data row4 col45" ></td>
      <td id="T_5c1a5_row4_col46" class="data row4 col46" ></td>
      <td id="T_5c1a5_row4_col47" class="data row4 col47" ></td>
      <td id="T_5c1a5_row4_col48" class="data row4 col48" ></td>
      <td id="T_5c1a5_row4_col49" class="data row4 col49" ></td>
      <td id="T_5c1a5_row4_col50" class="data row4 col50" ></td>
      <td id="T_5c1a5_row4_col51" class="data row4 col51" ></td>
      <td id="T_5c1a5_row4_col52" class="data row4 col52" ></td>
      <td id="T_5c1a5_row4_col53" class="data row4 col53" ></td>
      <td id="T_5c1a5_row4_col54" class="data row4 col54" ></td>
    </tr>
  </tbody>
</table>

## About the name
* Why snowyseoul?
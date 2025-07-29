import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('부산강서고 여름방학 파이썬 보충')

st.write('hello, 강서고등학교')

df = pd.DataFrame({
    '첫번째 칼럼' : [1, 2, 3, 4],
    '두 번째 칼럼' : [10, 20, 30, 40]
})

st.write(df)

st.write('아래는 DataFrame입니다. ', df, '위는 dataframe입니다. ')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip= ['a', 'b', 'c']
)

st.write(c)
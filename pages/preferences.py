
import streamlit as st

# 1. session_state에 'user_data'가 존재하는지 확인하고, 없으면 빈 딕셔너리로 초기화
if 'user_data' not in st.session_state:
    st.session_state.user_data = {} 
    # 또는 st.session_state['user_data'] = {'preferences': []} 처럼 기본값을 주어도 좋습니다.

# 2. 기존에 작성하셨던 코드 (이제 미리 초기화되었으므로 에러가 나지 않습니다!)
user_prefs = st.session_state.user_data.get('preferences', [])
st.title('선호도 설정')

# 같은 세션 상태에 접근
preferences = st.multiselect(
    '관심 분야를 선택하세요', 
    ['데이터 과학', '웹 개발', '모바일 앱', '게임 개발'],
    st.session_state.user_data.get('preferences', [])
)

st.session_state.user_data['preferences'] = preferences
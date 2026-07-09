import streamlit as st

st.set_page_config(page_title='streamlit 실습', page_icon='💻', layout='wide')

st.sidebar.title('📆강의 일정')
st.sidebar.caption('날짜를 클릭하면 그날의 실습/과제 화면으로 이동합니다')

selected_day = st.sidebar.radio(
     '날짜를 입력하세요',
    [
        '1일차 : 7월 6일(월)',
        '2일차 : 7월 7일(화)',
        '3일차 : 7월 8일(수)',
        '4일차 : 7월 9일(목)',
        '5일차 : 7월 10일(금)',
    ],
)

st.title(selected_day)
st.divider()

tab_practice, tab_assignment1, tab_assignment2 = st.tabs(['실습','과제1','과제2'])

if selected_day == '1일차 : 7월 6일(월)':
    with tab_practice:
        st.header('1일차 실습예제')
        st.title("나의 첫 번째 웹앱")

        st.write("VSCode, uv, Streamlit을 이용해서 만든 웹앱입니다.")

        name = st.text_input("이름을 입력하세요", key="name1")

        if name:
            st.success(f"{name}님, 반갑습니다!")

        age1 = st.slider("나이를 선택하세요", 0, 100, 0, key='age1')

        st.write(f"선택한 나이는 {age1}세입니다.")

        st.header("관심 분야 선택")
        interest = st.selectbox(
            "관심 있는 분야를 선택하세요",
            ["인공지능", "데이터분석", "웹앱 개발", "디지털 리터러시"]
        )
        st.write(f"선택한 관심 분야는 {interest}입니다.")

        st.write("---")
        st.title('자기소개')
        st.header('기본 정보')
        st.subheader('취미')
        st.write('저는 축구를 좋아합니다.')
        st.write("---")
        if st.button('인사하기'):
            st.write('안녕하세요!')

        st.write("---")
        st.success('성공했습니다!')
        st.info('안내 메시지입니다.')
        st.warning('주의하세요!')
        st.error('오류가 발생했습니다.')
        st.write("---")
        import random
        luck=['대박','행운','평범','조심','최고']
        if st.button('운세 보기'):
            st.write(random.choice(luck))

        st.write("---") 
        #st.image('images/그림1.png')
        st.video('https://www.youtube.com/watch?v=xxxx')

        st.write("---")
        name2 = st.text_input('이름을 입력하세요', key='name2')
        if name2:
            st.write(f'{name2}님, 환영합니다!')

        age2 = st.number_input('나이', min_value=0, max_value=100, key='age2')
        st.write('내년 나이:', age2+1)

        st.write("---")
        score = st.slider('집중도', 0, 100, 50)
        st.write('현재 집중도:', score)

        st.write("---")
        subject = st.selectbox('좋아하는 과목', ['국어','수학','영어','정보'])
        st.write('선택:', subject)

        st.write("---")
        menu = st.radio('점심 메뉴', ['김밥','라면','돈가스'])
        st.write(menu, '선택!')

        st.write("---")
        if st.checkbox('축구','야구', '배구'):
            st.write('축구를 좋아합니다!')

        items = ["인공지능", "데이터분석", "웹앱 개발", "디지털 리터러시"]

        selected_items = []

        for item in items:
            checked = st.checkbox(item)
            if checked:
                selected_items.append(item)

        st.subheader("선택한 항목")

        if selected_items:
            st.write(selected_items)
        else:
            st.write("아직 선택한 항목이 없습니다.")
            
        st.write("---")
        score = st.number_input('점수', 0, 100)
        if score >= 60:
            st.success('합격')
        else:
            st.warning('다시 도전')

        st.write("---")
        name3=st.text_input('이름', key='name3')
        age3=st.number_input('나이',0,100, key='age3')
        field3=st.selectbox('관심분야',['AI','게임','디자인'], key='field3')
        st.write(name3, age3, field3)

        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            st.write('왼쪽')
        with col2:
            st.write('오른쪽')

        st.write("---")
        menu = st.sidebar.selectbox('메뉴', ['홈','분석','설정'])
        st.write('선택한 메뉴:', menu)

        st.write("---")
        tab1, tab2 = st.tabs(['소개','실습'])
        with tab1:
            st.write('소개 화면')
        with tab2:
            st.write('실습 화면')


        st.write("---")
        if 'count' not in st.session_state:
            st.session_state.count = 0
            if st.button('증가'):
                st.session_state.count += 1
                st.write(st.session_state.count)

    with tab_assignment1:
        st.header('1일차 실습과제1')
        st.set_page_config(page_title="나의 프로필 & 오늘의 명언", page_icon="✨", layout="wide")
 
        quotes = [
            ("시작이 반이다.", "아리스토텔레스"),
            ("천 리 길도 한 걸음부터.", "한국 속담"),
            ("가장 큰 위험은 위험 없는 삶이다.", "작자 미상"),
            ("우흥 북딱 흔들어라.", "벤저민 프랭클린"),
            ("실패는 성공으로 가는 과정일 뿐이다.", "토마스 에디슨"),
            ("배움에 있어 늦은 때는 없다.", "작자 미상"),
            ("작은 습관이 큰 변화를 만든다.", "제임스 클리어"),
        ]
        
        if "quote_index" not in st.session_state:
            st.session_state.quote_index = random.randrange(len(quotes))
        
        st.title("나의 프로필 & 오늘의 명언")
        st.write("")
        
        col_profile, col_quote = st.columns(2)
        
        with col_profile:
            st.header("내 프로필")
            st.subheader("김규민")
            st.write("고등학교 2학년, 미래의 개발자")
            st.write("관심사: 게임, 음악, 파이썬, 디저트")
            st.info("위 이름과 소개, 관심사를 자기 것으로 바꿔보세요.")
        
        with col_quote:
            st.header("오늘의 명언")
            quote_text, quote_author = quotes[st.session_state.quote_index]
            st.success(quote_text)
            st.write(f"말한 사람: {quote_author}")
        
            if st.button("다른 명언 보기"):
                st.session_state.quote_index = random.randrange(len(quotes))
                st.rerun()

    with tab_assignment2:
        st.header('1일차 실습과제2')
        st.set_page_config(page_title="BMI 계산기", page_icon="⚖️", layout="wide")
        
        st.title("BMI 계산기")
        st.write("키와 몸무게를 입력하고 버튼을 눌러 체질량지수(BMI)를 확인해보세요.")
        st.divider()
        
        col_input, col_result = st.columns(2)
        
        with col_input:
            st.header("정보 입력")
            height_cm = st.slider("키 (cm)", min_value=100, max_value=220, value=165)
            weight_kg = st.slider("몸무게 (kg)", min_value=30, max_value=150, value=55)
            calculate = st.button("BMI 계산하기")
        
        with col_result:
            st.header("결과")
        
            if calculate:
                height_m = height_cm / 100
                bmi = weight_kg / (height_m ** 2)
        
                # 대한비만학회(KSSO) 기준: 저체중 <18.5 / 정상 18.5~22.9 / 과체중 23~24.9 / 비만 25 이상
                if bmi < 18.5:
                    category = "저체중"
                elif bmi < 23:
                    category = "정상 체중"
                elif bmi < 25:
                    category = "과체중"
                else:
                    category = "비만"
        
                st.metric(label="나의 BMI", value=f"{bmi:.1f}", delta=category, delta_color="off")
        
                # BMI 값을 0.0~1.0 사이 진행률로 환산 (15~35 범위를 기준으로)
                scale_min, scale_max = 15, 35
                progress_value = max(0.0, min(1.0, (bmi - scale_min) / (scale_max - scale_min)))
                st.progress(progress_value, text=f"저체중 ← BMI {bmi:.1f} → 비만")
        
                if category == "저체중":
                    st.info("표준 체중보다 가벼운 편입니다. 균형 잡힌 식사가 도움이 될 수 있어요.")
                elif category == "정상 체중":
                    st.success("건강한 범위의 체중입니다. 지금처럼 잘 유지해보세요.")
                elif category == "과체중":
                    st.warning("표준보다 조금 높은 편입니다. 꾸준한 활동이 도움이 될 수 있어요.")
                else:
                    st.error("전문가와 상담을 통해 건강 관리 계획을 세워보는 것을 권장합니다.")
        
                st.caption(
                    "이 결과는 대한비만학회 성인 기준을 적용한 참고용 계산입니다. "
                    "성장기 청소년은 나이·성별별 성장도표(퍼센타일)를 함께 보는 것이 더 정확합니다.")
            else:
                st.info("왼쪽에서 키와 몸무게를 입력하고 'BMI 계산하기' 버튼을 눌러주세요.")

elif selected_day == '2일차 : 7월 7일(화)':

    with tab_practice:
        st.header('2일차 실습예제')
        import re
        from streamlit_mic_recorder import speech_to_text
        from gtts import gTTS
        from io import BytesIO

        def classify_bmi(bmi: float) -> tuple[str, str, str]:
            """대한비만학회(아시아-태평양) 기준 BMI 분류
            반환: (분류명, 이모지, 건강정보 안내문)
            """
            if bmi < 18.5:
                return ("저체중", "🟦",
                        "체중이 표준보다 적은 상태입니다. 단백질과 탄수화물을 골고루 갖춘 "
                        "규칙적인 식사를 하고, 근육량을 늘리는 가벼운 근력 운동을 권장합니다. "
                        "급격한 체중 감소가 있었다면 병원 진료를 받아보세요.")
            elif bmi < 23:
                return ("정상", "🟩",
                        "건강한 체중 범위입니다. 지금의 식습관과 활동량을 잘 유지하세요. "
                        "주 3회 이상, 30분 이상의 유산소 운동을 꾸준히 하면 "
                        "현재의 건강 상태를 오래 지킬 수 있습니다.")
            elif bmi < 25:
                return ("과체중", "🟨",
                        "정상 범위를 조금 넘어선 상태입니다. 야식과 당분 섭취를 줄이고, "
                        "걷기·자전거 같은 유산소 운동을 주 4회 이상 실천해 보세요. "
                        "지금 관리하면 비만으로의 진행을 충분히 막을 수 있습니다.")
            elif bmi < 30:
                return ("비만 1단계", "🟧",
                        "체중 조절이 필요한 단계입니다. 식사량을 조금 줄이고 "
                        "규칙적인 운동을 병행하면 개선할 수 있습니다. 고혈압, 당뇨 등 "
                        "동반 질환 여부를 확인하기 위해 건강검진을 권장합니다.")
            else:
                return ("비만 2단계 이상", "🟥",
                        "적극적인 체중 관리가 필요한 단계입니다. 혼자 하기보다는 "
                        "의사, 영양사 등 전문가와 상담하여 체계적인 계획을 세우는 것이 "
                        "안전하고 효과적입니다. 가까운 병원이나 보건소를 방문해 보세요.")

        def speak(text: str) -> BytesIO:
            """텍스트를 한국어 음성(mp3 바이트)으로 변환"""
            tts = gTTS(text=text, lang="ko")
            buf = BytesIO()
            tts.write_to_fp(buf)
            buf.seek(0)
            return buf

        text = "마이크 버튼을 누르고 키와 몸무게를 말하면, BMI와 건강정보를 음성으로 알려드립니다."
        if st.button("🎵 음성 BMI 건강 도우미 클릭"):
            audio = speak(text)
            st.audio(audio, format="audio/mp3", autoplay=True)

        # if st.button("🎵 음성 BMI 건강 도우미"):
        #     tts = gTTS(text=text, lang='ko')     # 한국어 설정
        #     audio_bytes = BytesIO()               # 파일 저장 없이 메모리에서 처리
        #     tts.write_to_fp(audio_bytes)
        #     audio_bytes.seek(0)
        #     st.audio(audio_bytes, format='audio/mp3')   # 재생 플레이어 표시


        st.write("마이크 버튼을 누르고 키를 숫자를 말해보세요. 예: '삼십오' 또는 '35'")

        # 1단계: 음성 → 텍스트 (한국어 설정: language='ko')
        height_text = speech_to_text(
            language='ko',              # 한국어 인식
            start_prompt="🎙️ 녹음 시작",
            stop_prompt="⏹️ 녹음 종료",
            just_once=True,             # 한 번 인식 후 초기화
            use_container_width=True,
            key='stt1'
        )

        # 2단계: 텍스트 → 숫자 추출
        if height_text:
            st.info(f"인식된 말: **{height_text}**")
            numbers = re.findall(r'\d+\.?\d*', height_text)   # 아라비아 숫자 추출
            if numbers:
                height_value = float(numbers[0])
                st.success(f"✅ 입력된 숫자: **{height_value}**")
                st.session_state.height = height_value
                #st.session_state['voice_number'] = height_value
            else:
                st.warning("⚠️ 숫자를 찾지 못했어요. '35'처럼 또박또박 말해보세요.")

        # 3단계: 입력받은 숫자를 위젯에 반영
        # default = st.session_state.get('voice_number', 0.0)
        # num = st.number_input("확인/수정", value=default)

        st.write("마이크 버튼을 누르고 몸무게를 숫자를 말해보세요. 예: '칠십오' 또는 '75'")

        # 1단계: 음성 → 텍스트 (한국어 설정: language='ko')
        weight_text = speech_to_text(
            language='ko',              # 한국어 인식
            start_prompt="🎙️ 녹음 시작",
            stop_prompt="⏹️ 녹음 종료",
            just_once=True,             # 한 번 인식 후 초기화
            use_container_width=True,
            key='stt2'
        )

        # 2단계: 텍스트 → 숫자 추출
        if weight_text:
            st.info(f"인식된 말: **{weight_text}**")
            numbers = re.findall(r'\d+\.?\d*', weight_text)   # 아라비아 숫자 추출
            if numbers:
                weight_value = float(numbers[0])
                st.success(f"✅ 입력된 숫자: **{weight_value}**")
                st.session_state.weight = weight_value
                #st.session_state['voice_number'] = weight_value
            else:
                st.warning("⚠️ 숫자를 찾지 못했어요. '75'처럼 또박또박 말해보세요.")


        if st.button("🧮 BMI 계산하고 음성으로 듣기", use_container_width=True, type="primary"):
            height = st.number_input(
                "키 (cm)", min_value=0.0, max_value=250.0,
                value=float(st.session_state.height or 0.0), step=0.1,
            )
            weight = st.number_input(
                "몸무게 (kg)", min_value=0.0, max_value=300.0,
                value=float(st.session_state.weight or 0.0), step=0.1
            )

            if height <= 0 or weight <= 0:
                st.warning("⚠️ 키와 몸무게를 먼저 입력해 주세요.")
            else:
                bmi = weight / ((height / 100) ** 2)
                category, emoji, advice = classify_bmi(bmi)
        
                # 화면 표시
                st.metric(label="당신의 BMI", value=f"{bmi:.1f}", delta=category)
                st.markdown(f"### {emoji} 판정: **{category}**")
                st.info(advice)


                message = (
                    f"측정 결과를 알려드립니다. 키 {height:.0f} 센티미터, "
                    f"몸무게 {weight:.0f} 킬로그램으로, "
                    f"비엠아이 수치는 {bmi:.1f} 입니다. {category}에 해당합니다. {advice}"
                )
                with st.spinner("음성을 생성하는 중..."):
                    audio = speak(message)
                st.audio(audio, format="audio/mp3")
                st.caption("▶️ 재생 버튼을 눌러 결과를 들어보세요.")

    with tab_assignment1:
        st.header('2일차 실습과제1')
        st.subheader("고등학생 진로/학습 AI 챗봇")
        st.write(
            "궁금한 진로, 공부법, 고민을 편하게 물어보세요! (Google **Gemini API** 사용 — "
            "결제수단 등록 없이 무료로 발급받은 키로 바로 테스트할 수 있어요.)"
        )
    
        with st.sidebar:
            st.markdown("### 🔑 Day5 챗봇 설정 (Gemini)")
            api_key = st.text_input(
                "Gemini API Key",
                type="password",
                value="",
                help="https://aistudio.google.com/apikey 에서 Google 계정으로 로그인 후 무료 발급. "
                    "키는 서버에 저장되지 않고 이 세션에서만 사용됩니다.",
            )
            model_name = st.selectbox(
                "모델 선택",
                ["gemini-2.5-flash", "gemini-2.5-flash-lite"],
                help="Flash / Flash-Lite 계열은 무료 티어(RPM/RPD 한도 내)에서 사용할 수 있는 모델입니다.",
            )
            persona = st.selectbox(
                "챗봇 성격 선택",
                ["친절한 진로상담 선생님", "논리적인 스터디 코치", "유머러스한 친구 같은 챗봇"],
            )
            if st.button("Day5 대화 초기화 🔄"):
                st.session_state.day5_chat_messages = []
                st.session_state.pop("day5_gemini_chat", None)
                st.session_state.pop("day5_gemini_chat_key", None)
                st.rerun()
    
        persona_prompts = {
            "친절한 진로상담 선생님": (
                "당신은 따뜻하고 친절한 고등학교 진로상담 선생님입니다. "
                "학생의 눈높이에 맞춰 쉽고 구체적으로, 격려하는 말투로 답변하세요."
            ),
            "논리적인 스터디 코치": (
                "당신은 체계적이고 논리적인 학습 코치입니다. "
                "학생의 질문에 단계별로, 근거를 들어 명확하게 답변하세요."
            ),
            "유머러스한 친구 같은 챗봇": (
                "당신은 학생과 친구처럼 편하게 대화하는 유쾌한 챗봇입니다. "
                "가볍고 재미있는 말투를 쓰되, 유용한 정보는 정확히 전달하세요."
            ),
        }
    
        if "day5_chat_messages" not in st.session_state:
            st.session_state.day5_chat_messages = []
    
        for msg in st.session_state.day5_chat_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    
        prompt = st.chat_input("궁금한 것을 물어보세요!", key="day5_chat_input")
    
        if prompt:
            if not api_key:
                st.error("먼저 사이드바에 Gemini API Key를 입력해주세요! 🔑 (https://aistudio.google.com/apikey)")
                st.stop()
    
            st.session_state.day5_chat_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
    
            try:
                from google import genai
                from google.genai import types
    
                # 모델/페르소나가 바뀌면 채팅 세션을 새로 만들고, 그렇지 않으면 기존 세션(대화 맥락)을 재사용
                chat_key = f"{model_name}::{persona}"
                if st.session_state.get("day5_gemini_chat_key") != chat_key:
                    client = genai.Client(api_key=api_key)
                    st.session_state.day5_gemini_chat = client.chats.create(
                        model=model_name,
                        config=types.GenerateContentConfig(
                            system_instruction=persona_prompts[persona],
                        ),
                    )
                    st.session_state.day5_gemini_chat_key = chat_key
    
                chat = st.session_state.day5_gemini_chat
    
                with st.chat_message("assistant"):
                    placeholder = st.empty()
                    full_response = ""
                    for chunk in chat.send_message_stream(prompt):
                        if chunk.text:
                            full_response += chunk.text
                            placeholder.markdown(full_response + "▌")
                    placeholder.markdown(full_response)
    
                st.session_state.day5_chat_messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"오류가 발생했어요: {e}")

    with tab_assignment2:
                st.header('2일차 실습과제2')


elif selected_day == '3일차 : 7월 8일(수)':

    with tab_practice:
                st.header('3일차 실습예제')
    import random
    import base64
    from io import BytesIO
    from PIL import Image
    import streamlit.components.v1 as components
    
    st.set_page_config(page_title="가위바위보 대결 앱", page_icon="✂️", layout="wide")
    
    st.title("✂️🪨📄 가위바위보 대결 앱")
    
    CHOICES = ["가위", "바위", "보"]
    EMOJI = {"가위": "✂️", "바위": "🪨", "보": "📄"}
    
    # 가위바위보 승패 규칙: key가 이기는 대상은 value
    BEATS = {"가위": "보", "바위": "가위", "보": "바위"}
    
    
    def judge(player: str, computer: str) -> str:
        """플레이어 기준 결과 문자열 반환"""
        if player == computer:
            return "무승부"
        elif BEATS[player] == computer:
            return "승리"
        else:
            return "패배"
    
    
    tab_basic, tab_ai = st.tabs(["🖐️ 기본 모드 (버튼으로 대결)", "🤖 AI 인식 모드 (Teachable Machine 연동)"])
    
    # =========================================================================
    # 1) 기본 모드 - 버튼 클릭으로 컴퓨터와 대결, session_state로 누적 점수 기록
    # =========================================================================
    with tab_basic:
        st.subheader("버튼을 눌러 컴퓨터와 대결하세요!")
    
        if "score" not in st.session_state:
            st.session_state.score = {"승리": 0, "패배": 0, "무승부": 0}
        if "history" not in st.session_state:
            st.session_state.history = []
    
        col1, col2, col3 = st.columns(3)
        player_choice = None
        if col1.button("✂️ 가위", use_container_width=True):
            player_choice = "가위"
        if col2.button("🪨 바위", use_container_width=True):
            player_choice = "바위"
        if col3.button("📄 보", use_container_width=True):
            player_choice = "보"
    
        if player_choice:
            computer_choice = random.choice(CHOICES)
            result = judge(player_choice, computer_choice)
            st.session_state.score[result] += 1
            st.session_state.history.insert(
                0, {"내 선택": f"{EMOJI[player_choice]} {player_choice}",
                    "컴퓨터 선택": f"{EMOJI[computer_choice]} {computer_choice}",
                    "결과": result}
            )
    
            result_msg = {"승리": "🎉 이겼습니다!", "패배": "😢 졌습니다!", "무승부": "🤝 비겼습니다!"}
            st.markdown(f"## {EMOJI[player_choice]} VS {EMOJI[computer_choice]}")
            if result == "승리":
                st.success(result_msg[result])
            elif result == "패배":
                st.error(result_msg[result])
            else:
                st.warning(result_msg[result])
    
        st.markdown("---")
        s1, s2, s3 = st.columns(3)
        s1.metric("🎉 승리", st.session_state.score["승리"])
        s2.metric("😢 패배", st.session_state.score["패배"])
        s3.metric("🤝 무승부", st.session_state.score["무승부"])
    
        if st.button("🔄 점수 초기화"):
            st.session_state.score = {"승리": 0, "패배": 0, "무승부": 0}
            st.session_state.history = []
            st.rerun()
    
        if st.session_state.history:
            with st.expander("📋 대결 기록 보기"):
                st.table(st.session_state.history)
    
    # =========================================================================
    # 2) AI 인식 모드 - Teachable Machine 모델로 손 모양 사진을 인식해서 대결
    # =========================================================================
    with tab_ai:
        st.subheader("손 모양 사진을 올리면 AI가 가위/바위/보를 인식해서 대결합니다")
        st.write(
            "먼저 Teachable Machine에서 **가위 / 바위 / 보** 3개 클래스로 직접 학습시킨 모델을 "
            "`Export Model → Upload(Shareable link)`로 게시하고, 그 URL을 아래에 입력하세요."
        )
    
        model_url = st.text_input(
            "Teachable Machine 모델 URL",
            value="https://teachablemachine.withgoogle.com/models/pc8DpzFoM/",
            placeholder="https://teachablemachine.withgoogle.com/models/xxxxxxxx/",
            key="rps_model_url",
        )
    
        input_method = st.radio(
            "손 모양을 어떻게 입력할까요?",
            ["📸 카메라로 바로 찍기 (폰 추천)", "📁 파일 업로드"],
            horizontal=True,
            key="rps_input_method",
        )
    
        if input_method.startswith("📸"):
            st.caption("폰이라면 버튼을 누르는 순간 카메라가 열리고, 촬영하자마자 바로 아래에 결과가 나타나요.")
            uploaded_hand = st.camera_input("가위/바위/보 손 모양을 촬영하세요", key="rps_camera")
        else:
            uploaded_hand = st.file_uploader("손 모양 사진 업로드", type=["png", "jpg", "jpeg"], key="rps_upload")
    
        if model_url and uploaded_hand:
            if not model_url.endswith("/"):
                model_url += "/"
    
            image = Image.open(uploaded_hand).convert("RGB")
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_data_url = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()
    
            # 컴퓨터의 선택을 미리 정해서 JS 쪽에 함께 넘겨줍니다.
            computer_choice_ai = random.choice(CHOICES)
    
            col_left, col_right = st.columns([1, 1.4])
            with col_left:
                st.image(image, caption="업로드한 손 모양", use_container_width=True)
                st.info(f"컴퓨터의 선택: {EMOJI[computer_choice_ai]} {computer_choice_ai} (공개는 결과와 함께!)")
    
            with col_right:
                html_code = """
                <div style="font-family:-apple-system, sans-serif;">
                <div id="status" style="color:#555; margin-bottom:10px;">AI가 손 모양을 분석 중입니다... ⏳</div>
                <img id="predict-image" src="__IMG_DATA_URL__" style="display:none;" crossorigin="anonymous" />
                <div id="result-box" style="font-size:18px;"></div>
                <div id="label-container" style="margin-top:14px;"></div>
                </div>
    
                <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.20.0/dist/tf.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@0.8.5/dist/teachablemachine-image.min.js"></script>
                <script type="text/javascript">
                const URL_BASE = "__MODEL_URL__";
                const COMPUTER_CHOICE = "__COMPUTER_CHOICE__";
                const BEATS = { "가위": "보", "바위": "가위", "보": "바위",
                                "scissors": "paper", "rock": "scissors", "paper": "rock" };
                const KOR = { "scissors": "가위", "rock": "바위", "paper": "보" };
                const EMOJI = { "가위": "✂️", "바위": "🪨", "보": "📄",
                                "scissors": "✂️", "rock": "🪨", "paper": "📄" };
    
                function normalize(label) {
                    const trimmed = label.trim();
                    return KOR[trimmed.toLowerCase()] || trimmed;
                }
    
                function renderBar(className, prob) {
                    const pct = (prob * 100).toFixed(1);
                    return `<div style="margin-bottom:6px;">
                            <div style="display:flex; justify-content:space-between; font-size:13px;">
                                <span>${className}</span><span>${pct}%</span>
                            </div>
                            <div style="background:#eee; border-radius:6px; height:10px;">
                                <div style="background:#4C8BF5; width:${pct}%; height:10px; border-radius:6px;"></div>
                            </div>
                            </div>`;
                }
    
                async function init() {
                    const statusEl = document.getElementById("status");
                    try {
                    const model = await tmImage.load(URL_BASE + "model.json", URL_BASE + "metadata.json");
                    statusEl.innerText = "분석 중입니다... 🔍";
    
                    const imgEl = document.getElementById("predict-image");
                    imgEl.onload = async () => {
                        const predictions = await model.predict(imgEl);
                        predictions.sort((a, b) => b.probability - a.probability);
    
                        let html = "";
                        predictions.forEach((p) => { html += renderBar(p.className, p.probability); });
                        document.getElementById("label-container").innerHTML = html;
    
                        const rawTop = predictions[0].className;
                        const player = normalize(rawTop);
                        statusEl.innerHTML = `✅ AI가 인식한 내 손 모양: <b>${EMOJI[player] || ""} ${player}</b>`;
    
                        const resultBox = document.getElementById("result-box");
                        if (BEATS[player] === undefined) {
                        resultBox.innerHTML =
                            "⚠️ 클래스 이름이 '가위/바위/보' 또는 'scissors/rock/paper'와 일치하지 않아 승패를 판정할 수 없어요.";
                        return;
                        }
    
                        let outcome;
                        if (player === COMPUTER_CHOICE) outcome = "🤝 무승부입니다!";
                        else if (BEATS[player] === COMPUTER_CHOICE) outcome = "🎉 승리했습니다!";
                        else outcome = "😢 패배했습니다!";
    
                        resultBox.innerHTML =
                        `<h3>${EMOJI[player] || ""} VS ${EMOJI[COMPUTER_CHOICE]} ${COMPUTER_CHOICE}</h3>` +
                        `<p style="font-size:20px;">${outcome}</p>`;
                    };
                    if (imgEl.complete) imgEl.onload();
                    } catch (err) {
                    statusEl.innerHTML =
                        "❌ 모델을 불러오지 못했습니다. 모델 URL과 클래스 이름을 확인해주세요.<br><small>" + err + "</small>";
                    }
                }
                init();
                </script>
                """
                html_code = (
                    html_code
                    .replace("__IMG_DATA_URL__", img_data_url)
                    .replace("__MODEL_URL__", model_url)
                    .replace("__COMPUTER_CHOICE__", computer_choice_ai)
                )
                components.html(html_code, height=430, scrolling=True)
        else:
            st.info("모델 URL과 손 모양 사진을 모두 입력하면 여기에서 AI 대결 결과가 표시됩니다.")

    with tab_assignment1:
                st.header('3일차 실습과제1')

    with tab_assignment2:
                st.header('3일차 실습과제2')


elif selected_day == '4일차 : 7월 9일(목)':
    with tab_practice:
                st.header('4일차 실습과제')

    with tab_assignment1:
                st.header('4일차 실습과제1')

    with tab_assignment2:
                st.header('4일차 실습과제2')


elif selected_day == '5일차 : 7월 10(금)':
    with tab_practice:
                st.header('5일차 실습과제')

    with tab_assignment1:
                st.header('5일차 실습과제')

    with tab_assignment2:
                st.header('5일차 실습과제2')


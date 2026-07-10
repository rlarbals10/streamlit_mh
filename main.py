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
                st.header('4일차 실습예제')
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    
    st.set_page_config(page_title="ML 모델 데모 (sklearn)", layout="wide")
    
    st.markdown("## 08-05. ML 모델 데모 (sklearn)")
    st.info("분류/회귀 모델을 학습하고 입력값으로 즉시 예측해보는 데모 앱입니다.")
    
    AUTHOR_NAME = "에드윈"
    
    
    @st.cache_resource
    def load_model():
        iris = load_iris()
        X, y = iris.data, iris.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
        return model, iris, acc
    
    
    model, iris, accuracy = load_model()
    feature_names_kr = ["Sepal length (cm)", "Sepal width (cm)", "Petal length (cm)", "Petal width (cm)"]
    target_names_kr = {"setosa": "세토사", "versicolor": "베르시컬러", "virginica": "버지니카"}
    species_order = ["virginica", "versicolor", "setosa"]
    
    st.markdown("### 🤖 ML 모델 데모 — Iris 분류")
    st.caption(f"sklearn RandomForestClassifier · 정확도 {accuracy*100:.1f}% · 작성: {AUTHOR_NAME}")
    
    col_input, col_result = st.columns(2)
    
    with col_input:
        st.markdown("#### 입력 특성")
        sepal_length = st.slider(feature_names_kr[0], 4.3, 7.9, 5.8, 0.1)
        sepal_width = st.slider(feature_names_kr[1], 2.0, 4.4, 3.0, 0.1)
        petal_length = st.slider(feature_names_kr[2], 1.0, 6.9, 4.4, 0.1)
        petal_width = st.slider(feature_names_kr[3], 0.1, 2.5, 1.3, 0.1)
        predict_clicked = st.button("🔍 예측", use_container_width=True, type="primary")
    
        input_df = pd.DataFrame(
            [[sepal_length, sepal_width, petal_length, petal_width]],
            columns=iris.feature_names,
        )
        proba = model.predict_proba(input_df)[0]
        pred_idx = int(np.argmax(proba))
        pred_species = iris.target_names[pred_idx]
        pred_proba_pct = proba[pred_idx] * 100
    
    with col_result:
        st.markdown("#### 예측 결과")
    
        fig1, ax1 = plt.subplots(figsize=(5, 2.2))
        values = [proba[list(iris.target_names).index(sp)] * 100 for sp in species_order]
        colors = ["#e57373" if sp == pred_species else "#f8c9c9" for sp in species_order]
        bars = ax1.barh(species_order, values, color=colors, height=0.6)
        for bar, v in zip(bars, values):
            ax1.text(v + 2, bar.get_y() + bar.get_height() / 2, f"{v:.0f}%", va="center", fontsize=9)
        ax1.set_xlim(0, 100)
        ax1.spines[["top", "right", "left"]].set_visible(False)
        ax1.tick_params(left=False)
        ax1.set_xlabel("")
        fig1.tight_layout()
        st.pyplot(fig1)
    
        st.success(
            f"🌸 {pred_species} ({target_names_kr[pred_species]} · 확률 {pred_proba_pct:.0f}%) — "
            f"{target_names_kr[pred_species]} 종으로 분류"
        )
    
    st.markdown("#### 특성 중요도")
    importances = model.feature_importances_
    order = np.argsort(importances)
    sorted_feats = [feature_names_kr[i].split(" (")[0] for i in order]
    sorted_vals = importances[order]
    
    fig2, ax2 = plt.subplots(figsize=(9, 2.5))
    ax2.barh(sorted_feats, sorted_vals, color="#2e7d32", height=0.55)
    ax2.set_xlim(0, max(sorted_vals) * 1.2)
    ax2.spines[["top", "right"]].set_visible(False)
    fig2.tight_layout()
    st.pyplot(fig2)

    with tab_assignment1:
                st.header('4일차 실습과제1')

    with tab_assignment2:
                st.header('4일차 실습과제2')


elif selected_day == '5일차 : 7월 10일(금)':
    with tab_practice:
                st.header('5일차 실습예제')
                import math
                import time
                import requests
                import pandas as pd
                import streamlit as st
                import folium
                from folium.plugins import AntPath
                from streamlit_folium import st_folium
                from streamlit_js_eval import get_geolocation
                from streamlit_autorefresh import st_autorefresh
                
                # ----------------------------------------------------------------------------
                # 0. 기본 설정
                # ----------------------------------------------------------------------------
                st.set_page_config(page_title="창원시 누비자 가까운 대여소 찾기", page_icon="🚲", layout="wide")
                
                CHANGWON_CENTER = (35.2280, 128.6811)  # 창원시청 근처 좌표 (GPS를 못 받았을 때 기본값)
                DATA_PATH = "data/nubija_stations.xlsx"  # 창원시 제공 실제 누비자 터미널 데이터(2025.12.31 기준, 372곳)
                NEAREST_N = 5  # 가까운 대여소를 몇 개까지 보여줄지
                
                
                # ----------------------------------------------------------------------------
                # 1. 대여소 데이터 불러오기
                #    - 실제 수업/서비스에서는 공공데이터포털에서 내려받은
                #      "경상남도 창원시_누비자 터미널" 파일(XLSX)을 그대로 올리면 된다.
                #    - 컬럼 이름이 파일마다 조금씩 다를 수 있어서, 아래 매핑표로 흡수한다.
                # ----------------------------------------------------------------------------
                # 행정안전부 "전국자전거대여소표준데이터" - 전국 지자체 공영자전거 대여소를 표준 형식으로 모아 제공.
                # 요청주소가 고정되어 있어서, 사용자는 인증키만 발급받으면 된다.
                NUBIJA_OPENAPI_BASE_URL = "https://api.data.go.kr/openapi/tn_pubr_public_bcycl_lend_api"
                
                COLUMN_ALIASES = {
                    "name": ["대여소명", "터미널명", "정류장명", "station_name", "name", "자전거대여소명"],
                    "lat": ["위도", "lat", "latitude", "Y좌표"],
                    "lon": ["경도", "lon", "lng", "longitude", "X좌표"],
                    "address": ["주소", "소재지", "address", "소재지도로명주소", "소재지지번주소"],
                    "capacity": ["거치대수", "보관대수", "정원", "capacity"],
                    "org": ["관리기관명", "org"],  # 어느 지자체가 관리하는 대여소인지 (전국 데이터에서 창원만 걸러낼 때 사용)
                    "status": ["사용유무", "status"],  # 실제 창원시 데이터의 운영 상태(사용함/사용안함)
                }
                
                
                def _find_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
                    for c in candidates:
                        if c in df.columns:
                            return c
                    return None
                
                
                def _standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
                    rename_map = {}
                    for std_col, aliases in COLUMN_ALIASES.items():
                        found = _find_column(df, aliases)
                        if found:
                            rename_map[found] = std_col
                    df = df.rename(columns=rename_map)
                
                    required = {"name", "lat", "lon"}
                    missing = required - set(df.columns)
                    if missing:
                        raise ValueError(f"필수 컬럼이 없습니다: {missing} (대여소명/위도/경도에 해당하는 열이 있는지 확인하세요)")
                
                    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
                    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
                    df = df.dropna(subset=["lat", "lon"]).reset_index(drop=True)
                
                    # 창원시 실제 데이터에는 '사용유무' 컬럼이 있어서, 폐쇄된(사용안함) 대여소는 기본적으로 제외한다.
                    if "status" in df.columns:
                        before = len(df)
                        df = df[~df["status"].astype(str).str.contains("안함|폐쇄|중지", na=False)].reset_index(drop=True)
                        removed = before - len(df)
                        if removed > 0:
                            st.caption(f"운영 중지된 대여소 {removed}곳은 목록에서 제외했습니다.")
                
                    return df
                
                
                @st.cache_data(show_spinner="공공데이터포털 OpenAPI에서 대여소 정보를 받아오는 중...")
                def load_stations_from_openapi(service_key: str, org_keyword: str = "창원", page_size: int = 1000) -> pd.DataFrame:
                    """행정안전부 '전국자전거대여소표준데이터' OpenAPI를 호출해서
                    관리기관명에 org_keyword(기본값 '창원')가 포함된 대여소만 걸러서 돌려준다.
                    요청주소는 고정되어 있으므로 사용자는 인증키(service_key)만 입력하면 된다.
                    """
                    all_rows: list[dict] = []
                    page_no = 1
                    while True:
                        params = {
                            "serviceKey": service_key,
                            "pageNo": page_no,
                            "numOfRows": page_size,
                            "type": "json",
                        }
                        res = requests.get(NUBIJA_OPENAPI_BASE_URL, params=params, timeout=10)
                        res.raise_for_status()
                        payload = res.json()
                
                        # 공공데이터포털 응답 구조는 대개 response.body.items.item 형태이지만,
                        # 기관마다 조금씩 달라서 여러 경로를 순서대로 시도한다.
                        items = (
                            payload.get("response", {}).get("body", {}).get("items", {}).get("item")
                            or payload.get("body", {}).get("items")
                            or payload.get("items")
                        )
                        if not items:
                            break
                        if isinstance(items, dict):
                            items = [items]
                
                        all_rows.extend(items)
                        if len(items) < page_size:
                            break
                        page_no += 1
                        if page_no > 30:  # 안전장치: 무한루프 방지 (전국 데이터라 페이지가 많을 수 있음)
                            break
                
                    if not all_rows:
                        raise ValueError("OpenAPI 응답에서 데이터를 찾지 못했습니다. 인증키가 올바른지, 승인이 완료됐는지 확인해주세요.")
                
                    df = pd.DataFrame(all_rows)
                    df = _standardize_columns(df)
                
                    if "org" in df.columns and org_keyword:
                        filtered = df[df["org"].astype(str).str.contains(org_keyword, na=False)]
                        if len(filtered) > 0:
                            df = filtered
                        else:
                            st.warning(f"관리기관명에 '{org_keyword}'가 포함된 대여소를 찾지 못해 전체 데이터를 보여드립니다.")
                
                    return df.reset_index(drop=True)
                
                
                @st.cache_data(show_spinner=False)
                def load_stations(uploaded_bytes: bytes | None, uploaded_name: str | None) -> pd.DataFrame:
                    """업로드된 파일이 있으면 그것을, 없으면 샘플 데이터를 읽어서
                    name / lat / lon / address / capacity 라는 표준 컬럼으로 통일해서 돌려준다."""
                    if uploaded_bytes is not None:
                        if uploaded_name.endswith(".xlsx"):
                            df = pd.read_excel(uploaded_bytes)
                        else:
                            df = pd.read_csv(uploaded_bytes)
                    else:
                        df = pd.read_excel(DATA_PATH)
                
                    return _standardize_columns(df)
                
                
                # ----------------------------------------------------------------------------
                # 2. 거리 계산 - 하버사인(Haversine) 공식
                #    지구는 평평한 종이가 아니라 둥근 공이기 때문에,
                #    두 좌표 사이의 실제 거리를 재려면 구면 위의 거리 공식을 써야 한다.
                # ----------------------------------------------------------------------------
                def haversine_m(lat1, lon1, lat2, lon2) -> float:
                    R = 6371000  # 지구 반지름(m)
                    p1, p2 = math.radians(lat1), math.radians(lat2)
                    dphi = math.radians(lat2 - lat1)
                    dlambda = math.radians(lon2 - lon1)
                    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2) ** 2
                    return 2 * R * math.asin(math.sqrt(a))
                
                
                # ----------------------------------------------------------------------------
                # 3. OSRM 보행자 경로 API 호출
                #    무료 공개 데모 서버라서 수업용 데모에는 충분하지만,
                #    실서비스라면 자체 서버를 두거나 카카오/티맵 API로 바꾸는 것을 권장한다.
                # ----------------------------------------------------------------------------
                @st.cache_data(show_spinner=False, ttl=300)
                def get_walking_route(start_lat, start_lon, end_lat, end_lon):
                    url = (
                        f"https://router.project-osrm.org/route/v1/foot/"
                        f"{start_lon},{start_lat};{end_lon},{end_lat}"
                        f"?overview=full&geometries=geojson"
                    )
                    res = requests.get(url, timeout=6)
                    res.raise_for_status()
                    data = res.json()
                    if data.get("code") != "Ok":
                        return None
                    route = data["routes"][0]
                    coords = [(lat, lon) for lon, lat in route["geometry"]["coordinates"]]
                    return {
                        "coords": coords,
                        "distance_m": route["distance"],
                        "duration_s": route["duration"],
                    }
                
                
                # ----------------------------------------------------------------------------
                # 3-1. Tmap 보행자 경로안내 API - 인도/횡단보도/육교/지하보도/계단을 구분해서 안내
                #    OSRM은 도로망 데이터를 그대로 따라가서 "차도를 걷는 것"처럼 보이지만,
                #    Tmap 보행자 API는 실제 인도(보도) 폴리곤 데이터를 갖고 있어서
                #    "인도로 걷다가, 정해진 횡단보도에서만 차도를 건너는" 형태로 경로를 만들어준다.
                # ----------------------------------------------------------------------------
                TMAP_PEDESTRIAN_URL = "https://apis.openapi.sk.com/tmap/routes/pedestrian"
                
                # 구간 종류별 표시 스타일 (지도에 그릴 때 사용)
                SEGMENT_STYLE = {
                    "sidewalk":   {"color": "#2ECC71", "label": "인도 · 보행로", "dash": None},
                    "crosswalk":  {"color": "#E74C3C", "label": "횡단보도(차도 횡단)", "dash": "1,8"},
                    "overpass":   {"color": "#7F8C8D", "label": "육교", "dash": "6,4"},
                    "underpass":  {"color": "#7F8C8D", "label": "지하보도", "dash": "6,4"},
                    "stairs":     {"color": "#8E44AD", "label": "계단", "dash": "2,6"},
                    "bike":       {"color": "#3498DB", "label": "자전거도로", "dash": "8,4"},
                }
                
                
                def _classify_segment(props: dict) -> str:
                    """Tmap 응답의 텍스트 속성을 보고 이 구간이 인도인지 횡단보도인지 등을 판별한다."""
                    text = " ".join(str(props.get(k, "")) for k in ("facilityName", "description", "name", "roadName"))
                    if "횡단보도" in text:
                        return "crosswalk"
                    if "지하보도" in text or "지하차도" in text:
                        return "underpass"
                    if "육교" in text:
                        return "overpass"
                    if "계단" in text:
                        return "stairs"
                    if "자전거" in text:
                        return "bike"
                    return "sidewalk"
                
                
                @st.cache_data(show_spinner=False, ttl=300)
                def get_walking_route_tmap(app_key: str, start_lat, start_lon, end_lat, end_lon):
                    """Tmap 보행자 경로안내 API를 호출해서, 인도/횡단보도 등으로 구분된 구간 리스트를 돌려준다."""
                    # 복사/붙여넣기 과정에서 앞뒤 공백이나 줄바꿈이 섞여 들어오면
                    # requests가 "Invalid leading whitespace..." 에러를 내므로 여기서 한 번 더 정리한다.
                    app_key = (app_key or "").strip()
                    if not app_key:
                        raise ValueError("Tmap appKey가 비어 있습니다.")
                
                    headers = {
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "appKey": app_key,
                    }
                    body = {
                        "startX": start_lon, "startY": start_lat,
                        "endX": end_lon, "endY": end_lat,
                        "startName": "출발", "endName": "도착",
                        "reqCoordType": "WGS84GEO", "resCoordType": "WGS84GEO",
                        "searchOption": "0",  # 0: 추천(최단시간) 경로
                    }
                    res = requests.post(f"{TMAP_PEDESTRIAN_URL}?version=1", headers=headers, json=body, timeout=8)
                    res.raise_for_status()
                    data = res.json()
                
                    features = data.get("features")
                    if not features:
                        # 인증키 오류 등으로 실패하면 Tmap이 {"error": {...}} 형태로 응답한다.
                        err = data.get("error", {}).get("message", "알 수 없는 오류")
                        raise ValueError(f"Tmap 응답 오류: {err}")
                
                    total_distance, total_time = None, None
                    segments = []
                    for f in features:
                        props = f.get("properties", {})
                        geom = f.get("geometry", {})
                        if geom.get("type") == "Point" and props.get("pointIndex") == 0:
                            total_distance = props.get("totalDistance")
                            total_time = props.get("totalTime")
                        elif geom.get("type") == "LineString":
                            coords = [(lat, lon) for lon, lat in geom["coordinates"]]
                            segments.append({
                                "coords": coords,
                                "type": _classify_segment(props),
                                "distance": props.get("distance", 0) or 0,
                            })
                
                    if not segments:
                        return None
                    if total_distance is None:
                        total_distance = sum(s["distance"] for s in segments)
                
                    return {"segments": segments, "distance_m": total_distance, "duration_s": total_time or 0}
                
                
                # ----------------------------------------------------------------------------
                # 4. 화면 구성 시작
                # ----------------------------------------------------------------------------
                st.title("🚲 창원시 누비자 - 내 주변 가까운 대여소 찾기")
                st.caption("현재 위치 기준으로 가까운 누비자 대여소를 찾고, 선택한 대여소까지 걸어가는 경로를 실시간으로 지도에 표시합니다.")
                
                # session_state 초기값 준비
                # - target: 사용자가 "경로 보기"로 확정한 목적지(대여소). 목록 정렬이 바뀌어도 유지된다.
                # - tracking: 실시간 위치 추적 on/off
                # - trail: 지금까지 실제로 이동한 GPS 좌표 기록 (걸어온 길을 보여주기 위함)
                if "target" not in st.session_state:
                    st.session_state.target = None
                if "tracking" not in st.session_state:
                    st.session_state.tracking = False
                if "trail" not in st.session_state:
                    st.session_state.trail = []
                
                with st.sidebar:
                    st.header("⚙️ 설정")
                
                    data_source = st.radio(
                        "대여소 데이터를 어떻게 불러올까요?",
                        ["창원시 실제 데이터 (기본 제공, 342곳)", "파일 업로드 (최신 XLSX/CSV로 교체)", "공공데이터포털 OpenAPI 자동 연동"],
                    )
                
                    uploaded = None
                    api_service_key, api_org_filter = "", "창원"
                
                    if data_source == "파일 업로드 (최신 XLSX/CSV로 교체)":
                        uploaded = st.file_uploader(
                            "누비자 대여소 XLSX/CSV 업로드",
                            type=["xlsx", "csv"],
                        )
                    elif data_source == "공공데이터포털 OpenAPI 자동 연동":
                        st.caption(
                            "행정안전부 '전국자전거대여소표준데이터'를 사용합니다. "
                            "요청주소는 이미 앱에 내장되어 있으니, 인증키만 입력하면 됩니다.\n\n"
                            "1) data.go.kr 회원가입 → '전국자전거대여소표준데이터' 검색 → 활용신청\n"
                            "2) 마이페이지 > API 키 발급/관리 에서 '인증키(디코딩)' 복사 → 아래에 붙여넣기"
                        )
                        # secrets.toml에 저장해두면 자동으로 채워지고, 없으면 직접 입력한다.
                        default_key = st.secrets.get("DATA_GO_KR_SERVICE_KEY", "")
                        api_service_key = st.text_input(
                            "서비스 인증키 (디코딩 키)", value=default_key, type="password"
                        ).strip()
                        api_org_filter = st.text_input("관리기관명 필터", value="창원", help="전국 데이터 중 이 글자가 포함된 기관만 보여줍니다.")
                        fetch_clicked = st.button("🔄 OpenAPI에서 불러오기", use_container_width=True)
                
                    n_show = st.slider("가까운 대여소 몇 개를 볼까요?", 3, 10, NEAREST_N)
                
                    st.markdown("---")
                    st.subheader("🚏 경로 안내 방식")
                    routing_engine = st.radio(
                        "인도/차도를 구분해서 보고 싶다면 Tmap을 선택하세요",
                        ["OSRM (기본, 무료, 인도·차도 구분 없음)", "Tmap 보행자 API (인도·횡단보도·계단 등 구분)"],
                    )
                    tmap_app_key = ""
                    if routing_engine.startswith("Tmap"):
                        st.caption(
                            "Tmap 보행자 API는 실제 인도(보도) 데이터를 사용해서, 인도로 걷다가 "
                            "지정된 횡단보도에서만 차도를 건너는 형태로 경로를 안내합니다.\n\n"
                            "1) https://tmapapi.tmapmobility.com 가입 → 앱 등록(무료)\n"
                            "2) 마이페이지 > 앱 관리에서 발급된 appKey 복사 → 아래에 붙여넣기"
                        )
                        default_tmap_key = st.secrets.get("TMAP_APP_KEY", "")
                        tmap_app_key = st.text_input(
                            "Tmap appKey", value=default_tmap_key, type="password"
                        ).strip()
                
                    st.markdown("---")
                    st.subheader("📡 실시간 위치 추적")
                    st.session_state.tracking = st.toggle(
                        "실시간 추적 켜기 (걸어가면서 확인)",
                        value=st.session_state.tracking,
                        help="켜두면 5초마다 GPS를 다시 읽어와서 내 위치와 남은 경로를 자동으로 갱신합니다.",
                    )
                    if st.session_state.tracking:
                        refresh_interval = st.slider("갱신 주기(초)", 3, 15, 5)
                    st.markdown("---")
                    st.markdown(
                        "데이터 출처: [공공데이터포털 - 경상남도 창원시_누비자 터미널]"
                        "(https://www.data.go.kr/data/15000545/fileData.do)"
                    )
                
                # 추적이 켜져 있으면 지정한 주기마다 스크립트를 자동으로 다시 실행시킨다.
                # (이 tick 값이 바뀔 때마다 아래 get_geolocation()의 key도 바뀌어서, 캐시된 옛 위치가 아니라
                #  브라우저에게 "GPS 다시 읽어줘"라고 매번 새로 요청하게 된다.)
                if st.session_state.tracking:
                    tick = st_autorefresh(interval=refresh_interval * 1000, key="gps_autorefresh")
                else:
                    tick = 0
                
                try:
                    if data_source == "공공데이터포털 OpenAPI 자동 연동":
                        if not api_service_key:
                            st.info("왼쪽에 인증키를 입력하고 '불러오기'를 눌러주세요. 입력 전까지는 기본 데이터로 보여드립니다.")
                            stations_df = load_stations(None, None)
                        elif fetch_clicked or "openapi_df" in st.session_state:
                            if fetch_clicked:
                                st.session_state["openapi_df"] = load_stations_from_openapi(api_service_key, api_org_filter)
                            stations_df = st.session_state["openapi_df"]
                        else:
                            stations_df = load_stations(None, None)
                    else:
                        stations_df = load_stations(
                            uploaded.getvalue() if uploaded else None,
                            uploaded.name if uploaded else None,
                        )
                except Exception as e:
                    st.error(f"데이터를 불러오는 중 문제가 발생했습니다: {e}")
                    st.stop()
                
                st.info(f"불러온 대여소 개수: {len(stations_df)}개", icon="📍")
                
                # ----------------------------------------------------------------------------
                # 5. 현재 위치 가져오기 (브라우저 GPS)
                #    tick 값을 key에 섞어주면, 추적이 켜져 있는 동안 자동새로고침 때마다
                #    "새 위치를 다시 물어봐" 라는 의미가 되어 실시간처럼 동작한다.
                # ----------------------------------------------------------------------------
                loc = get_geolocation(component_key=f"geo_{tick}")
                
                if loc is None:
                    st.warning("브라우저에 위치 접근 권한을 허용해주세요. 권한 창이 뜨지 않으면 새로고침(F5) 해보세요.")
                    st.stop()
                
                if "error" in loc:
                    st.error(f"위치를 가져오지 못했습니다: {loc['error'].get('message', '알 수 없는 오류')}")
                    st.stop()
                
                my_lat = loc["coords"]["latitude"]
                my_lon = loc["coords"]["longitude"]
                
                # 실제로 걸어온 흔적(trail) 기록 - 직전 위치와 눈에 띄게 다를 때만 追加해서 GPS 흔들림 노이즈를 줄인다.
                if not st.session_state.trail or haversine_m(*st.session_state.trail[-1], my_lat, my_lon) > 3:
                    st.session_state.trail.append((my_lat, my_lon))
                
                st.success(f"현재 위치: 위도 {my_lat:.5f}, 경도 {my_lon:.5f}" + (f"  🔴 실시간 추적 중 (tick {tick})" if st.session_state.tracking else ""))
                
                # ----------------------------------------------------------------------------
                # 6. 가까운 대여소 N개 계산
                # ----------------------------------------------------------------------------
                stations_df = stations_df.copy()
                stations_df["distance_m"] = stations_df.apply(
                    lambda r: haversine_m(my_lat, my_lon, r["lat"], r["lon"]), axis=1
                )
                nearest = stations_df.sort_values("distance_m").head(n_show).reset_index(drop=True)
                
                col_list, col_map = st.columns([1, 2])
                
                with col_list:
                    st.subheader("가까운 대여소 목록")
                    # 라디오 버튼의 key를 station name(고유값)으로 고정해서, 거리 숫자가 바뀌어도
                    # 매번 새로운 위젯으로 취급되어 선택이 풀리는 문제를 막는다.
                    name_list = nearest["name"].tolist()
                    dist_map = dict(zip(nearest["name"], nearest["distance_m"]))
                    choice_name = st.radio(
                        "대여소를 선택하세요",
                        name_list,
                        format_func=lambda n: f"{n}  ({dist_map[n]:.0f}m)",
                        key="station_radio",
                    )
                    selected = nearest[nearest["name"] == choice_name].iloc[0]
                
                    st.metric("직선 거리", f"{selected['distance_m']:.0f} m")
                    if "address" in selected and pd.notna(selected.get("address")):
                        st.write(f"📮 주소: {selected['address']}")
                    if "capacity" in selected and pd.notna(selected.get("capacity")):
                        st.write(f"🚲 거치대수: {int(selected['capacity'])}대")
                
                    col_a, col_b = st.columns(2)
                    if col_a.button("🗺️ 이 대여소로 경로 시작", use_container_width=True):
                        # 목적지를 session_state에 "고정"해둔다. 이렇게 해야 다음 자동새로고침/재실행에서도
                        # 경로가 사라지지 않고 계속 표시된다. (이전 버전의 '깜빡였다 사라지는' 문제의 원인 수정)
                        st.session_state.target = {
                            "name": selected["name"],
                            "lat": float(selected["lat"]),
                            "lon": float(selected["lon"]),
                        }
                        st.session_state.trail = [(my_lat, my_lon)]  # 새 목적지를 정하면 이동 흔적도 새로 시작
                    if col_b.button("⏹️ 경로 그만 보기", use_container_width=True):
                        st.session_state.target = None
                        st.session_state.tracking = False
                
                # ----------------------------------------------------------------------------
                # 7. 지도 그리기
                # ----------------------------------------------------------------------------
                with col_map:
                    m = folium.Map(location=[my_lat, my_lon], zoom_start=15)
                
                    folium.Marker(
                        [my_lat, my_lon],
                        tooltip="내 현재 위치",
                        icon=folium.Icon(color="blue", icon="user", prefix="fa"),
                    ).add_to(m)
                
                    for i, row in nearest.iterrows():
                        is_target = st.session_state.target is not None and row["name"] == st.session_state.target["name"]
                        folium.Marker(
                            [row["lat"], row["lon"]],
                            tooltip=f"{row['name']} ({row['distance_m']:.0f}m)",
                            icon=folium.Icon(
                                color="red" if is_target else "green",
                                icon="bicycle",
                                prefix="fa",
                            ),
                        ).add_to(m)
                
                    # 지금까지 실제로 걸어온 흔적 - 옅은 파란 선으로 표시
                    if len(st.session_state.trail) >= 2:
                        folium.PolyLine(
                            st.session_state.trail, color="#3388FF", weight=4, opacity=0.5, dash_array="4"
                        ).add_to(m)
                
                    target = st.session_state.target
                    if target is not None:
                        use_tmap = routing_engine.startswith("Tmap") and bool(tmap_app_key)
                
                        with st.spinner("보행자 경로를 계산하는 중..."):
                            if use_tmap:
                                try:
                                    tmap_result = get_walking_route_tmap(tmap_app_key, my_lat, my_lon, target["lat"], target["lon"])
                                except Exception as e:
                                    st.warning(f"Tmap 경로 요청에 실패해서 OSRM으로 대신 안내합니다: {e}")
                                    tmap_result = None
                                route = None if tmap_result else get_walking_route(my_lat, my_lon, target["lat"], target["lon"])
                            else:
                                tmap_result = None
                                route = get_walking_route(my_lat, my_lon, target["lat"], target["lon"])
                                if routing_engine.startswith("Tmap") and not tmap_app_key:
                                    st.info("Tmap appKey를 입력하면 인도/횡단보도를 구분해서 보여드립니다. 지금은 OSRM으로 안내합니다.")
                
                        if tmap_result is not None:
                            # 구간(인도/횡단보도/계단 등)마다 색을 다르게 그려서 실제로 걷는 길을 구분해서 보여준다.
                            used_types = set()
                            for seg in tmap_result["segments"]:
                                style = SEGMENT_STYLE[seg["type"]]
                                used_types.add(seg["type"])
                                if seg["type"] == "sidewalk":
                                    # 인도 구간만 "흐르는" 애니메이션으로 강조해서 진행 방향을 보여준다.
                                    AntPath(seg["coords"], color=style["color"], weight=6, opacity=0.9, delay=800, dash_array=[10, 20]).add_to(m)
                                else:
                                    folium.PolyLine(
                                        seg["coords"], color=style["color"], weight=6, opacity=0.9,
                                        dash_array=style["dash"],
                                        tooltip=style["label"],
                                    ).add_to(m)
                                    if seg["type"] == "crosswalk":
                                        mid = seg["coords"][len(seg["coords"]) // 2]
                                        folium.Marker(
                                            mid, tooltip="🚦 횡단보도",
                                            icon=folium.DivIcon(html="<div style='font-size:18px'>🚦</div>"),
                                        ).add_to(m)
                
                            legend_html = "  ".join(
                                f"<span style='color:{SEGMENT_STYLE[t]['color']}'>●</span> {SEGMENT_STYLE[t]['label']}"
                                for t in used_types
                            )
                            st.markdown(f"**범례:** {legend_html}", unsafe_allow_html=True)
                
                            minutes = tmap_result["duration_s"] / 60
                            st.success(
                                f"🎯 목적지: {target['name']} · 남은 거리 약 {tmap_result['distance_m']:.0f}m · "
                                f"예상 소요시간 약 {minutes:.1f}분 (Tmap 보행자 경로 · 인도/차도 구분)"
                            )
                            if tmap_result["distance_m"] < 15:
                                st.balloons()
                                st.success("🎉 목적지에 도착했습니다!")
                            bounds = [[my_lat, my_lon], [target["lat"], target["lon"]]]
                            m.fit_bounds(bounds, padding=(30, 30))
                
                        elif route is None:
                            st.error("경로를 찾지 못했습니다. 잠시 후 다시 시도해주세요.")
                        else:
                            # AntPath는 선을 따라 점들이 흐르듯 움직이는 애니메이션 효과를 준다.
                            # -> "실시간으로 경로를 따라 이동하는 느낌"을 시각적으로 표현
                            AntPath(
                                route["coords"],
                                color="#FF5733",
                                weight=6,
                                opacity=0.9,
                                delay=800,
                                dash_array=[10, 20],
                            ).add_to(m)
                
                            minutes = route["duration_s"] / 60
                            st.success(
                                f"🎯 목적지: {target['name']} · 남은 거리 약 {route['distance_m']:.0f}m · "
                                f"예상 소요시간 약 {minutes:.1f}분 (OSRM · 도로망 기준)"
                            )
                            if route["distance_m"] < 15:
                                st.balloons()
                                st.success("🎉 목적지에 도착했습니다!")
                
                            bounds = [[my_lat, my_lon], [target["lat"], target["lon"]]]
                            m.fit_bounds(bounds, padding=(30, 30))
                    else:
                        st.info("왼쪽에서 대여소를 고르고 '이 대여소로 경로 시작'을 누르면 경로가 여기 표시됩니다.")
                
                    # key를 고정해두면 streamlit-folium이 지도 확대/이동 상태를 매 새로고침마다 유지해준다.
                    st_folium(m, height=560, use_container_width=True, key="main_map")
                
                
                st.markdown("---")
                st.caption(
                    "⚠️ OSRM은 무료 공개 데모 서버라서 도로망(차도)을 그대로 따라가는 경로를 줍니다. "
                    "인도·횡단보도·계단까지 구분해서 보고 싶다면 사이드바에서 'Tmap 보행자 API'를 선택하고 "
                    "무료 appKey를 입력하세요.\n\n"
                    "📡 실시간 추적을 켜면 설정한 주기마다 GPS를 다시 읽고 경로를 재계산합니다. "
                    "무료 API 정책상 너무 짧은 주기(1~2초)는 피하고 5초 이상을 권장합니다."
)

    with tab_assignment1:
                st.header('5일차 실습과제')

    with tab_assignment2:
                st.header('5일차 실습과제2')


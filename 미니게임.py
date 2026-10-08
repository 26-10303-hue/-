import streamlit as st
import streamlit.components.v1 as components

# 웹 브라우저 탭 네임 및 기본 설정
st.set_page_config(
    page_title="📖 스마트 학습 & 통합과학2 대방출",
    page_icon="📖",
    layout="centered"
)

if "current_screen" not in st.session_state:
    st.session_state.current_screen = "home"

def set_screen(screen_name):
    st.session_state.current_screen = screen_name

# ==========================================
# 🏠 1. 메인 홈 화면
# ==========================================
if st.session_state.current_screen == "home":
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>📖 스마트 학습 & 통합과학2 대방출 📖</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 16px; color: #bbb;'>통합과학2 전 소단원 완전 정복, 공부 타이머 & 오답노트 통합 스마트 학습 앱</p>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.subheader("🧪 통합과학2 전단원 퀴즈")
        st.write("소단원별 전면 개편! 타이머, 오답노트 기능 지원 및 문제 풀이 시 🪙 코인 보상.")
        st.button("🧪 통합과학2 공부하기", on_click=set_screen, args=("science",), use_container_width=True, type="primary")

    with col2:
        st.subheader("🏎️ 7인 카트 레이싱")
        st.write("10가지 테마 트랙, AI 무작위 동시 출발, 2개 아이템 슬롯 및 최고 기록 저장.")
        st.button("🏎️ 레이싱 플레이", on_click=set_screen, args=("racing",), use_container_width=True)

    with col3:
        st.subheader("🚗 장애물 피하기")
        st.write("횡단보도 도로 연출, 맞은편 차량 추가 & 디테일 실물 구조물 그래픽 적용.")
        st.button("🚗 피하기 플레이", on_click=set_screen, args=("obstacle",), use_container_width=True)

    with col4:
        st.subheader("🧗‍♂️ 건강의 다리")
        st.write("50코인으로 200계단 폭풍 부스터(Z키)! 100단위 가속 시스템 & 기록 저장.")
        st.button("🧗‍♂️ 건강의 다리 플레이", on_click=set_screen, args=("stairs",), use_container_width=True)

# ==========================================
# 🧪 2. 통합과학2 전 소단원 개념, 오답노트 & 공부 타이머
# ==========================================
elif st.session_state.current_screen == "science":
    col_nav1, col_nav2 = st.columns([1, 4])
    with col_nav1:
        st.button("🏠 메인으로", on_click=set_screen, args=("home",), use_container_width=True)
    with col_nav2:
        st.subheader("🧪 통합과학2 전체 소단원 스마트 학습 센터")

    science_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { background-color: #0e1117; color: #fff; font-family: 'Malgun Gothic', sans-serif; padding: 10px; margin: 0; }
            .timer-box { background: #0f172a; border: 2px solid #38bdf8; border-radius: 10px; padding: 12px; margin-bottom: 15px; text-align: center; display: flex; justify-content: space-between; align-items: center; }
            .timer-display { font-size: 24px; font-weight: bold; color: #f1c40f; font-family: monospace; }
            .btn-timer { padding: 6px 14px; font-size: 13px; font-weight: bold; border-radius: 5px; border: none; cursor: pointer; margin-left: 5px; }
            
            .tab-container { display: flex; gap: 4px; }
            .tab-btn { padding: 10px 16px; font-size: 14px; font-weight: bold; background: #1e293b; color: #cbd5e1; border: 1px solid #334155; border-radius: 8px 8px 0 0; cursor: pointer; }
            .tab-btn.active { background: #0284c7; color: #fff; border-color: #38bdf8; }
            .tab-content { background: #1e293b; border: 1px solid #334155; padding: 20px; border-radius: 0 8px 8px 8px; margin-bottom: 20px; }
            
            .concept-box { background: #0f172a; padding: 15px; border-left: 4px solid #38bdf8; border-radius: 6px; margin-bottom: 15px; }
            .concept-title { color: #f1c40f; font-size: 16px; font-weight: bold; margin-bottom: 8px; }
            .sub-title { color: #38bdf8; font-weight: bold; margin-top: 10px; margin-bottom: 4px; }
            
            .quiz-card { background: #0f172a; padding: 20px; border-radius: 10px; border: 1px solid #334155; }
            .question-title { color: #38bdf8; font-size: 16px; font-weight: bold; margin-bottom: 12px; line-height: 1.5; }
            .box-text { background: #1e293b; padding: 12px; border: 1px dashed #64748b; border-radius: 6px; font-size: 14px; margin-bottom: 15px; white-space: pre-line; color: #e2e8f0; }
            .option-item { background: #1e293b; border: 1px solid #334155; padding: 10px 15px; border-radius: 6px; margin-bottom: 8px; cursor: pointer; transition: 0.2s; }
            .option-item:hover { background: #334155; border-color: #38bdf8; }
            .option-item.selected { background: #0369a1; border-color: #38bdf8; font-weight: bold; }
            .btn-action { padding: 10px 20px; font-size: 14px; font-weight: bold; border-radius: 6px; border: none; cursor: pointer; margin-top: 15px; margin-right: 8px; }
            .btn-submit { background: #27ae60; color: white; }
            .btn-next { background: #e67e22; color: white; }
            
            .result-box { margin-top: 15px; padding: 15px; border-radius: 8px; display: none; }
            .result-success { background: rgba(39, 174, 96, 0.2); border: 1px solid #27ae60; color: #2ecc71; }
            .result-fail { background: rgba(231, 76, 60, 0.2); border: 1px solid #e74c3c; color: #e74c3c; }
            
            .wrong-card { background: #0f172a; border: 1px solid #e74c3c; border-radius: 8px; padding: 12px; margin-bottom: 12px; }
        </style>
    </head>
    <body>

    <!-- ⏱️ 공부 타이머 바 -->
    <div class="timer-box">
        <div style="font-weight:bold; color:#cbd5e1;">⏱️ 학습 스톱워치: <span id="timerText" class="timer-display">00:00:00</span></div>
        <div>
            <button class="btn-timer" style="background:#27ae60; color:#fff;" onclick="startTimer()">시작</button>
            <button class="btn-timer" style="background:#e67e22; color:#fff;" onclick="pauseTimer()">일시정지</button>
            <button class="btn-timer" style="background:#7f8c8d; color:#fff;" onclick="resetTimer()">리셋</button>
        </div>
    </div>

    <!-- 탭 버튼 -->
    <div class="tab-container">
        <button class="tab-btn active" id="btnTab1" onclick="switchTab(1)">📚 소단원 개념 요약</button>
        <button class="tab-btn" id="btnTab2" onclick="switchTab(2)">🎲 무한 기출 문제</button>
        <button class="tab-btn" id="btnTab3" onclick="switchTab(3)">📝 오답노트 (<span id="wrongCount">0</span>)</button>
    </div>

    <!-- 탭 1: 소단원 핵심 개념 -->
    <div id="tab1" class="tab-content">
        <h3 style="color:#f1c40f; margin-top:0;">📘 통합과학2 소단원별 완전 분석</h3>
        
        <div class="concept-box">
            <div class="concept-title">Ⅰ. 변화와 다양성</div>
            <div class="sub-title">1. 산화·환원과 일상생활</div>
            <div>산소를 얻거나 전자를 잃으면 산화, 산소를 잃거나 전자를 얻으면 환원입니다. (광합성, 호흡, 철의 부식, 연소 반응)</div>
            <div class="sub-title">2. 중화 반응</div>
            <div>산($H^+$)과 염기($OH^-$)가 반응하여 물($H_2O$)과 염을 생성하며 중화열이 발생합니다. 지시약 색 변화와 온도 변화가 중요합니다.</div>
            <div class="sub-title">3. 지질 시대와 생물 변천</div>
            <div>선캄브리아 시대, 고생대(삼엽충), 중생대(공룡, 암모나이트), 신생대(화석)의 표준화석과 생물 대멸종을 다룹니다.</div>
            <div class="sub-title">4. 자연선택과 진화</div>
            <div>개체 변이 중에서 환경에 적합한 유리한 형질을 가진 개체가 선택되어 자손을 남기는 과정입니다.</div>
            <div class="sub-title">5. 생물 다양성과 보전</div>
            <div>유전적 다양성, 종 다양성, 생태계 다양성으로 구성되며 서식지 파괴 방지 및 보존 노력이 필요합니다.</div>
        </div>

        <div class="concept-box">
            <div class="concept-title">Ⅱ. 환경과 에너지</div>
            <div class="sub-title">1. 생태계와 환경 변화</div>
            <div>먹이 사슬과 먹이 그물, 생태계 평형의 유지 조건 및 물질 순환과 에너지 흐름을 학습합니다.</div>
            <div class="sub-title">2. 지구 환경 변화</div>
            <div>온실가스 증가에 의한 지구 온난화 및 적도 수온이 상승하는 엘니뇨, 사막화 현상의 원인과 영향을 다룹니다.</div>
            <div class="sub-title">3. 에너지 전환과 효율</div>
            <div>에너지 보존 법칙에 의해 에너지는 전환되지만 열에너지로 산일되므로 열효율($\eta$) 관리가 중요합니다.</div>
            <div class="sub-title">4. 발전과 전력 수송</div>
            <div>전자기 유도를 이용한 화력/수력/핵발전과 손실 전력($P_{loss} = I^2 R$)을 줄이기 위한 고전압 송전 원리를 배웁니다.</div>
            <div class="sub-title">5. 신재생 에너지</div>
            <div>태양 광발전, 풍력 발전, 수소와 산소의 반응으로 물만 배출하는 친환경 수소 연료 전지 원리입니다.</div>
        </div>

        <div class="concept-box">
            <div class="concept-title">Ⅲ. 과학기술과 인류</div>
            <div class="sub-title">1. 신소재의 개발과 활용</div>
            <div>임계 온도 이하 저항이 0이 되는 초전도체, 벌집 모양 탄소 구조 그래핀, 탄소나노튜브의 특성을 배웁니다.</div>
            <div class="sub-title">2. 첨단 과학기술 & 3. 사회적 윤리</div>
            <div>인공지능, 빅데이터 기술 발전과 생명 윤리, 정보 보호 등 기술 발전에 따른 사회적 책임을 학습합니다.</div>
        </div>

        <div class="concept-box">
            <div class="concept-title">Ⅳ. 지구시스템과 우주</div>
            <div class="sub-title">1. 지구시스템과 탄소 순환</div>
            <div>기권, 수권, 지권, 생물권 사이에서 탄소가 이산화탄소, 탄산 이온, 석회암 등으로 순환하는 과정입니다.</div>
            <div class="sub-title">2. 우주 원소의 탄생과 별의 진화</div>
            <div>빅뱅 우주론(수소:헬륨 = 3:1), 별의 내부 핵융합 반응 및 주계열성, 초신성 폭발을 통해 무거운 원소가 생성됩니다.</div>
        </div>
    </div>

    <!-- 탭 2: 문제 풀이 -->
    <div id="tab2" class="tab-content" style="display:none;">
        <div class="quiz-card">
            <div id="quizChapter" style="color:#f1c40f; font-size:13px; font-weight:bold; margin-bottom:5px;">[단원 분류]</div>
            <div class="question-title" id="quizQuestion">문제를 불러오는 중...</div>
            <div class="box-text" id="quizBox" style="display:none;"></div>
            <div id="quizOptions"></div>

            <button class="btn-action btn-submit" onclick="checkAnswer()">정답 제출</button>
            <button class="btn-action btn-next" onclick="loadRandomQuiz()">🎲 새로운 문제 풀기</button>

            <div id="resultBox" class="result-box">
                <div id="resultText" style="font-weight:bold; font-size:16px;"></div>
                <div id="resultDesc" style="margin-top:8px; font-size:14px; color:#ddd; white-space:pre-line;"></div>
            </div>
        </div>
    </div>

    <!-- 탭 3: 오답노트 -->
    <div id="tab3" class="tab-content" style="display:none;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <h3 style="color:#e74c3c; margin:0;">📝 나의 오답 노트</h3>
            <button class="btn-action" style="background:#7f8c8d; color:white; padding:6px 12px; margin:0;" onclick="clearWrongNotes()">🗑️ 오답노트 비우기</button>
        </div>
        <div id="wrongNotesList">오답 기록이 없습니다. 틀린 문제가 이곳에 자동으로 저장됩니다!</div>
    </div>

    <script>
        // 스톱워치 로직
        let timerSeconds = 0, timerInterval = null;
        function startTimer() {
            if (timerInterval) return;
            timerInterval = setInterval(() => {
                timerSeconds++;
                let h = String(Math.floor(timerSeconds / 3600)).padStart(2, '0');
                let m = String(Math.floor((timerSeconds % 3600) / 60)).padStart(2, '0');
                let s = String(timerSeconds % 60).padStart(2, '0');
                document.getElementById("timerText").innerText = `${h}:${m}:${s}`;
            }, 1000);
        }
        function pauseTimer() { clearInterval(timerInterval); timerInterval = null; }
        function resetTimer() { pauseTimer(); timerSeconds = 0; document.getElementById("timerText").innerText = "00:00:00"; }

        // 문제 은행 (소단원별 세분화)
        const QUESTION_BANK = [
            {
                chapter: "Ⅰ. 변화와 다양성 (1. 산화·환원)",
                question: "[완자 기출] 산화 및 환원 반응에 관한 설명으로 옳은 것만을 보기에서 고른 것은?",
                box: "ㄱ. 전자를 잃는 반응을 산화라고 한다.\nㄴ. 산화와 환원은 독립적으로 발생할 수 있다.\nㄷ. 철이 부식하는 현상은 산화 반응에 속한다.",
                options: ["① ㄱ", "② ㄴ", "③ ㄱ, ㄷ", "④ ㄴ, ㄷ", "⑤ ㄱ, ㄴ, ㄷ"],
                answer: 2,
                explanation: "전자를 잃는 것은 산화(ㄱ), 철에 산소가 결합해 부식되는 것도 산화(ㄷ)입니다. 산화-환원은 항상 동시에 일어납니다."
            },
            {
                chapter: "Ⅰ. 변화와 다양성 (2. 중화 반응)",
                question: "[천재교육 기출] 묽은 염산(HCl)과 수산화 나트륨(NaOH) 수용액을 혼합할 때의 설명으로 옳은 것은?",
                options: [
                    "① 수소 이온과 수산화 이온이 1:1 개수비로 반응하여 물이 생성된다.",
                    "② 중화 반응이 진행되어도 혼합 수용액의 온도는 변하지 않는다.",
                    "③ 중화점에 도달하면 페놀프탈레인 용액이 붉은색으로 변한다.",
                    "④ 반응 후 알짜 이온은 나트륨 이온과 염화 이온이다.",
                    "⑤ 산성과 염기성이 만나면 항상 이산화탄소 기체가 발생한다."
                ],
                answer: 0,
                explanation: "중화 반응 시 H⁺와 OH⁻는 1:1 개수비로 결합하여 물(H₂O)을 만듭니다. 이때 온도가 최고점에 도달합니다."
            },
            {
                chapter: "Ⅰ. 변화와 다양성 (4. 자연선택과 진화)",
                question: "[완자 기출] 자연선택설에 따른 생물의 진화 과정 순서로 옳은 것은?",
                box: "(가) 환경 변화 및 자연선택\n(나) 과잉 생산과 변이\n(다) 생존 경쟁\n(라) 유리한 변이의 집단 형성 및 진화",
                options: [
                    "① (가) ➔ (나) ➔ (다) ➔ (라)",
                    "② (나) ➔ (다) ➔ (가) ➔ (라)",
                    "③ (나) ➔ (가) ➔ (다) ➔ (라)",
                    "④ (다) ➔ (나) ➔ (가) ➔ (라)",
                    "⑤ (가) ➔ (다) ➔ (나) ➔ (라)"
                ],
                answer: 1,
                explanation: "진화 순서: 과잉 생산과 변이 ➔ 생존 경쟁 ➔ 환경에 적합한 형질 선택(자연선택) ➔ 개체군 변화 및 진화."
            },
            {
                chapter: "Ⅱ. 환경과 에너지 (4. 발전과 전력 수송)",
                question: "[천재교육 기출] 송전선에서 손실되는 전력($P_{loss}$)을 줄이기 위한 방법으로 가장 효과적인 것은?",
                options: [
                    "① 송전 전압을 낮춘다.",
                    "② 송전선에 흐르는 전류의 세기를 늘린다.",
                    "③ 변전소에서 송전 전압을 크게 높여 송전한다.",
                    "④ 저항이 훨씬 큰 송전선 재질로 교체한다.",
                    "⑤ 전력 발전량을 절반 이하로 줄인다."
                ],
                answer: 2,
                explanation: "손실 전력 $P_{loss} = I^2 R$ 입니다. 전압을 V배 높이면 전류는 1/V배로 줄어들어 손실 전력이 $1/V^2$ 배로 대폭 감소합니다."
            },
            {
                chapter: "Ⅱ. 환경과 에너지 (5. 신재생 에너지)",
                question: "[완자 기출] 수소 연료 전지에 대한 특징으로 옳지 않은 것은?",
                options: [
                    "① 수소가 산화되면서 발생하는 전자를 이용한다.",
                    "② 화학 에너지를 전기 에너지를 직접 전환한다.",
                    "③ 연소 과정이 없으므로 에너지 효율이 높다.",
                    "④ 반응 부산물로 순수한 물(H₂O)만 배출된다.",
                    "⑤ 반응 시 유해한 온실가스(CO₂)가 대량 배출된다."
                ],
                answer: 4,
                explanation: "수소 연료 전지는 이산화탄소나 유해 가스 배출이 전혀 없는 친환경 자원입니다."
            },
            {
                chapter: "Ⅲ. 과학기술과 인류 (1. 신소재)",
                question: "[천재교육 기출] 초전도체와 관련된 설명으로 옳은 것만을 보기에서 고른 것은?",
                box: "ㄱ. 특정 온도(임계 온도) 이하에서 전기 저항이 0이 된다.\nㄴ. 자석 위에 부유하는 현상을 마이스너 효과라고 한다.\nㄷ. 강한 자기장을 형성하여 MRI 장치 등에 활용된다.",
                options: ["① ㄱ", "② ㄷ", "③ ㄱ, ㄴ", "④ ㄴ, ㄷ", "⑤ ㄱ, ㄴ, ㄷ"],
                answer: 4,
                explanation: "초전도체는 임계 온도 이하에서 저항이 0이 되며 자석을 띄우는 마이스너 효과를 나타냅니다."
            },
            {
                chapter: "Ⅳ. 지구시스템과 우주 (2. 우주 원소의 탄생)",
                question: "[완자 기출] 빅뱅 우주론에 의해 우주 초기에 형성된 수소 핵과 헬륨 핵의 질량비는?",
                options: ["① 1 : 1", "② 3 : 1", "③ 7 : 1", "④ 12 : 1", "⑤ 1 : 3"],
                answer: 1,
                explanation: "빅뱅 핵합성에 의해 수소와 헬륨의 질량비는 약 3 : 1로 형성되었으며 펜지어스와 윌슨의 우주배경복사 관측으로 입증되었습니다."
            }
        ];

        let currentQuiz = null;
        let selectedOption = -1;
        let wrongNotes = JSON.parse(localStorage.getItem("science_wrong_notes") || "[]");

        function updateWrongCount() {
            document.getElementById("wrongCount").innerText = wrongNotes.length;
        }
        updateWrongCount();

        function switchTab(idx) {
            document.getElementById("btnTab1").className = idx === 1 ? "tab-btn active" : "tab-btn";
            document.getElementById("btnTab2").className = idx === 2 ? "tab-btn active" : "tab-btn";
            document.getElementById("btnTab3").className = idx === 3 ? "tab-btn active" : "tab-btn";
            document.getElementById("tab1").style.display = idx === 1 ? "block" : "none";
            document.getElementById("tab2").style.display = idx === 2 ? "block" : "none";
            document.getElementById("tab3").style.display = idx === 3 ? "block" : "none";
            
            if (idx === 2 && !currentQuiz) loadRandomQuiz();
            if (idx === 3) renderWrongNotes();
        }

        function loadRandomQuiz() {
            selectedOption = -1;
            document.getElementById("resultBox").style.display = "none";
            
            const randIdx = Math.floor(Math.random() * QUESTION_BANK.length);
            currentQuiz = QUESTION_BANK[randIdx];

            document.getElementById("quizChapter").innerText = `[${currentQuiz.chapter}]`;
            document.getElementById("quizQuestion").innerText = currentQuiz.question;

            const boxEl = document.getElementById("quizBox");
            if (currentQuiz.box) {
                boxEl.innerText = currentQuiz.box;
                boxEl.style.display = "block";
            } else {
                boxEl.style.display = "none";
            }

            let optHtml = "";
            currentQuiz.options.forEach((opt, idx) => {
                optHtml += `<div class="option-item" id="opt_${idx}" onclick="selectOption(${idx})">${opt}</div>`;
            });
            document.getElementById("quizOptions").innerHTML = optHtml;
        }

        function selectOption(idx) {
            selectedOption = idx;
            currentQuiz.options.forEach((_, i) => {
                const el = document.getElementById(`opt_${i}`);
                if (i === idx) el.classList.add("selected");
                else el.classList.remove("selected");
            });
        }

        function checkAnswer() {
            if (selectedOption === -1) {
                alert("정답 보기 중 하나를 선택해 주세요!");
                return;
            }

            const resBox = document.getElementById("resultBox");
            const resText = document.getElementById("resultText");
            const resDesc = document.getElementById("resultDesc");

            if (selectedOption === currentQuiz.answer) {
                resBox.className = "result-box result-success";
                resText.innerText = "🎉 정답입니다! (+50 코인 적립)";
                resDesc.innerText = "해설: " + currentQuiz.explanation;

                let coins = parseInt(localStorage.getItem("car_total_coins") || "0");
                localStorage.setItem("car_total_coins", (coins + 50).toString());
            } else {
                resBox.className = "result-box result-fail";
                resText.innerText = `❌ 틀렸습니다. (정답: ${currentQuiz.options[currentQuiz.answer]})`;
                resDesc.innerText = "해설: " + currentQuiz.explanation;

                // 오답노트 저장
                wrongNotes.push({
                    chapter: currentQuiz.chapter,
                    question: currentQuiz.question,
                    myAnswer: currentQuiz.options[selectedOption],
                    correctAnswer: currentQuiz.options[currentQuiz.answer],
                    explanation: currentQuiz.explanation
                });
                localStorage.setItem("science_wrong_notes", JSON.stringify(wrongNotes));
                updateWrongCount();
            }
            resBox.style.display = "block";
        }

        function renderWrongNotes() {
            const listEl = document.getElementById("wrongNotesList");
            if (wrongNotes.length === 0) {
                listEl.innerHTML = "<p style='color:#bbb;'>오답 기록이 없습니다. 완벽하네요!</p>";
                return;
            }

            let html = "";
            wrongNotes.forEach((wn, idx) => {
                html += `<div class="wrong-card">
                    <div style="color:#f1c40f; font-size:12px; font-weight:bold;">${wn.chapter}</div>
                    <div style="font-weight:bold; margin-top:4px; color:#38bdf8;">${wn.question}</div>
                    <div style="margin-top:6px; font-size:13px; color:#ef4444;">내 선택: ${wn.myAnswer}</div>
                    <div style="font-size:13px; color:#2ecc71;">정답: ${wn.correctAnswer}</div>
                    <div style="margin-top:6px; font-size:12px; color:#ccc;">💡 해설: ${wn.explanation}</div>
                </div>`;
            });
            listEl.innerHTML = html;
        }

        function clearWrongNotes() {
            if (confirm("오답노트를 비우시겠습니까?")) {
                wrongNotes = [];
                localStorage.removeItem("science_wrong_notes");
                updateWrongCount();
                renderWrongNotes();
            }
        }
    </script>
    </body>
    </html>
    """
    components.html(science_html, height=720)

# ==========================================
# 🏎️ 3. 7인 아이템 카트 레이싱
# ==========================================
elif st.session_state.current_screen == "racing":
    col_nav1, col_nav2 = st.columns([1, 4])
    with col_nav1:
        st.button("🏠 메인으로", on_click=set_screen, args=("home",), use_container_width=True)
    with col_nav2:
        st.subheader("🏎️ 7인 카트 레이싱")

    st.caption("조작법 | W: 전진 | S: 후진 | A/D: 회전 | Shift: 드리프트 | Ctrl/Alt: 첫 번째 아이템 사용")

    racing_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; padding: 0; background-color: #0e1117; color: #fff; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; }
            #gameContainer { position: relative; width: 720px; height: 500px; box-shadow: 0 10px 25px rgba(0,0,0,0.7); border-radius: 12px; overflow: hidden; border: 2px solid #333; }
            canvas { display: block; }
            #startOverlay, #recordsOverlay {
                position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0,0,0,0.88); display: flex; flex-direction: column;
                align-items: center; justify-content: center; z-index: 10;
            }
            .btn-start {
                padding: 12px 28px; font-size: 18px; font-weight: bold; color: #fff;
                background: #e74c3c; border: none; border-radius: 8px; cursor: pointer; margin: 5px;
            }
            .btn-practice { background: #3498db; }
            .btn-records { background: #f39c12; }
            .btn-reset { background: #7f8c8d; font-size: 14px; padding: 8px 16px; margin-top: 10px; }
            .btn-start:hover { transform: scale(1.05); }
        </style>
    </head>
    <body>

    <div id="gameContainer">
        <div id="startOverlay">
            <h1 id="mapTitle" style="color:#f1c40f; margin-bottom:5px;">🏁 카트 레이싱</h1>
            <p id="mapDesc" style="color:#ccc; margin-bottom:15px;">아이템을 최대 2개까지 보관할 수 있습니다!</p>
            <div style="display:flex; gap:10px;">
                <button class="btn-start" onclick="startGame(false)">🏁 경기 시작</button>
                <button class="btn-start btn-practice" onclick="startGame(true)">🏎️ 혼자 연습하기</button>
            </div>
            <div style="display:flex; gap:10px; margin-top:10px;">
                <button class="btn-start btn-records" onclick="showRecords()">⏱️ 트랙별 최고기록</button>
                <button class="btn-start btn-reset" onclick="resetRacingData()">🔄 레이스 데이터 리셋</button>
            </div>
        </div>

        <div id="recordsOverlay" style="display:none;">
            <h2 style="color:#f1c40f; margin-bottom:10px;">⏱️ 스테이지별 최고 기록</h2>
            <div id="recordsList" style="text-align:left; max-height:300px; overflow-y:auto; font-size:15px; width:80%;"></div>
            <button class="btn-start" style="margin-top:15px;" onclick="closeRecords()">닫기</button>
        </div>

        <canvas id="gameCanvas" width="720" height="500"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const MAP_THEMES = [
            { id: 1, name: "1번 맵: 🌵 사막 대곡선 8자 루프 트랙", bgColor: "#e67e22", roadColor: "#2c3e50", border: "#f39c12", props: [{x:800,y:400,icon:"🌵"}, {x:2200,y:1200,icon:"🏜️"}, {x:1500,y:2500,icon:"🏝️"}, {x:600,y:3000,icon:"🌵"}], waypoints: [{x:600,y:600}, {x:1800,y:600}, {x:2600,y:1200}, {x:2000,y:2000}, {x:1200,y:1600}, {x:800,y:2400}, {x:1600,y:3400}, {x:2800,y:3200}, {x:3400,y:2200}, {x:3000,y:1000}, {x:2000,y:200}, {x:600,y:600}] },
            { id: 2, name: "2번 맵: ❄️ 눈꽃 설원 연속 S자 헤어핀 트랙", bgColor: "#3498db", roadColor: "#ecf0f1", border: "#2980b9", props: [{x:700,y:400,icon:"🌲"}, {x:1800,y:1200,icon:"🧊"}, {x:3000,y:2200,icon:"☃️"}, {x:1200,y:3000,icon:"🌲"}], waypoints: [{x:600,y:600}, {x:1500,y:600}, {x:2200,y:1200}, {x:1500,y:1800}, {x:2500,y:2200}, {x:3400,y:1600}, {x:3600,y:2800}, {x:2600,y:3400}, {x:1600,y:2800}, {x:1000,y:3600}, {x:400,y:2600}, {x:600,y:1500}, {x:600,y:600}] },
            { id: 3, name: "3번 맵: 🏙️ 네온 시티 스트리트 트랙", bgColor: "#1a0826", roadColor: "#2c2c54", border: "#ff007f", props: [{x:800,y:300,icon:"🏙️"}, {x:2500,y:1000,icon:"🏢"}, {x:3200,y:2500,icon:"🏬"}, {x:1000,y:3200,icon:"🏙️"}], waypoints: [{x:600,y:600}, {x:2400,y:600}, {x:2400,y:1500}, {x:3500,y:1500}, {x:3500,y:3200}, {x:2000,y:3200}, {x:2000,y:2200}, {x:1000,y:2200}, {x:1000,y:3600}, {x:400,y:3600}, {x:400,y:1800}, {x:600,y:600}] },
            { id: 4, name: "4번 맵: 🌳 깊은 숲속 원형 링 코스", bgColor: "#1e4620", roadColor: "#4e3629", border: "#27ae60", props: [{x:900,y:400,icon:"🌳"}, {x:2600,y:1100,icon:"🍄"}, {x:3100,y:2600,icon:"🌲"}, {x:1200,y:3100,icon:"🌳"}], waypoints: [{x:600,y:600}, {x:2000,y:400}, {x:3200,y:1000}, {x:3600,y:2200}, {x:3000,y:3200}, {x:1800,y:3600}, {x:800,y:3000}, {x:400,y:1800}, {x:600,y:600}] },
            { id: 5, name: "5번 맵: 🌋 화산 지옥 꼬불꼬불 복합 트랙", bgColor: "#3d0c02", roadColor: "#1c1c1c", border: "#e74c3c", props: [{x:700,y:300,icon:"🔥"}, {x:2000,y:1000,icon:"🗿"}, {x:3300,y:2000,icon:"🔥"}, {x:1400,y:3200,icon:"🗿"}], waypoints: [{x:600,y:600}, {x:1400,y:600}, {x:1000,y:1400}, {x:2000,y:1400}, {x:2600,y:800}, {x:3400,y:1600}, {x:2800,y:2400}, {x:3400,y:3200}, {x:2200,y:3600}, {x:1500,y:2800}, {x:800,y:3400}, {x:400,y:2200}, {x:600,y:600}] },
            { id: 6, name: "6번 맵: 🌊 해변 리조트 야자수 트랙", bgColor: "#16a085", roadColor: "#f39c12", border: "#1abc9c", props: [{x:800,y:400,icon:"🌴"}, {x:2200,y:1000,icon:"🏖️"}, {x:3000,y:2400,icon:"🍹"}, {x:1200,y:3000,icon:"🌴"}], waypoints: [{x:600,y:600}, {x:1800,y:500}, {x:2800,y:1200}, {x:3400,y:2400}, {x:2400,y:3000}, {x:1800,y:2200}, {x:1000,y:3200}, {x:400,y:2000}, {x:600,y:600}] },
            { id: 7, name: "7번 맵: 🌌 우주 은하수 레이싱 트랙", bgColor: "#0c0826", roadColor: "#341f97", border: "#5f27cd", props: [{x:900,y:300,icon:"🚀"}, {x:2400,y:1200,icon:"🪐"}, {x:3200,y:2600,icon:"⭐"}, {x:1100,y:2800,icon:"🛸"}], waypoints: [{x:600,y:600}, {x:1600,y:1000}, {x:2600,y:600}, {x:3500,y:1600}, {x:2800,y:2600}, {x:2000,y:1800}, {x:1200,y:3400}, {x:400,y:2400}, {x:600,y:600}] },
            { id: 8, name: "8번 맵: 🍬 달콤한 캔디랜드 트랙", bgColor: "#fd79a8", roadColor: "#6c5ce7", border: "#e84393", props: [{x:800,y:400,icon:"🍭"}, {x:2300,y:1100,icon:"🍬"}, {x:3100,y:2500,icon:"🍩"}, {x:1000,y:3000,icon:"🧁"}], waypoints: [{x:600,y:600}, {x:1400,y:600}, {x:2000,y:1200}, {x:2800,y:600}, {x:3500,y:1800}, {x:2600,y:2800}, {x:1600,y:2200}, {x:800,y:3400}, {x:400,y:2000}, {x:600,y:600}] },
            { id: 9, name: "9번 맵: 🏰 중세 고성 기사 트랙", bgColor: "#2d3436", roadColor: "#636e72", border: "#d63031", props: [{x:700,y:300,icon:"🏰"}, {x:2100,y:1000,icon:"🛡️"}, {x:3200,y:2200,icon:"⚔️"}, {x:1300,y:3100,icon:"👑"}], waypoints: [{x:600,y:600}, {x:1900,y:600}, {x:2500,y:1400}, {x:3500,y:1400}, {x:3500,y:3000}, {x:2200,y:3000}, {x:1500,y:2000}, {x:800,y:3400}, {x:400,y:1800}, {x:600,y:600}] },
            { id: 10, name: "10번 맵: ⚡ 사이버펑크 미래도시 트랙", bgColor: "#0f0f1b", roadColor: "#111", border: "#00d2d3", props: [{x:800,y:400,icon:"⚡"}, {x:2500,y:1200,icon:"🤖"}, {x:3000,y:2500,icon:"👾"}, {x:1100,y:3000,icon:"🔋"}], waypoints: [{x:600,y:600}, {x:1600,y:400}, {x:2400,y:1200}, {x:3600,y:1200}, {x:3000,y:2600}, {x:1800,y:2600}, {x:1200,y:3600}, {x:400,y:2400}, {x:600,y:600}] }
        ];

        const PRACTICE_MAP = {
            id: 0, name: "🏎️ 자유 연습 트랙 (기록 저장 가능)",
            bgColor: "#2c3e50", roadColor: "#34495e", border: "#1abc9c",
            props: [{x:1000,y:1000,icon:"🎯"}],
            waypoints: [{x:600,y:600}, {x:2000,y:600}, {x:2000,y:2000}, {x:600,y:2000}, {x:600,y:600}]
        };

        let currentTheme = MAP_THEMES[Math.floor(Math.random() * MAP_THEMES.length)];
        let waypoints = currentTheme.waypoints;
        document.getElementById("mapTitle").innerText = currentTheme.name;

        let gameStarted = false, countdown = -1, finishTimer = -1, raceEnded = false, winnerName = "", raceStartTime = 0, elapsedRaceTime = "00:00.0", isPractice = false;
        const keys = { w: false, s: false, a: false, d: false, shift: false };

        window.addEventListener("keydown", (e) => {
            if (e.key === "w" || e.key === "W" || e.key === "ㅈ") keys.w = true;
            if (e.key === "s" || e.key === "S" || e.key === "ㄴ") keys.s = true;
            if (e.key === "a" || e.key === "A" || e.key === "ㅁ") keys.a = true;
            if (e.key === "d" || e.key === "D" || e.key === "ㅇ") keys.d = true;
            if (e.key === "Shift") keys.shift = true;
            if (e.key === "Control" || e.key === "Alt") useItem(player);
        });

        window.addEventListener("keyup", (e) => {
            if (e.key === "w" || e.key === "W" || e.key === "ㅈ") keys.w = false;
            if (e.key === "s" || e.key === "S" || e.key === "ㄴ") keys.s = false;
            if (e.key === "a" || e.key === "A" || e.key === "ㅁ") keys.a = false;
            if (e.key === "d" || e.key === "D" || e.key === "ㅇ") keys.d = false;
            if (e.key === "Shift") keys.shift = false;
        });

        function showRecords() {
            let html = "";
            let practiceRec = localStorage.getItem(`kart_best_map_0`) || "기록 없음";
            html += `<div style="margin-bottom:8px; color:#38bdf8;"><b>${PRACTICE_MAP.name}</b>: <span>${practiceRec}</span></div><hr/>`;
            MAP_THEMES.forEach(m => {
                let rec = localStorage.getItem(`kart_best_map_${m.id}`) || "기록 없음";
                html += `<div style="margin-bottom:8px;"><b>${m.name}</b>: <span style="color:#2ecc71;">${rec}</span></div>`;
            });
            document.getElementById("recordsList").innerHTML = html;
            document.getElementById("recordsOverlay").style.display = "flex";
        }

        function closeRecords() { document.getElementById("recordsOverlay").style.display = "none"; }

        function resetRacingData() {
            if (confirm("연습 트랙 및 모든 스테이지 최고 기록을 초기화하시겠습니까?")) {
                localStorage.removeItem(`kart_best_map_0`);
                MAP_THEMES.forEach(m => localStorage.removeItem(`kart_best_map_${m.id}`));
                alert("기록이 리셋되었습니다.");
                showRecords();
            }
        }

        function startGame(practiceMode) {
            isPractice = practiceMode;
            if (isPractice) {
                currentTheme = PRACTICE_MAP;
                waypoints = currentTheme.waypoints;
            }
            document.getElementById("startOverlay").style.display = "none";
            countdown = 5;

            karts = [createKart(0, "나(Player)", colors[0], false, 600, 600)];
            if (!isPractice) {
                for (let i = 1; i < 7; i++) karts.push(createKart(i, `AI ${i}`, colors[i], true, 600 - (i*30), 600 + (i%2 === 0 ? 35 : -35)));
            }
            player = karts[0];

            itemBoxes = [];
            for (let i = 1; i < waypoints.length - 1; i += 2) {
                itemBoxes.push({ x: waypoints[i].x, y: waypoints[i].y, active: true, timer: 0 });
            }

            let timer = setInterval(() => {
                countdown--;
                if (countdown < 0) { clearInterval(timer); gameStarted = true; raceStartTime = Date.now(); }
            }, 1000);
        }

        function createKart(id, name, color, isAI, startX, startY) {
            return { id: id, name: name, color: color, isAI: isAI, x: startX, y: startY, angle: 0, speed: 0, maxSpeed: isAI ? 7.8 + Math.random()*1.2 : 8.6, accel: 0.13, decel: 0.05, turnSensitivity: 0.038, laneOffset: isAI ? (Math.random()-0.5)*90 : 0, targetWayIndex: 1, lap: 1, finished: false, finishTimeStr: "-", finishTimeMs: Infinity, items: [], boostTime: 0, spinTime: 0, skidmarks: [] };
        }

        const colors = ["#e74c3c", "#3498db", "#2ecc71", "#f1c40f", "#9b59b6", "#e67e22", "#1abc9c"];
        let karts = [], player = null, bananas = [], itemBoxes = [];

        function useItem(kart) {
            if (!kart.items || kart.items.length === 0) return;
            let currentItem = kart.items.shift();
            if (currentItem === "booster") kart.boostTime = 90;
            else if (currentItem === "banana") bananas.push({ x: kart.x - Math.cos(kart.angle)*35, y: kart.y - Math.sin(kart.angle)*35 });
        }

        function getDistanceToTrack(px, py) {
            let minDistance = 99999, closestProjX = px, closestProjY = py;
            for (let i = 0; i < waypoints.length - 1; i++) {
                const p1 = waypoints[i], p2 = waypoints[i+1];
                const dx = p2.x - p1.x, dy = p2.y - p1.y, len = Math.hypot(dx, dy);
                const u = Math.max(0, Math.min(1, ((px - p1.x)*dx + (py - p1.y)*dy) / (len*len)));
                const projX = p1.x + u*dx, projY = p1.y + u*dy, dist = Math.hypot(px - projX, py - projY);
                if (dist < minDistance) { minDistance = dist; closestProjX = projX; closestProjY = projY; }
            }
            return { distance: minDistance, projX: closestProjX, projY: closestProjY };
        }

        function formatTime(ms) {
            const totalSec = ms / 1000;
            return `${Math.floor(totalSec / 60).toString().padStart(2, '0')}:${Math.floor(totalSec % 60).toString().padStart(2, '0')}.${Math.floor((ms % 1000) / 100)}`;
        }

        function saveStageRecord(mapId, timeStr, rawMs) {
            let key = `kart_best_map_${mapId}`;
            let keyMs = `kart_best_ms_${mapId}`;
            let oldMs = parseInt(localStorage.getItem(keyMs) || "99999999");
            if (rawMs < oldMs) {
                localStorage.setItem(key, timeStr);
                localStorage.setItem(keyMs, rawMs.toString());
            }
        }

        function update() {
            if (!gameStarted || raceEnded) return;
            const currentMs = Date.now() - raceStartTime;
            elapsedRaceTime = formatTime(currentMs);

            karts.forEach((k) => {
                if (k.finished) return;

                if (k.spinTime > 0) { k.spinTime--; k.speed *= 0.85; k.angle += 0.3; return; }

                if (k.isAI) {
                    const target = waypoints[k.targetWayIndex];
                    let angleDiff = Math.atan2(target.y + k.laneOffset - k.y, target.x + k.laneOffset - k.x) - k.angle;
                    while (angleDiff < -Math.PI) angleDiff += Math.PI * 2;
                    while (angleDiff > Math.PI) angleDiff -= Math.PI * 2;
                    k.angle += Math.sign(angleDiff) * Math.min(Math.abs(angleDiff), k.turnSensitivity);
                    if (k.speed < k.maxSpeed * 0.9) k.speed += k.accel;
                    if (Math.hypot(target.x - k.x, target.y - k.y) < 250) {
                        k.targetWayIndex++;
                        if (k.targetWayIndex >= waypoints.length) { 
                            k.targetWayIndex = 1; k.lap++; 
                            if (k.lap > 3 && !k.finished) { 
                                k.finished = true; 
                                k.finishTimeStr = elapsedRaceTime; 
                                k.finishTimeMs = currentMs; 
                                checkFirstFinish(k.name); 
                            } 
                        }
                    }
                    if (k.items.length > 0 && Math.random() < 0.01) useItem(k);
                } else {
                    if (keys.w) k.speed = Math.min(k.maxSpeed, k.speed + k.accel);
                    else if (keys.s) k.speed = Math.max(-k.maxSpeed * 0.4, k.speed - k.accel * 1.5);
                    else { if (k.speed > 0) k.speed = Math.max(0, k.speed - k.decel); if (k.speed < 0) k.speed = Math.min(0, k.speed + k.decel); }

                    let turnSpeed = k.turnSensitivity;
                    if (keys.shift && (keys.a || keys.d)) { turnSpeed = 0.065; k.speed *= 0.988; k.skidmarks.push({ x: k.x, y: k.y, alpha: 1.0 }); }
                    if (keys.a) k.angle -= turnSpeed; if (keys.d) k.angle += turnSpeed;

                    const target = waypoints[k.targetWayIndex];
                    if (Math.hypot(target.x - k.x, target.y - k.y) < 250) {
                        k.targetWayIndex++;
                        if (k.targetWayIndex >= waypoints.length) {
                            k.targetWayIndex = 1; k.lap++;
                            if (k.lap > 3 && !k.finished) {
                                k.finished = true; 
                                k.finishTimeStr = elapsedRaceTime;
                                k.finishTimeMs = currentMs;
                                saveStageRecord(currentTheme.id, elapsedRaceTime, currentMs);
                                checkFirstFinish(k.name);
                            }
                        }
                    }
                }

                if (k.boostTime > 0) { k.boostTime--; k.speed = k.maxSpeed * 1.45; }

                let nextX = k.x + Math.cos(k.angle) * k.speed;
                let nextY = k.y + Math.sin(k.angle) * k.speed;
                const trackInfo = getDistanceToTrack(nextX, nextY);
                if (trackInfo.distance > 115) {
                    const pushAngle = Math.atan2(nextY - trackInfo.projY, nextX - trackInfo.projX);
                    nextX = trackInfo.projX + Math.cos(pushAngle) * 115;
                    nextY = trackInfo.projY + Math.sin(pushAngle) * 115;
                    k.speed *= 0.6;
                }
                k.x = nextX; k.y = nextY;

                itemBoxes.forEach(box => {
                    if (box.active && Math.hypot(k.x - box.x, k.y - box.y) < 40) {
                        box.active = false; box.timer = 180;
                        if (k.items.length < 2) {
                            k.items.push(Math.random() > 0.5 ? "booster" : "banana");
                        }
                    }
                });

                for (let i = bananas.length - 1; i >= 0; i--) {
                    if (Math.hypot(k.x - bananas[i].x, k.y - bananas[i].y) < 25) {
                        k.spinTime = 40; bananas.splice(i, 1);
                    }
                }

                k.skidmarks.forEach((sm, idx) => {
                    sm.alpha -= 0.02;
                    if (sm.alpha <= 0) k.skidmarks.splice(idx, 1);
                });
            });

            itemBoxes.forEach(box => { if (!box.active && --box.timer <= 0) box.active = true; });

            karts.sort((a, b) => {
                if (a.finished && b.finished) return a.finishTimeMs - b.finishTimeMs;
                if (a.finished) return -1;
                if (b.finished) return 1;
                if (a.lap !== b.lap) return b.lap - a.lap;
                if (a.targetWayIndex !== b.targetWayIndex) return b.targetWayIndex - a.targetWayIndex;
                return Math.hypot(waypoints[a.targetWayIndex].x - a.x, waypoints[a.targetWayIndex].y - a.y) - Math.hypot(waypoints[b.targetWayIndex].x - b.x, waypoints[b.targetWayIndex].y - b.y);
            });
        }

        function checkFirstFinish(winner) {
            if (finishTimer !== -1) return;
            winnerName = winner; finishTimer = 5;
            let interval = setInterval(() => { 
                finishTimer--; 
                if (finishTimer <= 0) { 
                    clearInterval(interval); 
                    raceEnded = true; 
                    karts.sort((a, b) => {
                        if (a.finished && b.finished) return a.finishTimeMs - b.finishTimeMs;
                        if (a.finished) return -1;
                        if (b.finished) return 1;
                        return 0;
                    });
                } 
            }, 1000);
        }

        function restartRace() {
            currentTheme = MAP_THEMES[Math.floor(Math.random() * MAP_THEMES.length)]; waypoints = currentTheme.waypoints;
            document.getElementById("mapTitle").innerText = currentTheme.name;
            gameStarted = false; countdown = -1; finishTimer = -1; raceEnded = false; winnerName = ""; elapsedRaceTime = "00:00.0"; bananas = [];
            document.getElementById("startOverlay").style.display = "flex";
        }

        function draw() {
            ctx.fillStyle = currentTheme.bgColor; ctx.fillRect(0, 0, canvas.width, canvas.height);
            if (!player) return;

            ctx.save(); ctx.translate(canvas.width / 2 - player.x, canvas.height / 2 - player.y);

            ctx.strokeStyle = currentTheme.roadColor; ctx.lineWidth = 240; ctx.lineCap = "round"; ctx.lineJoin = "round";
            ctx.beginPath(); ctx.moveTo(waypoints[0].x, waypoints[0].y);
            for (let i = 1; i < waypoints.length; i++) ctx.lineTo(waypoints[i].x, waypoints[i].y);
            ctx.stroke();

            ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 246; ctx.stroke();
            ctx.strokeStyle = currentTheme.border; ctx.lineWidth = 240; ctx.setLineDash([35, 35]); ctx.stroke(); ctx.setLineDash([]);
            ctx.strokeStyle = currentTheme.roadColor; ctx.lineWidth = 230; ctx.stroke();
            ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 5; ctx.setLineDash([25, 25]); ctx.stroke(); ctx.setLineDash([]);
            ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 18; ctx.beginPath(); ctx.moveTo(600, 470); ctx.lineTo(600, 730); ctx.stroke();

            currentTheme.props.forEach(p => { ctx.font = "40px sans-serif"; ctx.textAlign = "center"; ctx.fillText(p.icon, p.x, p.y); });

            bananas.forEach(b => {
                ctx.fillStyle = "#f1c40f"; ctx.beginPath(); ctx.arc(b.x, b.y, 12, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#111"; ctx.font = "14px sans-serif"; ctx.fillText("🍌", b.x - 8, b.y + 5);
            });

            itemBoxes.forEach(box => {
                if (box.active) {
                    ctx.fillStyle = "#9b59b6"; ctx.fillRect(box.x - 20, box.y - 20, 40, 40);
                    ctx.fillStyle = "#fff"; ctx.font = "bold 20px sans-serif"; ctx.fillText("?", box.x - 6, box.y + 7);
                }
            });

            karts.forEach(k => {
                k.skidmarks.forEach(sm => { ctx.fillStyle = `rgba(0,0,0,${sm.alpha * 0.5})`; ctx.fillRect(sm.x - 4, sm.y - 4, 8, 8); });
                ctx.save(); ctx.translate(k.x, k.y); ctx.rotate(k.angle);
                ctx.fillStyle = k.color; ctx.beginPath(); ctx.roundRect(-18, -12, 36, 24, 6); ctx.fill();
                ctx.fillStyle = "#111"; ctx.fillRect(-14, -15, 9, 4); ctx.fillRect(5, -15, 9, 4); ctx.fillRect(-14, 11, 9, 4); ctx.fillRect(5, 11, 9, 4);
                ctx.rotate(-k.angle); ctx.fillStyle = "#fff"; ctx.font = "bold 12px sans-serif"; ctx.textAlign = "center"; ctx.fillText(k.name, 0, -22); ctx.restore();
            });
            ctx.restore();

            if (countdown > 0) { ctx.fillStyle = "rgba(0,0,0,0.5)"; ctx.fillRect(0,0,canvas.width,canvas.height); ctx.fillStyle = "#f1c40f"; ctx.font = "bold 90px sans-serif"; ctx.textAlign = "center"; ctx.fillText(countdown, canvas.width/2, canvas.height/2 + 30); }
            else if (countdown === 0) { ctx.fillStyle = "#2ecc71"; ctx.font = "bold 90px sans-serif"; ctx.textAlign = "center"; ctx.fillText("GO!", canvas.width/2, canvas.height/2 + 30); }

            const myRank = karts.findIndex(k => k.id === player.id) + 1;
            ctx.fillStyle = "#ffffff"; ctx.font = "bold 22px sans-serif"; ctx.textAlign = "left";
            ctx.fillText(`순위: ${myRank} / ${karts.length}위`, 20, 35);
            ctx.fillText(`LAP: ${Math.min(3, player.lap)} / 3`, 20, 65);
            ctx.fillText(`TIME: ${elapsedRaceTime}`, 20, 95);

            for (let s = 0; s < 2; s++) {
                const boxX = canvas.width - 150 + (s * 70);
                ctx.fillStyle = "rgba(0,0,0,0.6)"; ctx.fillRect(boxX, 15, 60, 60);
                ctx.strokeStyle = "#f1c40f"; ctx.lineWidth = 2; ctx.strokeRect(boxX, 15, 60, 60);
                if (player.items && player.items[s]) {
                    ctx.font = "28px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(player.items[s] === "booster" ? "🚀" : "🍌", boxX + 30, 55);
                }
            }

            const mapX = canvas.width - 140, mapY = canvas.height - 140, mapSize = 120;
            ctx.fillStyle = "rgba(0,0,0,0.85)"; ctx.fillRect(mapX, mapY, mapSize, mapSize);
            ctx.strokeStyle = "rgba(255,255,255,0.5)"; ctx.lineWidth = 3; ctx.beginPath();
            ctx.moveTo(mapX + (waypoints[0].x / 4000) * mapSize, mapY + (waypoints[0].y / 4000) * mapSize);
            for (let i = 1; i < waypoints.length; i++) ctx.lineTo(mapX + (waypoints[i].x / 4000) * mapSize, mapY + (waypoints[i].y / 4000) * mapSize);
            ctx.stroke();
            karts.forEach(k => { ctx.fillStyle = k.color; ctx.beginPath(); ctx.arc(mapX + (k.x / 4000) * mapSize, mapY + (k.y / 4000) * mapSize, k.id === player.id ? 4 : 2, 0, Math.PI*2); ctx.fill(); });

            if (finishTimer > 0) {
                ctx.fillStyle = "rgba(0,0,0,0.75)"; ctx.fillRect(0, canvas.height/2 - 50, canvas.width, 100);
                ctx.fillStyle = "#2ecc71"; ctx.font = "bold 26px sans-serif"; ctx.textAlign = "center";
                ctx.fillText(`🏁 ${winnerName} 1등 완주! 종료까지 ${finishTimer}초`, canvas.width/2, canvas.height/2 + 8);
            }

            if (raceEnded) {
                ctx.fillStyle = "rgba(0,0,0,0.92)"; ctx.fillRect(0,0,canvas.width,canvas.height);
                ctx.fillStyle = "#f1c40f"; ctx.font = "bold 30px sans-serif"; ctx.textAlign = "center"; ctx.fillText("🏆 레이스 최종 결과 🏆", canvas.width/2, 60);
                ctx.fillStyle = "#3498db"; ctx.font = "bold 18px sans-serif"; ctx.fillText(`[ ${currentTheme.name} 완주 ]`, canvas.width/2, 95);
                
                karts.forEach((k, idx) => { 
                    ctx.fillStyle = k.id === player.id ? "#f1c40f" : "#ffffff"; 
                    ctx.font = "17px sans-serif"; 
                    ctx.textAlign = "left"; 
                    ctx.fillText(`${idx + 1}위 : ${k.name} - ⏱️ ${k.finished ? k.finishTimeStr : "RETIRED"}`, canvas.width/2 - 170, 140 + (idx * 35)); 
                });
                
                ctx.fillStyle = "#2ecc71"; ctx.font = "bold 17px sans-serif"; ctx.textAlign = "center"; ctx.fillText("아래 [다른 트랙으로 다시 하기] 버튼을 누르세요!", canvas.width/2, 425);
            }
        }
        function loop() { update(); draw(); requestAnimationFrame(loop); } loop();
    </script>
    <div style="text-align: center; margin-top: 10px;">
        <button onclick="restartRace()" style="padding: 10px 25px; font-size: 16px; font-weight: bold; background-color: #27ae60; color: white; border: none; border-radius: 6px; cursor: pointer;">🔄 다른 트랙으로 다시 하기</button>
    </div>
    </body>
    </html>
    """
    components.html(racing_html, height=560)

# ==========================================
# 🚗 4. 도시 자동차 장애물 피하기 (횡단보도 & 맞은편 자동차/실무 그래픽 반영)
# ==========================================
elif st.session_state.current_screen == "obstacle":
    col_nav1, col_nav2 = st.columns([1, 4])
    with col_nav1:
        st.button("🏠 메인으로", on_click=set_screen, args=("home",), use_container_width=True)
    with col_nav2:
        st.subheader("🚗 도시 자동차 장애물 피하기")

    st.caption("조작법 | A/D: 좌우 이동 | Spacebar: 점프 (나무/사람 넘기 시 +5점)")

    obstacle_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; padding: 0; background-color: #1a1a1a; color: #fff; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; }
            #gameContainer { position: relative; width: 500px; height: 580px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); border-radius: 12px; overflow: hidden; }
            canvas { background: #2c3e50; display: block; }
            #menuOverlay, #shopOverlay {
                position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(15, 23, 42, 0.95); display: flex; flex-direction: column;
                align-items: center; justify-content: center; z-index: 10;
            }
            .shop-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; width: 90%; margin-top: 15px; }
            .shop-item { background: #1e293b; border: 2px solid #334155; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer; font-size: 12px; }
            .shop-item.owned { border-color: #38bdf8; }
            .shop-item.equipped { border-color: #2ecc71; background: #064e3b; }
            .btn-menu { padding: 12px 30px; font-size: 18px; font-weight: bold; background: #e74c3c; border: none; color: #fff; border-radius: 6px; margin: 6px; cursor: pointer; }
            .btn-menu:hover { transform: scale(1.05); }
        </style>
    </head>
    <body>

    <div id="gameContainer">
        <div id="menuOverlay">
            <h1 style="color:#f1c40f; margin-bottom:5px;">🚗 장애물 피하기</h1>
            <p id="menuCoinText" style="color:#38bdf8; font-weight:bold; margin-bottom:20px;">보유 코인: 0 개</p>
            <button class="btn-menu" style="background:#27ae60;" onclick="startObstacleGame()">🏁 시작하기</button>
            <button class="btn-menu" style="background:#f39c12;" onclick="openShop()">🏪 상점</button>
            <button class="btn-menu" style="background:#7f8c8d; font-size:14px;" onclick="resetCarData()">🔄 기록 재설정</button>
        </div>

        <div id="shopOverlay" style="display:none;">
            <h2 style="color:#f1c40f; margin-bottom:5px;">🏪 자동차 차종 상점</h2>
            <p id="shopCoinText" style="color:#38bdf8; font-weight:bold;">보유 코인: 0 개</p>
            <div class="shop-grid" id="shopGrid"></div>
            <button class="btn-menu" style="margin-top:15px; background:#e74c3c; font-size:14px; padding:8px 20px;" onclick="closeShop()">닫기</button>
        </div>

        <canvas id="gameCanvas" width="500" height="580"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas"), ctx = canvas.getContext("2d");

        const CAR_MODELS = [
            { id: 0, name: "레드 세단", color: "#e74c3c", price: 0, icon: "🚗" },
            { id: 1, name: "경찰차", color: "#1e293b", price: 500, icon: "🚓" },
            { id: 2, name: "시티 버스", color: "#f39c12", price: 500, icon: "🚌" },
            { id: 3, name: "옐로우 택시", color: "#f1c40f", price: 500, icon: "🚕" },
            { id: 4, name: "블루 스포츠카", color: "#00d2d3", price: 500, icon: "🏎️" },
            { id: 5, name: "그린 SUV", color: "#2ecc71", price: 500, icon: "🚙" },
            { id: 6, name: "골드 리무진", color: "#d4af37", price: 500, icon: "🚘" },
            { id: 7, name: "사이버 픽업", color: "#8e44ad", price: 500, icon: "🛻" }
        ];

        let ownedCars = JSON.parse(localStorage.getItem("car_owned_list") || "[0]");
        let equippedCarId = parseInt(localStorage.getItem("car_equipped_id") || "0");
        let totalCoins = parseInt(localStorage.getItem("car_total_coins") || "0");

        function updateMenuCoins() {
            document.getElementById("menuCoinText").innerText = `보유 코인: ${totalCoins} 개`;
        }
        updateMenuCoins();

        let score = 0, sessionCoins = 0, bonusCoinsFromScore = 0, speed = 6, gameOver = false, gameActive = false, floatText = [];
        let scoreTimer = 0;
        let animationFrameId = null;

        const player = { x: canvas.width / 2 - 22, y: canvas.height - 100, width: 44, height: 75, speed: 7.5, isJumping: false, jumpHeight: 0, jumpVelocity: 0, gravity: 0.85 };
        const keys = { a: false, d: false };

        function startObstacleGame() {
            equippedCarId = parseInt(localStorage.getItem("car_equipped_id") || "0");
            document.getElementById("menuOverlay").style.display = "none";
            gameActive = true;
            restartGame();
        }

        function openShop() {
            document.getElementById("shopCoinText").innerText = `보유 코인: ${totalCoins} 개 (개당 500 코인)`;
            let html = "";
            CAR_MODELS.forEach(car => {
                let isOwned = ownedCars.includes(car.id);
                let isEquipped = equippedCarId === car.id;
                let statusText = isEquipped ? "장착 중" : isOwned ? "선택하기" : "500 🪙 구매";
                let classNames = `shop-item ${isOwned ? 'owned' : ''} ${isEquipped ? 'equipped' : ''}`;
                html += `<div class="${classNames}" onclick="buyOrEquipCar(${car.id})">
                    <div style="font-size:24px;">${car.icon}</div>
                    <div><b>${car.name}</b></div>
                    <div style="color:#2ecc71; margin-top:4px;">${statusText}</div>
                </div>`;
            });
            document.getElementById("shopGrid").innerHTML = html;
            document.getElementById("shopOverlay").style.display = "flex";
        }

        function closeShop() {
            document.getElementById("shopOverlay").style.display = "none";
            updateMenuCoins();
        }

        function buyOrEquipCar(id) {
            if (ownedCars.includes(id)) {
                equippedCarId = id;
                localStorage.setItem("car_equipped_id", equippedCarId.toString());
            } else {
                if (totalCoins >= 500) {
                    totalCoins -= 500;
                    ownedCars.push(id);
                    equippedCarId = id;
                    localStorage.setItem("car_total_coins", totalCoins.toString());
                    localStorage.setItem("car_owned_list", JSON.stringify(ownedCars));
                    localStorage.setItem("car_equipped_id", equippedCarId.toString());
                } else {
                    alert("코인이 부족합니다! (500 코인 필요)");
                }
            }
            openShop();
        }

        function resetCarData() {
            if (confirm("구매 내역과 코인을 초기화하시겠습니까?")) {
                localStorage.removeItem("car_owned_list");
                localStorage.removeItem("car_equipped_id");
                localStorage.removeItem("car_total_coins");
                ownedCars = [0]; equippedCarId = 0; totalCoins = 0;
                updateMenuCoins();
                alert("리셋되었습니다.");
            }
        }

        window.addEventListener("keydown", (e) => {
            if (e.key === "a" || e.key === "A" || e.key === "ㅁ") keys.a = true;
            if (e.key === "d" || e.key === "D" || e.key === "ㅇ") keys.d = true;
            if (e.code === "Space") {
                if (!player.isJumping && !gameOver && gameActive) { player.isJumping = true; player.jumpVelocity = -13.5; }
                if (gameOver && gameActive) restartGame();
                e.preventDefault();
            }
        });
        window.addEventListener("keyup", (e) => {
            if (e.key === "a" || e.key === "A" || e.key === "ㅁ") keys.a = false;
            if (e.key === "d" || e.key === "D" || e.key === "ㅇ") keys.d = false;
        });

        const obstacleTypes = [
            { type: "tree", label: "나무", tag: "[점프가능]", width: 60, height: 60, canJumpOver: true },
            { type: "person", label: "사람", tag: "[점프가능]", width: 35, height: 45, canJumpOver: true },
            { type: "trafficLight", label: "신호등", tag: "[회피필수]", width: 65, height: 60, canJumpOver: false },
            { type: "building", label: "구조물", tag: "[회피필수]", width: 100, height: 75, canJumpOver: false },
            { type: "enemyTruck", label: "대형 트럭", tag: "[회피필수]", width: 48, height: 95, canJumpOver: false },
            { type: "enemyCar", label: "맞은편 승용차", tag: "[회피필수]", width: 44, height: 75, canJumpOver: false }
        ];
        let obstacles = [], coins = [], roadOffset = 0, obstacleTimer = 0, coinTimer = 0;

        function spawnObstacle() {
            const laneWidth = (canvas.width - 100) / 3;
            const lane = Math.floor(Math.random() * 3);
            const x = 50 + lane * laneWidth + (laneWidth / 2);
            const rType = obstacleTypes[Math.floor(Math.random() * obstacleTypes.length)];
            obstacles.push({
                type: rType.type,
                x: x - rType.width / 2,
                y: -120,
                width: rType.width,
                height: rType.height,
                label: rType.label,
                tag: rType.tag,
                canJumpOver: rType.canJumpOver,
                passed: false
            });
        }

        function spawnCoin() {
            const laneWidth = (canvas.width - 100) / 3;
            const lane = Math.floor(Math.random() * 3);
            coins.push({ x: 50 + lane * laneWidth + (laneWidth / 2), y: -40, radius: 15 });
        }

        function update() {
            if (!gameActive || gameOver) return;
            roadOffset = (roadOffset + speed) % 500;

            if (++scoreTimer >= 18) { score += 1; scoreTimer = 0; }

            if (keys.a && player.x > 45) player.x -= player.speed;
            if (keys.d && player.x < canvas.width - 45 - player.width) player.x += player.speed;

            if (player.isJumping) {
                player.jumpHeight += player.jumpVelocity;
                player.jumpVelocity += player.gravity;
                if (player.jumpHeight >= 0) { player.jumpHeight = 0; player.isJumping = false; }
            }

            if (++obstacleTimer > Math.max(18, 40 - Math.floor(score / 30))) { spawnObstacle(); obstacleTimer = 0; }
            if (++coinTimer > 35) { spawnCoin(); coinTimer = 0; }

            for (let i = obstacles.length - 1; i >= 0; i--) {
                let obs = obstacles[i]; 
                let currentObsSpeed = (obs.type === "enemyTruck" || obs.type === "enemyCar") ? speed + 2 : speed;
                obs.y += currentObsSpeed;

                if (obs.canJumpOver && !obs.passed && player.y < obs.y && player.jumpHeight < -20 && Math.abs((player.x + player.width/2) - (obs.x + obs.width/2)) < 45) {
                    obs.passed = true;
                    score += 5;
                    floatText.push({ x: player.x + 20, y: player.y + player.jumpHeight, text: "+5점 점프!", alpha: 1.0 });
                }

                if (player.x < obs.x + obs.width && player.x + player.width > obs.x && player.y < obs.y + obs.height && player.y + player.height > obs.y) {
                    if (!(obs.canJumpOver && player.jumpHeight < -22)) {
                        gameOver = true;
                        bonusCoinsFromScore = Math.floor(score / 5);
                        totalCoins += (sessionCoins + bonusCoinsFromScore);
                        localStorage.setItem("car_total_coins", totalCoins.toString());
                        updateMenuCoins();
                    }
                }
                if (obs.y > canvas.height + 50) obstacles.splice(i, 1);
            }

            for (let i = coins.length - 1; i >= 0; i--) {
                let c = coins[i]; c.y += speed;
                let dist = Math.hypot((player.x + player.width/2) - c.x, (player.y + player.jumpHeight + player.height/2) - c.y);
                if (dist < c.radius + player.width/2 + 10) {
                    coins.splice(i, 1);
                    sessionCoins += 2;
                    floatText.push({ x: c.x, y: c.y, text: "+2 🪙", alpha: 1.0 });
                } else if (c.y > canvas.height) coins.splice(i, 1);
            }

            for (let i = floatText.length - 1; i >= 0; i--) {
                floatText[i].y -= 2;
                floatText[i].alpha -= 0.03;
                if (floatText[i].alpha <= 0) floatText.splice(i, 1);
            }
        }

        function drawObstacleDetail(o) {
            ctx.save();
            ctx.translate(o.x, o.y);

            if (o.type === "tree") {
                ctx.fillStyle = "#78350f"; ctx.fillRect(o.width/2 - 6, o.height - 18, 12, 18);
                ctx.fillStyle = "#15803d";
                ctx.beginPath(); ctx.arc(o.width/2, 22, 22, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#22c55e";
                ctx.beginPath(); ctx.arc(o.width/2 - 8, 16, 14, 0, Math.PI*2); ctx.fill();
                ctx.beginPath(); ctx.arc(o.width/2 + 8, 16, 12, 0, Math.PI*2); ctx.fill();
            } else if (o.type === "person") {
                ctx.fillStyle = "#fde047"; ctx.beginPath(); ctx.arc(o.width/2, 8, 7, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#2563eb"; ctx.fillRect(o.width/2 - 8, 16, 16, 16);
                ctx.fillStyle = "#1e293b"; ctx.fillRect(o.width/2 - 7, 32, 6, 12); ctx.fillRect(o.width/2 + 1, 32, 6, 12);
            } else if (o.type === "trafficLight") {
                ctx.fillStyle = "#475569"; ctx.fillRect(o.width/2 - 4, 25, 8, o.height - 25);
                ctx.fillStyle = "#0f172a"; ctx.beginPath(); ctx.roundRect(o.width/2 - 25, 0, 50, 25, 4); ctx.fill();
                ctx.fillStyle = "#ef4444"; ctx.beginPath(); ctx.arc(o.width/2 - 14, 12, 7, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#eab308"; ctx.beginPath(); ctx.arc(o.width/2, 12, 7, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#22c55e"; ctx.beginPath(); ctx.arc(o.width/2 + 14, 12, 7, 0, Math.PI*2); ctx.fill();
            } else if (o.type === "building") {
                ctx.fillStyle = "#334155"; ctx.fillRect(0, 0, o.width, o.height);
                ctx.fillStyle = "#f8fafc";
                for(let r=8; r<o.height-12; r+=18) {
                    for(let c=10; c<o.width-15; c+=20) {
                        ctx.fillRect(c, r, 10, 10);
                    }
                }
            } else if (o.type === "enemyTruck") {
                ctx.fillStyle = "#94a3b8"; ctx.fillRect(2, 0, o.width - 4, o.height - 25);
                ctx.fillStyle = "#dc2626"; ctx.beginPath(); ctx.roundRect(0, o.height - 25, o.width, 25, 4); ctx.fill();
                ctx.fillStyle = "#1e293b"; ctx.fillRect(4, o.height - 18, o.width - 8, 10);
                ctx.fillStyle = "#fef08a"; ctx.fillRect(4, o.height - 3, 8, 3); ctx.fillRect(o.width - 12, o.height - 3, 8, 3);
            } else if (o.type === "enemyCar") {
                ctx.fillStyle = "#2563eb"; ctx.beginPath(); ctx.roundRect(0, 0, o.width, o.height, 8); ctx.fill();
                ctx.fillStyle = "#0284c7"; ctx.fillRect(5, 35, o.width - 10, 18);
                ctx.fillStyle = "#fef08a"; ctx.fillRect(4, o.height - 4, 7, 4); ctx.fillRect(o.width - 11, o.height - 4, 7, 4);
            }

            ctx.restore();
        }

        function drawCustomCar(x, y, modelId) {
            const w = player.width;
            const h = player.height;

            ctx.fillStyle = "#111";
            ctx.fillRect(x - 3, y + 10, 5, 16);
            ctx.fillRect(x + w - 2, y + 10, 5, 16);
            ctx.fillRect(x - 3, y + h - 26, 5, 16);
            ctx.fillRect(x + w - 2, y + h - 26, 5, 16);

            if (modelId === 0) {
                ctx.fillStyle = "#e74c3c"; ctx.beginPath(); ctx.roundRect(x, y, w, h, 8); ctx.fill();
                ctx.fillStyle = "#3498db"; ctx.fillRect(x + 5, y + 18, w - 10, 16);
                ctx.fillStyle = "#2c3e50"; ctx.fillRect(x + 7, y + 22, w - 14, 10);
            } else if (modelId === 1) {
                ctx.fillStyle = "#0f172a"; ctx.beginPath(); ctx.roundRect(x, y, w, h, 6); ctx.fill();
                ctx.fillStyle = "#f8fafc"; ctx.fillRect(x + 4, y + 14, w - 8, 38);
                ctx.fillStyle = "#38bdf8"; ctx.fillRect(x + 6, y + 18, w - 12, 14);
                ctx.fillStyle = "#ef4444"; ctx.fillRect(x + w/2 - 12, y + 23, 10, 5);
                ctx.fillStyle = "#3b82f6"; ctx.fillRect(x + w/2 + 2, y + 23, 10, 5);
            } else if (modelId === 2) {
                ctx.fillStyle = "#f39c12"; ctx.beginPath(); ctx.roundRect(x - 2, y - 5, w + 4, h + 10, 4); ctx.fill();
                ctx.fillStyle = "#34495e"; ctx.fillRect(x + 3, y + 4, w - 6, 12);
                ctx.fillRect(x + 3, y + 22, w - 6, 32);
                ctx.fillStyle = "#ecf0f1"; ctx.fillRect(x + 5, y + 24, w - 10, 28);
            } else if (modelId === 3) {
                ctx.fillStyle = "#f1c40f"; ctx.beginPath(); ctx.roundRect(x, y, w, h, 8); ctx.fill();
                ctx.fillStyle = "#2c3e50"; ctx.fillRect(x + 5, y + 18, w - 10, 16);
                ctx.fillStyle = "#111"; ctx.fillRect(x + w/2 - 10, y + 22, 20, 7);
                ctx.fillStyle = "#f1c40f"; ctx.font = "bold 6px sans-serif"; ctx.textAlign = "center"; ctx.fillText("TAXI", x + w/2, y + 27);
            } else if (modelId === 4) {
                ctx.fillStyle = "#00d2d3"; ctx.beginPath(); ctx.roundRect(x, y + 4, w, h - 8, 12); ctx.fill();
                ctx.fillStyle = "#2e86de"; ctx.fillRect(x + 6, y + 20, w - 12, 14);
                ctx.fillStyle = "#ff6b6b"; ctx.fillRect(x - 3, y + h - 10, w + 6, 5);
            } else if (modelId === 5) {
                ctx.fillStyle = "#2ecc71"; ctx.beginPath(); ctx.roundRect(x - 1, y, w + 2, h, 5); ctx.fill();
                ctx.fillStyle = "#1ea252"; ctx.fillRect(x + 4, y + 15, w - 8, 22);
                ctx.fillStyle = "#111"; ctx.beginPath(); ctx.arc(x + w/2, y + h - 2, 8, 0, Math.PI * 2); ctx.fill();
                ctx.fillStyle = "#7f8c8d"; ctx.beginPath(); ctx.arc(x + w/2, y + h - 2, 4, 0, Math.PI * 2); ctx.fill();
            } else if (modelId === 6) {
                ctx.fillStyle = "#d4af37"; ctx.beginPath(); ctx.roundRect(x, y - 6, w, h + 12, 6); ctx.fill();
                ctx.fillStyle = "#f1c40f"; ctx.fillRect(x + 5, y + 12, w - 10, 36);
                ctx.fillStyle = "#111"; ctx.fillRect(x + 7, y + 15, w - 14, 30);
            } else if (modelId === 7) {
                ctx.fillStyle = "#8e44ad"; ctx.beginPath(); ctx.roundRect(x, y, w, h, 4); ctx.fill();
                ctx.fillStyle = "#00d2d3"; ctx.fillRect(x + 5, y + 12, w - 10, 14);
                ctx.fillStyle = "#2c3e50"; ctx.fillRect(x + 4, y + 36, w - 8, 28);
            }

            ctx.fillStyle = "#fef08a";
            ctx.fillRect(x + 4, y + 2, 7, 4);
            ctx.fillRect(x + w - 11, y + 2, 7, 4);
        }

        function draw() {
            ctx.fillStyle = "#1e293b"; ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#334155"; ctx.fillRect(40, 0, canvas.width - 80, canvas.height);

            ctx.strokeStyle = "#f1c40f"; ctx.lineWidth = 4; ctx.setLineDash([20, 20]); ctx.lineDashOffset = -roadOffset;
            ctx.beginPath(); ctx.moveTo(canvas.width/3 + 10, 0); ctx.lineTo(canvas.width/3 + 10, canvas.height); ctx.stroke();
            ctx.beginPath(); ctx.moveTo((canvas.width/3)*2 - 10, 0); ctx.lineTo((canvas.width/3)*2 - 10, canvas.height); ctx.stroke();
            ctx.setLineDash([]);

            const crosswalkY = (roadOffset * 2) % 600 - 100;
            ctx.fillStyle = "#f8fafc";
            for(let cx = 45; cx < canvas.width - 45; cx += 35) {
                ctx.fillRect(cx, crosswalkY, 22, 55);
            }

            coins.forEach(c => {
                ctx.fillStyle = "#f1c40f"; ctx.beginPath(); ctx.arc(c.x, c.y, c.radius, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#fff"; ctx.font = "bold 13px sans-serif"; ctx.textAlign = "center"; ctx.fillText("★", c.x, c.y + 3);
            });

            obstacles.forEach(o => {
                drawObstacleDetail(o);
            });

            const rY = player.y + player.jumpHeight;
            drawCustomCar(player.x, rY, equippedCarId);

            floatText.forEach(ft => { ctx.fillStyle = `rgba(241, 196, 15, ${ft.alpha})`; ctx.font = "bold 20px sans-serif"; ctx.fillText(ft.text, ft.x, ft.y); });

            ctx.fillStyle = "#fff"; ctx.font = "bold 18px sans-serif"; ctx.textAlign = "left";
            ctx.fillText(`SCORE: ${score}`, 20, 35);
            ctx.fillText(`🪙 획득 코인: ${sessionCoins}`, 20, 60);

            ctx.fillStyle = "#f39c12"; ctx.fillRect(canvas.width - 110, 15, 90, 35);
            ctx.fillStyle = "#fff"; ctx.font = "bold 14px sans-serif"; ctx.textAlign = "center"; ctx.fillText("🏪 상점", canvas.width - 65, 38);

            if (gameOver) {
                ctx.fillStyle = "rgba(0,0,0,0.85)"; ctx.fillRect(0,0,canvas.width,canvas.height);
                ctx.fillStyle = "#e74c3c"; ctx.font = "bold 38px sans-serif"; ctx.textAlign = "center"; ctx.fillText("GAME OVER", canvas.width/2, canvas.height/2 - 60);
                ctx.fillStyle = "#fff"; ctx.font = "18px sans-serif"; ctx.fillText(`최종 완주 점수: ${score} 점`, canvas.width/2, canvas.height/2 - 10);
                ctx.fillText(`획득 코인: +${sessionCoins} 개`, canvas.width/2, canvas.height/2 + 20);
                ctx.fillStyle = "#2ecc71"; ctx.fillText(`🎁 점수 보너스(5점당 1개): +${bonusCoinsFromScore} 코인`, canvas.width/2, canvas.height/2 + 50);
                ctx.fillStyle = "#f39c12"; ctx.font = "16px sans-serif"; ctx.fillText("[ Spacebar ] 눌러 다시 시작", canvas.width/2, canvas.height/2 + 95);
            }
        }

        canvas.addEventListener("click", (e) => {
            const rect = canvas.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const clickY = e.clientY - rect.top;
            if (clickX > canvas.width - 110 && clickX < canvas.width - 20 && clickY > 15 && clickY < 50) {
                openShop();
            }
        });

        function restartGame() {
            if (animationFrameId) cancelAnimationFrame(animationFrameId);
            score = 0; sessionCoins = 0; bonusCoinsFromScore = 0; speed = 6; gameOver = false; obstacles = []; coins = []; player.x = canvas.width/2 - 22; loop();
        }

        function loop() {
            update();
            draw();
            if (!gameOver && gameActive) {
                animationFrameId = requestAnimationFrame(loop);
            }
        }
    </script>
    </body>
    </html>
    """
    components.html(obstacle_html, height=610)

# ==========================================
# 🧗‍♂️ 5. 건강의 다리
# ==========================================
elif st.session_state.current_screen == "stairs":
    col_nav1, col_nav2 = st.columns([1, 4])
    with col_nav1:
        st.button("🏠 메인으로", on_click=set_screen, args=("home",), use_container_width=True)
    with col_nav2:
        st.subheader("🧗‍♂️ 건강의 다리 (Infinite Health Bridge)")

    st.caption("조작법 | A: 오르기 | D: 방향틀기 | Z 키: 50코인으로 200계단 부스터! | Space/Enter: 재시작")

    stairs_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; padding: 0; background-color: #0b0c10; color: #fff; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; }
            #gameContainer { position: relative; width: 480px; height: 600px; box-shadow: 0 10px 30px rgba(0,0,0,0.9); border-radius: 12px; overflow: hidden; border: 2px solid #334155; }
            canvas { background: #020617; display: block; }
            #charSelectOverlay {
                position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(2, 6, 23, 0.95); display: flex; flex-direction: column;
                align-items: center; justify-content: center; z-index: 10;
            }
            .char-box { display: flex; gap: 15px; margin-top: 15px; }
            .char-card {
                width: 125px; padding: 12px; background: #0f172a; border: 2px solid #334155;
                border-radius: 10px; text-align: center; cursor: pointer; transition: 0.2s;
            }
            .char-card:hover { transform: translateY(-5px); border-color: #f1c40f; }
            .char-card.selected { border-color: #2ecc71; background: #1e293b; }
            .btn-start {
                margin-top: 20px; padding: 12px 35px; font-size: 20px; font-weight: bold; color: #fff;
                background: #e74c3c; border: none; border-radius: 8px; cursor: pointer;
            }
            .btn-start:hover { background: #c0392b; }
            .btn-reset { background: #7f8c8d; font-size: 13px; padding: 6px 14px; margin-top: 10px; border:none; border-radius:4px; color:#fff; cursor:pointer;}
            .btn-booster-start { background: #38bdf8; color:#0f172a; font-weight:bold; padding:8px 16px; border:none; border-radius:6px; margin-top:10px; cursor:pointer; }
        </style>
    </head>
    <body>

    <div id="gameContainer">
        <div id="charSelectOverlay">
            <h1 style="color:#f1c40f; margin-bottom:5px;">🧗‍♂️ 건강의 다리</h1>
            <p id="bestRecordText" style="color:#2ecc71; font-weight:bold; font-size:15px;">🏆 최고 기록: 0 계단 | 🪙 보유 코인: 0 개</p>
            <button class="btn-booster-start" onclick="useBoosterInMenu()">⚡ Z 키 부스터 구매 (50코인 = +200계단)</button>

            <div class="char-box">
                <div class="char-card selected" id="char0" onclick="selectChar(0)">
                    <svg width="45" height="45" viewBox="0 0 40 40">
                        <circle cx="20" cy="12" r="8" fill="#38bdf8"/>
                        <rect x="12" y="20" width="16" height="15" rx="3" fill="#0284c7"/>
                        <rect x="8" y="22" width="6" height="10" rx="2" fill="#38bdf8"/>
                        <rect x="26" y="22" width="6" height="10" rx="2" fill="#38bdf8"/>
                    </svg>
                    <div style="font-weight:bold; margin-top:3px; color:#38bdf8; font-size:13px;">블루 히어로</div>
                </div>
                <div class="char-card" id="char1" onclick="selectChar(1)">
                    <svg width="45" height="45" viewBox="0 0 40 40">
                        <circle cx="20" cy="12" r="8" fill="#facc15"/>
                        <path d="M12 20 L28 20 L24 35 L16 35 Z" fill="#ca8a04"/>
                        <rect x="10" y="10" width="20" height="5" fill="#eab308"/>
                    </svg>
                    <div style="font-weight:bold; margin-top:3px; color:#facc15; font-size:13px;">골드 닌자</div>
                </div>
                <div class="char-card" id="char2" onclick="selectChar(2)">
                    <svg width="45" height="45" viewBox="0 0 40 40">
                        <rect x="12" y="6" width="16" height="12" rx="2" fill="#c084fc"/>
                        <rect x="10" y="20" width="20" height="15" rx="4" fill="#7e22ce"/>
                        <circle cx="16" cy="11" r="2" fill="#06b6d4"/>
                        <circle cx="24" cy="11" r="2" fill="#06b6d4"/>
                    </svg>
                    <div style="font-weight:bold; margin-top:3px; color:#c084fc; font-size:13px;">사이보그 봇</div>
                </div>
            </div>

            <button class="btn-start" onclick="startGame()">▶️ 도전 시작</button>
            <button class="btn-reset" onclick="resetBridgeData()">🔄 기록 리셋</button>
        </div>
        <canvas id="gameCanvas" width="480" height="600"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const STAIR_WIDTH = 75;
        const STAIR_HEIGHT = 32;

        let selectedCharIndex = 0;
        let score = 0;
        let coinsCollected = 0;
        let timer = 100;
        let gameOver = false;
        let gameActive = false;
        let isNewRecord = false;

        let boosterCount = 0;
        let isBoosterActive = false;

        let highScore = parseInt(localStorage.getItem("stairs_high_score") || "0");
        let totalCoins = parseInt(localStorage.getItem("car_total_coins") || "0");

        function updateBestDisplay() {
            document.getElementById("bestRecordText").innerText = `🏆 최고 기록: ${highScore} 계단 | 🪙 보유 코인: ${totalCoins} 개`;
        }
        updateBestDisplay();

        function resetBridgeData() {
            if (confirm("건강의 다리 기록을 리셋하시겠습니까?")) {
                localStorage.removeItem("stairs_high_score");
                localStorage.removeItem("car_total_coins");
                highScore = 0; totalCoins = 0;
                updateBestDisplay();
            }
        }

        let stairs = [];
        let stars = [];
        let clouds = [];

        let playerState = { stairIndex: 0, dir: 1, x: 240, y: 420 };

        for (let i = 0; i < 60; i++) {
            stars.push({ x: Math.random() * canvas.width, y: Math.random() * canvas.height, r: Math.random() * 2, alpha: Math.random() });
        }
        for (let i = 0; i < 5; i++) {
            clouds.push({ x: Math.random() * canvas.width, y: Math.random() * canvas.height, speed: 0.15 + Math.random() * 0.25, size: 30 + Math.random() * 25 });
        }

        function selectChar(idx) {
            selectedCharIndex = idx;
            document.querySelectorAll(".char-card").forEach((card, i) => {
                if (i === idx) card.classList.add("selected");
                else card.classList.remove("selected");
            });
        }

        function generateStairs() {
            stairs = [];
            let currentX = 240;
            let currentY = 420;
            let currentDir = 1;

            stairs.push({ x: currentX, y: currentY, dir: currentDir, hasCoin: false, type: 0 });

            for (let i = 1; i < 400; i++) {
                if (Math.random() < 0.38 && i > 2) currentDir = -currentDir;
                currentX += currentDir * (STAIR_WIDTH - 15);
                currentY -= STAIR_HEIGHT;
                const stairType = Math.floor(i / 15) % 4;
                stairs.push({ x: currentX, y: currentY, dir: currentDir, hasCoin: Math.random() < 0.28, type: stairType });
            }
        }

        function startGame() {
            document.getElementById("charSelectOverlay").style.display = "none";
            score = 0;
            coinsCollected = 0;
            timer = 100;
            gameOver = false;
            gameActive = true;
            isNewRecord = false;
            isBoosterActive = false;
            boosterCount = 0;

            generateStairs();
            playerState.stairIndex = 0;
            playerState.dir = 1;
            playerState.x = stairs[0].x;
            playerState.y = stairs[0].y;
        }

        function trigger200Booster() {
            if (totalCoins < 50 && coinsCollected < 50) {
                alert("코인이 부족합니다! (50 코인 필요)");
                return;
            }

            if (totalCoins >= 50) {
                totalCoins -= 50;
                localStorage.setItem("car_total_coins", totalCoins.toString());
            } else {
                coinsCollected -= 50;
            }

            updateBestDisplay();
            isBoosterActive = true;
            boosterCount = 200;
        }

        function useBoosterInMenu() {
            if (totalCoins >= 50) {
                startGame();
                trigger200Booster();
            } else {
                alert("보유 코인이 부족합니다! (50 코인 필요)");
            }
        }

        function handleGameOver() {
            gameOver = true;
            totalCoins += coinsCollected;
            localStorage.setItem("car_total_coins", totalCoins.toString());

            if (score > highScore) {
                highScore = score;
                localStorage.setItem("stairs_high_score", highScore.toString());
                isNewRecord = true;
            }
            updateBestDisplay();
        }

        window.addEventListener("keydown", (e) => {
            if (e.key === "z" || e.key === "Z" || e.key === "ㅋ") {
                if (gameActive && !gameOver && !isBoosterActive) {
                    trigger200Booster();
                }
                return;
            }

            if (gameOver && (e.code === "Space" || e.code === "Enter")) {
                startGame();
                e.preventDefault();
                return;
            }

            if (!gameActive || gameOver || isBoosterActive) return;

            if (e.key === "a" || e.key === "A" || e.key === "ㅁ" || e.key === "ArrowLeft") {
                climb(false);
            } else if (e.key === "d" || e.key === "D" || e.key === "ㅇ" || e.key === "ArrowRight") {
                climb(true);
            }
        });

        function climb(turn) {
            if (turn) playerState.dir = -playerState.dir;

            const nextIndex = playerState.stairIndex + 1;
            const targetStair = stairs[nextIndex];
            const expectedDir = (targetStair.x > stairs[playerState.stairIndex].x) ? 1 : -1;

            if (playerState.dir === expectedDir) {
                playerState.stairIndex = nextIndex;
                score++;
                timer = Math.min(100, timer + 10);

                if (targetStair.hasCoin) {
                    targetStair.hasCoin = false;
                    coinsCollected++;
                    score += 5;
                }

                if (stairs.length - playerState.stairIndex < 50) {
                    let lastStair = stairs[stairs.length - 1];
                    let nextDir = lastStair.dir;
                    if (Math.random() < 0.38) nextDir = -nextDir;
                    const nextType = Math.floor(stairs.length / 15) % 4;
                    stairs.push({
                        x: lastStair.x + nextDir * (STAIR_WIDTH - 15),
                        y: lastStair.y - STAIR_HEIGHT,
                        dir: nextDir,
                        hasCoin: Math.random() < 0.28,
                        type: nextType
                    });
                }
            } else {
                handleGameOver();
            }
        }

        function update() {
            if (!gameActive || gameOver) return;

            if (isBoosterActive && boosterCount > 0) {
                const nextIndex = playerState.stairIndex + 1;
                const targetStair = stairs[nextIndex];
                playerState.dir = (targetStair.x > stairs[playerState.stairIndex].x) ? 1 : -1;
                playerState.stairIndex = nextIndex;
                score++;
                boosterCount--;

                if (targetStair.hasCoin) {
                    targetStair.hasCoin = false;
                    coinsCollected++;
                    score += 5;
                }

                if (stairs.length - playerState.stairIndex < 50) {
                    let lastStair = stairs[stairs.length - 1];
                    let nextDir = lastStair.dir;
                    if (Math.random() < 0.38) nextDir = -nextDir;
                    stairs.push({
                        x: lastStair.x + nextDir * (STAIR_WIDTH - 15),
                        y: lastStair.y - STAIR_HEIGHT,
                        dir: nextDir,
                        hasCoin: Math.random() < 0.28,
                        type: Math.floor(stairs.length / 15) % 4
                    });
                }

                if (boosterCount <= 0) {
                    isBoosterActive = false;
                }
                return;
            }

            const speedMultiplier = 1 + Math.floor(score / 100) * 0.45;
            timer -= (0.22 + Math.min(0.65, score * 0.0035)) * speedMultiplier;

            if (timer <= 0) { timer = 0; handleGameOver(); }

            clouds.forEach(c => {
                c.x += c.speed;
                if (c.x > canvas.width + 60) c.x = -60;
            });
        }

        function drawNightSpaceBackground() {
            let grad = ctx.createLinearGradient(0, 0, 0, canvas.height);
            grad.addColorStop(0, "#020617");
            grad.addColorStop(0.5, "#1e1b4b");
            grad.addColorStop(1, "#311042");
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            stars.forEach(s => {
                ctx.fillStyle = `rgba(255, 255, 255, ${0.3 + Math.sin(Date.now() * 0.003 + s.alpha * 10) * 0.5})`;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ctx.fill();
            });

            clouds.forEach(c => {
                ctx.fillStyle = "rgba(148, 163, 184, 0.12)";
                ctx.beginPath();
                ctx.arc(c.x, c.y, c.size, 0, Math.PI * 2);
                ctx.arc(c.x + 20, c.y - 10, c.size * 0.8, 0, Math.PI * 2);
                ctx.arc(c.x - 20, c.y + 5, c.size * 0.7, 0, Math.PI * 2);
                ctx.fill();
            });
        }

        function drawClearCharacter(x, y, dir) {
            ctx.save();
            ctx.translate(x, y);
            if (dir === -1) ctx.scale(-1, 1);

            if (selectedCharIndex === 0) {
                ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(0, -28, 9, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#0284c7"; ctx.fillRect(-8, -18, 16, 18);
                ctx.fillStyle = "#f8fafc"; ctx.fillRect(-5, -28, 12, 4);
                ctx.fillStyle = "#38bdf8"; ctx.fillRect(-7, 0, 6, 10); ctx.fillRect(1, 0, 6, 10);
            } else if (selectedCharIndex === 1) {
                ctx.fillStyle = "#facc15"; ctx.beginPath(); ctx.arc(0, -28, 9, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = "#ca8a04"; ctx.fillRect(-8, -18, 16, 18);
                ctx.fillStyle = "#ef4444"; ctx.fillRect(-10, -22, 20, 4);
                ctx.fillStyle = "#eab308"; ctx.fillRect(-7, 0, 6, 10); ctx.fillRect(1, 0, 6, 10);
            } else {
                ctx.fillStyle = "#c084fc"; ctx.fillRect(-8, -34, 16, 12);
                ctx.fillStyle = "#06b6d4"; ctx.fillRect(-4, -30, 4, 3); ctx.fillRect(2, -30, 4, 3);
                ctx.fillStyle = "#7e22ce"; ctx.fillRect(-9, -20, 18, 20);
                ctx.fillStyle = "#a855f7"; ctx.fillRect(-7, 0, 6, 10); ctx.fillRect(1, 0, 6, 10);
            }

            ctx.restore();
        }

        function draw() {
            drawNightSpaceBackground();

            if (!gameActive) return;

            const currentStair = stairs[playerState.stairIndex];

            ctx.save();
            ctx.translate(canvas.width / 2 - currentStair.x, canvas.height / 2 + 120 - currentStair.y);

            stairs.forEach((s, idx) => {
                if (Math.abs(idx - playerState.stairIndex) > 25) return;

                let topColor = "#94a3b8", sideColor = "#475569";
                if (s.type === 1) { topColor = "#d97706"; sideColor = "#78350f"; }
                else if (s.type === 2) { topColor = "#f8fafc"; sideColor = "#94a3b8"; }
                else if (s.type === 3) { topColor = "#a855f7"; sideColor = "#581c87"; }

                ctx.fillStyle = topColor;
                ctx.fillRect(s.x - STAIR_WIDTH/2, s.y, STAIR_WIDTH, STAIR_HEIGHT);

                ctx.fillStyle = sideColor;
                ctx.fillRect(s.x - STAIR_WIDTH/2, s.y + 12, STAIR_WIDTH, STAIR_HEIGHT - 12);

                ctx.strokeStyle = "rgba(0,0,0,0.3)";
                ctx.lineWidth = 2;
                ctx.strokeRect(s.x - STAIR_WIDTH/2, s.y, STAIR_WIDTH, STAIR_HEIGHT);

                if (s.hasCoin) {
                    ctx.fillStyle = "#f59e0b";
                    ctx.beginPath();
                    ctx.arc(s.x, s.y - 18, 11, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.fillStyle = "#fef08a";
                    ctx.font = "bold 12px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText("★", s.x, s.y - 14);
                }
            });

            drawClearCharacter(currentStair.x, currentStair.y, playerState.dir);

            ctx.restore();

            ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
            ctx.fillRect(40, 25, canvas.width - 80, 18);

            const timerWidth = ((canvas.width - 84) * timer) / 100;
            ctx.fillStyle = isBoosterActive ? "#f1c40f" : (timer > 30 ? "#38bdf8" : "#f43f5e");
            ctx.fillRect(42, 27, Math.max(0, timerWidth), 14);

            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 34px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText(`${score}`, canvas.width / 2, 85);

            ctx.fillStyle = "#f59e0b";
            ctx.font = "bold 15px sans-serif";
            ctx.textAlign = "left";
            ctx.fillText(`🪙 COINS: ${coinsCollected}`, 20, 40);

            ctx.fillStyle = "#38bdf8";
            ctx.font = "bold 15px sans-serif";
            ctx.textAlign = "right";
            ctx.fillText(`🏆 BEST: ${highScore}`, canvas.width - 20, 40);

            if (isBoosterActive) {
                ctx.fillStyle = "#f1c40f";
                ctx.font = "bold 20px sans-serif";
                ctx.textAlign = "center";
                ctx.fillText(`⚡ 200계단 폭풍 부스터 진행 중!! (${boosterCount})`, canvas.width / 2, 120);
            }

            if (gameOver) {
                ctx.fillStyle = "rgba(2, 6, 23, 0.88)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#f43f5e";
                ctx.font = "bold 38px sans-serif";
                ctx.textAlign = "center";
                ctx.fillText("GAME OVER", canvas.width / 2, canvas.height / 2 - 50);

                if (isNewRecord) {
                    ctx.fillStyle = "#facc15";
                    ctx.font = "bold 20px sans-serif";
                    ctx.fillText("🎉 축하합니다! 최고 기록 경신!", canvas.width / 2, canvas.height / 2 - 10);
                }

                ctx.fillStyle = "#f8fafc";
                ctx.font = "20px sans-serif";
                ctx.fillText(`이번 기록: ${score} 계단`, canvas.width / 2, canvas.height / 2 + 25);
                ctx.fillText(`🏆 최고 기록: ${highScore} 계단`, canvas.width / 2, canvas.height / 2 + 55);

                ctx.fillStyle = "#38bdf8";
                ctx.font = "bold 17px sans-serif";
                ctx.fillText("[ Spacebar / Enter ] 즉시 다시 시작", canvas.width / 2, canvas.height / 2 + 105);
            }
        }

        function loop() {
            update();
            draw();
            requestAnimationFrame(loop);
        }
        loop();
    </script>

    <div style="text-align: center; margin-top: 10px; display: flex; justify-content: center; gap: 10px;">
        <button onclick="climb(false)" style="padding: 10px 20px; font-size: 16px; font-weight: bold; background-color: #0284c7; color: white; border: none; border-radius: 8px; cursor: pointer;">🅰️ 오르기 (A)</button>
        <button onclick="climb(true)" style="padding: 10px 20px; font-size: 16px; font-weight: bold; background-color: #d97706; color: white; border: none; border-radius: 8px; cursor: pointer;">🇩 방향틀기 (D)</button>
        <button onclick="trigger200Booster()" style="padding: 10px 20px; font-size: 16px; font-weight: bold; background-color: #f1c40f; color: #111; border: none; border-radius: 8px; cursor: pointer;">⚡ Z (50코인 부스터)</button>
    </div>

    </body>
    </html>
    """
    components.html(stairs_html, height=660)
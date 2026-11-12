
import streamlit as st
from datetime import date, datetime

st.set_page_config(page_title="Smart Food Manager", page_icon="🥗", layout="wide")

# 음식 데이터: 분류 | 음식 이름 | 대표 재료
DATA = """
한식|김치찌개|김치,돼지고기,두부,대파
한식|된장찌개|된장,두부,애호박,양파,감자
한식|순두부찌개|순두부,고춧가루,달걀,대파
한식|부대찌개|햄,소시지,김치,두부,대파
한식|고추장찌개|고추장,돼지고기,감자,양파
한식|미역국|미역,소고기,마늘
한식|소고기뭇국|소고기,무,대파,마늘
한식|콩나물국|콩나물,대파,마늘
한식|북엇국|북어,달걀,무,대파
한식|떡국|떡,소고기,달걀,대파
한식|육개장|소고기,고사리,숙주,대파
한식|불고기|소고기,양파,당근,대파
한식|제육볶음|돼지고기,고추장,양파,대파
한식|찜닭|닭고기,감자,당근,양파
한식|닭볶음탕|닭고기,감자,당근,양파
한식|닭갈비|닭고기,양배추,고구마,대파
한식|잡채|당면,돼지고기,당근,양파,시금치
한식|비빔밥|밥,달걀,당근,시금치,콩나물
한식|김치볶음밥|밥,김치,달걀,대파
한식|새우볶음밥|밥,새우,달걀,당근,대파
한식|오므라이스|밥,달걀,양파,당근,케첩
한식|계란볶음밥|밥,달걀,대파,당근
한식|김밥|김,밥,달걀,당근,단무지
한식|참치김밥|김,밥,참치,달걀,단무지
한식|주먹밥|밥,김,참치,마요네즈
한식|감자조림|감자,간장,양파
한식|두부조림|두부,간장,대파,고춧가루
한식|계란말이|달걀,당근,대파
한식|계란찜|달걀,대파,당근
한식|애호박볶음|애호박,양파,마늘
한식|고등어구이|고등어,레몬
한식|갈치조림|갈치,무,양파,대파
한식|콩나물무침|콩나물,마늘,대파
한식|시금치나물|시금치,마늘
한식|파전|부침가루,대파,달걀,오징어
한식|김치전|김치,부침가루,양파
한식|감자전|감자,양파
한식|떡볶이|떡,어묵,고추장,대파
한식|라볶이|라면,떡,어묵,고추장
한식|잔치국수|소면,달걀,애호박,당근
한식|비빔국수|소면,오이,고추장,달걀
한식|수제비|밀가루,감자,애호박,양파
한식|칼국수|칼국수면,감자,애호박,바지락
한식|만둣국|만두,달걀,대파
한식|오징어볶음|오징어,양파,당근,대파
한식|두부김치|두부,김치,돼지고기
한식|카레라이스|밥,카레,감자,당근,양파
한식|소불고기덮밥|밥,소고기,양파,당근
한식|마파두부덮밥|밥,두부,돼지고기,대파
한식|참치마요덮밥|밥,참치,마요네즈,달걀
한식|버섯전골|버섯,두부,배추,대파
한식|오이무침|오이,고춧가루,양파
한식|무생채|무,고춧가루,대파
한식|어묵볶음|어묵,양파,당근,대파
한식|순대볶음|순대,양배추,양파,대파
한식|고구마맛탕|고구마,설탕
한식|간장계란밥|밥,달걀,간장,참기름
한식|김치콩나물국|김치,콩나물,대파
한식|소시지야채볶음|소시지,양파,피망,당근
한식|부추전|부추,부침가루,달걀
한식|닭강정|닭고기,전분,간장
한식|감자탕|돼지고기,감자,우거지,대파
한식|떡만둣국|떡,만두,달걀,대파
중식|짜장면|중화면,춘장,돼지고기,양파
중식|짬뽕|중화면,오징어,새우,양배추,양파
중식|탕수육|돼지고기,전분,당근,오이
중식|깐풍기|닭고기,전분,마늘,고추
중식|마파두부|두부,돼지고기,대파,두반장
중식|볶음밥|밥,달걀,당근,양파,대파
중식|고추잡채|돼지고기,피망,양파,꽃빵
중식|마라탕|마라소스,청경채,숙주,두부,버섯
중식|마라샹궈|마라소스,소시지,청경채,연근
중식|군만두|만두,식용유
중식|볶음우동|우동면,양배추,양파,돼지고기
중식|새우칠리|새우,토마토,마늘,고추
중식|토마토달걀볶음|토마토,달걀,대파
일식|돈가스|돼지고기,달걀,빵가루,양배추
일식|치킨가스|닭고기,달걀,빵가루,양배추
일식|규동|밥,소고기,양파,달걀
일식|가츠동|밥,돼지고기,달걀,양파
일식|오야코동|밥,닭고기,달걀,양파
일식|연어덮밥|밥,연어,아보카도,오이
일식|참치덮밥|밥,참치,김,오이
일식|새우튀김|새우,달걀,빵가루
일식|야채튀김|고구마,당근,양파,튀김가루
일식|우동|우동면,대파,어묵
일식|냉모밀|메밀면,무,김,쪽파
일식|라멘|라멘면,돼지고기,달걀,대파
일식|야키소바|중화면,양배추,돼지고기,당근
일식|오코노미야키|양배추,밀가루,달걀,베이컨
일식|타코야키|문어,밀가루,달걀,대파
일식|일본식 카레|밥,카레,감자,당근,양파
일식|미소된장국|된장,두부,미역,대파
일식|유부초밥|유부,밥,당근
양식|토마토파스타|파스타면,토마토,마늘,양파
양식|크림파스타|파스타면,생크림,베이컨,마늘
양식|알리오올리오|파스타면,마늘,올리브유,페퍼론치노
양식|로제파스타|파스타면,토마토소스,생크림,베이컨
양식|봉골레파스타|파스타면,바지락,마늘,올리브유
양식|까르보나라|파스타면,달걀,베이컨,치즈
양식|라자냐|라자냐면,소고기,토마토소스,치즈
양식|버섯크림리조또|쌀,버섯,생크림,치즈
양식|마르게리타피자|피자도우,토마토소스,모차렐라치즈,바질
양식|햄버거|햄버거빵,소고기패티,양상추,토마토,치즈
양식|클럽샌드위치|식빵,닭고기,달걀,양상추,토마토
양식|에그샌드위치|식빵,달걀,마요네즈
양식|프렌치토스트|식빵,달걀,우유,설탕
양식|감자그라탕|감자,생크림,치즈,양파
양식|치킨스테이크|닭고기,감자,버섯,마늘
양식|비프스테이크|소고기,버터,마늘,아스파라거스
양식|함박스테이크|소고기,돼지고기,양파,달걀
양식|감바스|새우,마늘,올리브유,바게트
양식|시저샐러드|양상추,닭고기,치즈,식빵
양식|그릭샐러드|토마토,오이,양상추,페타치즈
양식|양송이스프|양송이버섯,우유,생크림,양파
양식|팬케이크|밀가루,달걀,우유,버터
양식|콘치즈|옥수수,마요네즈,치즈
양식|오믈렛|달걀,우유,치즈,양파
양식|피자토스트|식빵,토마토소스,치즈,햄
동남아|베트남 쌀국수|쌀국수면,소고기,숙주,양파
동남아|분짜|쌀국수면,돼지고기,상추,당근
동남아|반미|바게트,돼지고기,당근,오이
동남아|팟타이|쌀국수면,새우,달걀,숙주
동남아|똠얌꿍|새우,버섯,토마토,레몬
동남아|그린커리|닭고기,코코넛밀크,가지,그린커리페이스트
동남아|나시고랭|밥,달걀,새우,양파
동남아|월남쌈|라이스페이퍼,새우,당근,오이,상추
멕시코|타코|또띠아,소고기,양상추,토마토
멕시코|부리토|또띠아,밥,소고기,콩,치즈
멕시코|퀘사디아|또띠아,치즈,닭고기,피망
멕시코|엔칠라다|또띠아,닭고기,토마토소스,치즈
중동|후무스|병아리콩,참깨,레몬,마늘
중동|팔라펠|병아리콩,양파,파슬리,마늘
중동|샥슈카|토마토,달걀,피망,양파
간식|과일요거트|요거트,바나나,딸기,블루베리
간식|바나나스무디|바나나,우유,요거트
간식|딸기스무디|딸기,우유,요거트
간식|아보카도토스트|식빵,아보카도,달걀
간식|고구마구이|고구마
간식|삶은달걀|달걀
간식|계란샐러드|달걀,감자,마요네즈
간식|참치주먹밥|밥,참치,김,마요네즈
간식|치즈토스트|식빵,치즈,버터
간식|시리얼볼|시리얼,우유,바나나
간식|오트밀죽|오트밀,우유,바나나
간식|과일샐러드|사과,바나나,딸기,요거트
간식|고구마샐러드|고구마,달걀,마요네즈
간식|토마토카프레제|토마토,모차렐라치즈,바질
간식|핫도그|핫도그빵,소시지,케첩
간식|또띠아롤|또띠아,닭고기,양상추,치즈
간식|망고요거트볼|망고,요거트,그래놀라
간식|견과류요거트|요거트,견과류,꿀
간식|레몬에이드|레몬,탄산수,설탕
간식|당근사과주스|당근,사과
"""

RECIPES = []
for line in DATA.strip().splitlines():
    category, name, ingredients = line.split("|")
    RECIPES.append({
        "category": category.strip(),
        "name": name.strip(),
        "ingredients": [x.strip() for x in ingredients.split(",")],
    })

ALIASES = {
    "계란": "달걀",
    "파": "대파",
    "삼겹살": "돼지고기",
    "목살": "돼지고기",
    "쇠고기": "소고기",
    "닭": "닭고기",
    "닭가슴살": "닭고기",
    "스파게티면": "파스타면",
}

def normalize(text):
    cleaned = str(text).strip().replace(" ", "")
    return ALIASES.get(cleaned, cleaned)

if "ingredients" not in st.session_state:
    st.session_state.ingredients = []

menu = st.sidebar.radio(
    "메뉴",
    ["홈", "식재료 등록", "식재료 관리", "음식 추천", "음식 데이터베이스"],
)

st.title("🥗 Smart Food Manager")
st.caption("식재료를 관리하고, 보유 재료를 활용할 수 있는 음식을 추천해 음식물 낭비를 줄여보세요.")

# 홈
if menu == "홈":
    today = date.today()
    total = len(st.session_state.ingredients)
    urgent = sum(1 for x in st.session_state.ingredients if 0 <= (x["expiry"] - today).days <= 3)
    expired = sum(1 for x in st.session_state.ingredients if (x["expiry"] - today).days < 0)

    st.header("📊 식재료 현황")
    c1, c2, c3 = st.columns(3)
    c1.metric("등록 식재료", f"{total}개")
    c2.metric("유통기한 임박", f"{urgent}개")
    c3.metric("날짜 확인 필요", f"{expired}개")

    st.subheader("⏰ 먼저 확인할 식재료")
    if not st.session_state.ingredients:
        st.info("식재료 등록 메뉴에서 냉장고 속 재료를 추가해 주세요.")
    else:
        for item in sorted(st.session_state.ingredients, key=lambda x: x["expiry"])[:10]:
            days = (item["expiry"] - today).days
            label = "기한 지남" if days < 0 else ("오늘까지" if days == 0 else f"{days}일 남음")
            st.write(f"**{item['name']}** · {item['quantity']:g} {item['unit']} · {label}")

    st.info(f"현재 음식 데이터베이스에는 {len(RECIPES)}개 음식이 등록되어 있습니다.")

# 식재료 등록
elif menu == "식재료 등록":
    st.header("➕ 식재료 등록")
    with st.form("add_ingredient", clear_on_submit=True):
        name = st.text_input("식재료 이름", placeholder="예: 달걀, 양파, 김치")
        quantity = st.number_input("수량", min_value=0.1, value=1.0, step=1.0)
        unit = st.selectbox("단위", ["개", "팩", "봉", "g", "kg", "ml", "L", "묶음"])
        expiry = st.date_input("소비기한 또는 유통기한", value=date.today())
        memo = st.text_input("메모 (선택)")
        submitted = st.form_submit_button("저장", use_container_width=True)

    if submitted:
        if not name.strip():
            st.error("식재료 이름을 입력해 주세요.")
        else:
            st.session_state.ingredients.append({
                "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
                "name": normalize(name),
                "quantity": quantity,
                "unit": unit,
                "expiry": expiry,
                "memo": memo.strip(),
            })
            st.success(f"{name.strip()} 등록 완료!")
            st.rerun()

# 식재료 관리
elif menu == "식재료 관리":
    st.header("🧺 식재료 관리")
    if not st.session_state.ingredients:
        st.info("등록된 식재료가 없습니다.")
    else:
        today = date.today()
        for item in list(st.session_state.ingredients):
            days = (item["expiry"] - today).days
            if days < 0:
                status = f"기한 {abs(days)}일 지남"
            elif days == 0:
                status = "오늘까지"
            elif days <= 3:
                status = f"{days}일 남음 · 임박"
            else:
                status = f"{days}일 남음"

            with st.container(border=True):
                left, middle, right = st.columns([3, 2, 1])
                left.write(f"**{item['name']}**")
                left.caption(f"{item['quantity']:g} {item['unit']} · {item['expiry']}")
                if item["memo"]:
                    left.caption(item["memo"])
                middle.write(status)
                if right.button("삭제", key=f"delete_{item['id']}"):
                    st.session_state.ingredients = [
                        x for x in st.session_state.ingredients if x["id"] != item["id"]
                    ]
                    st.rerun()

        if st.button("전체 식재료 비우기"):
            st.session_state.ingredients = []
            st.rerun()

# 음식 추천
elif menu == "음식 추천":
    st.header("🍳 보유 재료로 음식 추천")
    if not st.session_state.ingredients:
        st.warning("먼저 식재료를 등록해 주세요.")
    else:
        today = date.today()
        owned = {normalize(x["name"]) for x in st.session_state.ingredients}
        urgent = {
            normalize(x["name"]) for x in st.session_state.ingredients
            if 0 <= (x["expiry"] - today).days <= 3
        }

        category = st.selectbox(
            "음식 종류",
            ["전체"] + sorted({x["category"] for x in RECIPES}),
            key="recommend_category",
        )
        complete_only = st.checkbox("대표 재료를 모두 보유한 음식만 보기", value=False)
        urgent_first = st.checkbox("기한 임박 재료를 사용하는 음식 우선 추천", value=True)

        results = []
        for recipe in RECIPES:
            if category != "전체" and recipe["category"] != category:
                continue
            required = {normalize(x) for x in recipe["ingredients"]}
            matched = required & owned
            missing = required - owned
            coverage = len(matched) / len(required)
            urgent_used = len(required & urgent)
            if complete_only and missing:
                continue
            score = coverage * 100 + (urgent_used * 12 if urgent_first else 0)
            results.append((score, recipe, matched, missing, coverage, urgent_used))

        results.sort(key=lambda x: (x[0], x[4], x[5]), reverse=True)
        st.write(f"추천 결과: **{len(results)}개**")
        if not results:
            st.info("조건에 맞는 음식이 없습니다. 필터를 바꾸거나 재료를 더 등록해 보세요.")
        else:
            for score, recipe, matched, missing, coverage, urgent_used in results[:50]:
                with st.container(border=True):
                    title_col, metric_col = st.columns([4, 1])
                    title_col.subheader(recipe["name"])
                    title_col.caption(recipe["category"])
                    metric_col.metric("재료 보유율", f"{coverage * 100:.0f}%")
                    st.write("**보유 재료:** " + (", ".join(sorted(matched)) if matched else "없음"))
                    st.write("**추가 필요 재료:** " + (", ".join(sorted(missing)) if missing else "없음"))
                    st.progress(coverage)
                    if urgent_used:
                        st.success(f"유통기한 임박 재료 {urgent_used}개 활용 가능")

# 음식 데이터베이스
elif menu == "음식 데이터베이스":
    st.header("📚 음식 데이터베이스")
    st.write(f"등록된 음식: **{len(RECIPES)}개**")
    search = st.text_input("음식 또는 재료 검색", placeholder="예: 파스타, 달걀, 김치")
    category = st.selectbox(
        "분류",
        ["전체"] + sorted({x["category"] for x in RECIPES}),
        key="database_category",
    )

    filtered = RECIPES
    if category != "전체":
        filtered = [x for x in filtered if x["category"] == category]
    if search.strip():
        q = search.strip().lower()
        filtered = [
            x for x in filtered
            if q in x["name"].lower()
            or any(q in ingredient.lower() for ingredient in x["ingredients"])
        ]

    st.caption(f"검색 결과: {len(filtered)}개")
    for recipe in filtered:
        with st.expander(f"{recipe['name']} · {recipe['category']}"):
            st.write("대표 재료: " + ", ".join(recipe["ingredients"]))

st.divider()
st.caption("Smart Food Manager · 음식 추천은 대표 재료 기준입니다. 실제 조리법, 보관 상태, 알레르기 정보는 반드시 별도로 확인하세요.")

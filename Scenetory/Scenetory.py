"""소설 및 글 작성 시 AI의 문장 추천을 받아 작성하는 프로그램입니다."""
import pynecone as pc
import openai

# API 키
YOUR_API_KEY = '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'

# 작성부분 스탯
class EditableState(pc.State):

    # 프롬프트 결과
    prompt_result: str = ""
    # 프롬프트 결과의 리스트 변환
    result_to_list=list()
    # 제목 리스트
    title_list=list()
    # 본문 리스트
    detail_list=list()


    def write_fairy_tale(self):

        # API 키 설정
        openai.api_key = YOUR_API_KEY

        # ChatGPT 호출
        completion = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"Write a fairy tale by table of contents",
            temperature = 0,
            max_tokens = 1024,
            top_p = 1,
        )

        # 생성된 프롬프트의 결과를 리스트 형식으로 변환
        self.prompt_result=completion['choices'][0]['text']
        self.result_to_list=self.prompt_result.replace('.', './n').split('/n')

        return pc.redirect('/home')

def print_fairy_tale(fairy_tale):
    return pc.box(
        pc.text(
            fairy_tale
        )
    )

# 메인 화면
def index():
    return pc.center(
        pc.vstack(
            pc.heading("동화 제조기", font_family="KyoboHandwriting2021sjy"),
            pc.button(
                "Get Started!",
                on_click=EditableState.write_fairy_tale
            )
        )
    )

def home():
    return pc.center(
        pc.vstack(
            pc.foreach(EditableState.result_to_list, print_fairy_tale)
        )
    )

# Add state and page to the app.
app = pc.App(
    state=EditableState,
    stylesheets=['../assets/font_style.css']
)
app.add_page(index, route="/")
app.add_page(home)
app.compile()
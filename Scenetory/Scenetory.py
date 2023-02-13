"""소설 및 글 작성 시 AI의 문장 추천을 받아 작성하는 프로그램입니다."""
import pynecone as pc
import openai

# API 키
<<<<<<< HEAD
YOUR_API_KEY = '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'
=======
YOUR_API_KEY = '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'

styles = {
    'title_style': {
        'font_family': 'SilkScreen',
        'font_size' : '4xl',
    }
}
>>>>>>> 192021f (Initial commit)

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
<<<<<<< HEAD
            max_tokens = 1024,
=======
            max_tokens = 500,
>>>>>>> 192021f (Initial commit)
            top_p = 1,
        )

        # 생성된 프롬프트의 결과를 리스트 형식으로 변환
        self.prompt_result=completion['choices'][0]['text']
<<<<<<< HEAD
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
=======
        self.result_to_list=self.prompt_result.split('\n')

        # 리스트 변형
        # 목차와 본문을 나누는 과정
        del self.result_to_list[:3]

        temp=self.result_to_list[0]
        self.title_list.append(self.result_to_list.pop(0))
        while temp!=self.result_to_list[0]:
            self.title_list.append(self.result_to_list.pop(0))

        return pc.redirect('/home')

def print_list(text):
    return pc.box(
        pc.text(
            text
        )
    )

# 시작 화면
def index():
    return pc.center(
        pc.vstack(
            pc.heading("Fairytale Generator", style=styles['title_style']),
            pc.button(
                "Get Started!",
                on_click=EditableState.write_fairy_tale
            ),
            padding_top="25em"
>>>>>>> 192021f (Initial commit)
        )
    )

def home():
    return pc.center(
        pc.vstack(
<<<<<<< HEAD
            pc.foreach(EditableState.result_to_list, print_fairy_tale)
        )
=======
            pc.foreach(EditableState.title_list, print_list),
            pc.divider(),
            pc.foreach(EditableState.result_to_list, print_list)
        ),
>>>>>>> 192021f (Initial commit)
    )

# Add state and page to the app.
app = pc.App(
    state=EditableState,
<<<<<<< HEAD
    stylesheets=['../assets/font_style.css']
=======
    stylesheets=["./assets/font_style.css"]
>>>>>>> 192021f (Initial commit)
)
app.add_page(index, route="/")
app.add_page(home)
app.compile()
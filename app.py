import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://pythonandvba.com)")


# import streamlit as st

# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()


# # Use local CSS
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# local_css("style/style.css")

# # # # ---- LOAD ASSETS ----
# # lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# # img_contact_form = Image.open("images/yt_contact_form.png")
# # img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# # ---- HEADER SECTION ----
# with st.container():
#     with st.container():
#         st.write("---")
#         st.title("Shira Tamari")
#         st.write("---")

# # art

# # # work
# #         urls = [
# #             "https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8",
# #             "https://photos.app.goo.gl/fuAaCVfaQq6TthMf9",
# #             "https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8",
# #             "https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8",
# #         ]

# #         image_paths = [
# #             "art.png",
# #             "wall.png",
# #             "wall.png",
# #             "wall.png",
# #             # "rishum.png",
# #             # "grafiti.png",

# #         ]
# #         titels = ["s","sd","asf","asf"
           
# #         ]
# #         col1, col2= st.columns(2)

# #         for url, path, titels, col in zip(urls, image_paths,titels, [col1,col2,col2,col2]):
# #             with col:
# #                 st.write(titels)
# #                 link = f'<a href="{url}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open(path, "rb").read()).decode()}" alt="Description of the image" width="222"></a>'
# #                 st.markdown(link, unsafe_allow_html=True)

# # with st.container():
# #     with st.container():
# #         st.write("---")
# #         st.write("054-8000524")
# #         st.write("shirgilboatamari@gmail.com")
# #         st.write("---")


# #         # left_column, right_column = st.columns(2)
# #         # with left_column:
# #         #     # st.subheader("Bring back a litlebit of nature")
# #         #     # st.title("SHIRA TAMARY")
# #         #     st.write(
# #         #         "somthing"
# #         #     )
# #         #     st.write("[art](https://www.youtube.com/@CodingIsFun) ")
# #         # with right_column:
# #         #     st.write("[social wall painting](https://www.youtube.com/@CodingIsFun) ")
# #         #     st.write(" my email: ")
# #         # # with right_column:
# #         # #     # img = Image.open("lily.jpg")
# #         # #     # st.image(img)
# #         #

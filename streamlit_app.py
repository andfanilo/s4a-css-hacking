import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(page_title="CSS hacks", page_icon=":smirk:")
st.title("CSS Hack tests")

c1 = st.container()
st.markdown("---")
c2 = st.container()
with c1:
    st.markdown("Hello")
    st.slider("World", 0, 10, key="1")
with c2:
    st.markdown("Hello")
    st.slider("World", 0, 10, key="2")

# STYLE WITH CSS THROUGH MARKDOWN
st.markdown("""
<style>
div[data-testid="stBlock"] {
    padding: 1em 0;
    border: thick double #32a1ce;
}
</style>
""", unsafe_allow_html=True)

# STYLE WITH JS THROUGH HTML IFRAME 
components.html("""
<script>
const elements = window.parent.document.querySelectorAll('div[data-testid="stBlock"]')
console.log(elements)
elements[0].style.backgroundColor = 'paleturquoise'
elements[1].style.backgroundColor = 'lightgreen'
</script>
""", height=0, width=0)

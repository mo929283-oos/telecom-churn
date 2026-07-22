"""
===========================================================
TelcoGuard AI
HTML Rendering Helper
===========================================================

Streamlit's st.markdown() runs content through a CommonMark
parser before allowing raw HTML through. If a multi-line HTML
snippet contains a BLANK LINE in the middle of it (which this
codebase's formatting style does, a lot), the parser treats
that blank line as the end of the HTML block. Everything after
it then gets misinterpreted as indented code, which is why
raw tags like <div> or <h1> were showing up as literal text
instead of being rendered.

render_html() collapses the whole snippet onto a single line
before handing it to st.markdown(), so it's always parsed as
one continuous HTML block.
"""

import re
import streamlit as st


def render_html(raw: str):
    compact = re.sub(r"\s+", " ", raw.strip())
    st.markdown(compact, unsafe_allow_html=True)

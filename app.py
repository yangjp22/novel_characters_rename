import streamlit as st


rename = st.text_area("Give me the rename mapping...", height=150)
content = st.text_area("Content here...", height=200)
modified_cnt = {}

if rename and content:
    rename = rename.replace("\n", " ")
    maps = rename.split(";")
    for each_map in maps:
        old = each_map.split(":")[0].strip()
        new = each_map.split(":")[-1].strip()
        if old in content and old:
            modified_cnt[old] = content.count(old)
            content = content.replace(old, new)

    with st.expander("Content after modification:"):
        st.write(content)

    with st.expander("Modification details"):
        modification = sorted(modified_cnt.items(), key=lambda x: x[1], reverse=True)
        if modification:
            for single in modification:
                st.write("{} is replaced {} times".format(single[0], single[1]))
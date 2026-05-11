import streamlit as st
import subprocess
import sys

st.set_page_config(page_title="AI视频笔记生成工具", layout="centered")
st.title("📝 AI 视频笔记生成器（支持合集）")

# 输入模式选择
mode = st.radio("选择模式", ["单个视频", "**合集/批量**（原版官方功能）"], horizontal=True)

video_url = st.text_input("输入视频/合集链接", placeholder="https://www.bilibili.com/...")

template_opt = st.radio("笔记类型", ["brief 精简", "detailed 详细", "quiz 测验"], horizontal=True)
template = template_opt.split()[0]

# 生成按钮
if st.button("🚀 开始生成", use_container_width=True):
    if not video_url.strip():
        st.warning("请输入链接")
        st.stop()

    # 选择命令
    if "合集" in mode:
        # ✅ 这里调用的是你项目原版官方 batch 命令！
        cmd = [sys.executable, "-m", "noteking.cli", "batch", video_url, "--template", template]
        tip = "正在处理合集（批量生成 + 自动合并）..."
    else:
        cmd = [sys.executable, "-m", "noteking.cli", "run", video_url, "--template", template]
        tip = "正在处理单个视频..."

    with st.spinner(tip):
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        if res.returncode == 0:
            st.success("✅ 生成完成！（合集已自动合并为一份笔记）")
            st.code(res.stdout, language="markdown")
        else:
            st.error("❌ 执行失败")
            st.code(res.stderr)
NoteKing（个人修改版）
🎥 B站视频一键生成AI结构化笔记 | 无需下载完整视频 | 命令行+可视化前端双模式
基于官方NoteKing二次优化，聚焦实际使用痛点，适配个人学习、高效笔记生成场景，全程无冗余操作，兼顾便捷性与API使用经济性，开箱即用。
🔧 个人优化亮点（核心差异化）
- ✅ 修复.env密钥自动读取异常，无需手动输入--api-key参数，配置后全程自动调用，彻底解决密钥配置报错问题
- ✅ 新增省Token核心优化：开启字幕缓存、长文本自动压缩、重复生成跳过功能，大幅降低大模型API使用成本
- ✅ 优化B站链接解析逻辑，解决带多余参数的链接报错问题，完美兼容单视频、多P合集两种场景
- ✅ 完善Streamlit前端界面适配，启动后自动弹出浏览器，小白用户可直接粘贴链接、一键生成笔记
- ✅ 优化核心配置文件（core/config.py），支持旧配置自动重建，解决旧配置覆盖.env密钥的核心痛点
📋 项目简介
本项目是NoteKing的个人定制修改版，基于官方核心架构优化而来，核心功能为解析B站视频链接，自动提取视频字幕（不下载完整视频，仅缓存字幕/必要音频），调用大模型快速生成结构化Markdown笔记，支持导出PDF，适配学生、职场人快速整理视频干货、高效复盘学习。
保留官方全部核心功能，重点修复实际使用中的各类报错的痛点，简化配置流程，提升使用流畅度，无需复杂操作，配置完成即可快速上手。

核心卖点：图文并茂的 PDF 讲义
这不是简单的"视频转文字"，而是 带关键帧截图、结构化章节、高亮知识框 的专业讲义：

功能	说明
🎯 智能关键帧提取	场景检测 + 信息密度评分 + 感知哈希去重，自动挑选最有价值的画面
📐 专业 LaTeX 排版	tcolorbox 高亮框、代码高亮、数学公式、封面、目录、页眉页脚
📚 13 种输出模板	详细笔记、简要总结、思维导图、闪卡、测验题、考试复习、时间线……
🌍 30+ 平台支持	B站、YouTube、抖音、小红书、快手、TikTok、Twitter 等
🔄 批量处理	整个课程合集（比如 26 集的课）一键全部处理
🔁 字幕三级回退	平台字幕 → Whisper ASR → 纯视觉模式

13 种输出模板一览
模板	名称	适用场景	命令
brief	简要总结	快速了解视频讲了什么	-t brief
detailed	详细笔记	系统学习，带章节目录	-t detailed
mindmap	思维导图	画出知识结构	-t mindmap
flashcard	闪卡/Anki	间隔复习背诵	-t flashcard
quiz	测验题	自测掌握程度	-t quiz
timeline	时间线	按时间戳整理要点	-t timeline
exam	考试复习	公式速查 + 练习题	-t exam
tutorial	教程步骤	跟着视频一步步做	-t tutorial
news	新闻速览	媒体报道风格	-t news
podcast	播客摘要	音频/访谈内容整理	-t podcast
xhs_note	小红书笔记	社交平台分享	-t xhs_note
latex_pdf	LaTeX PDF	专业打印讲义	-t latex_pdf
custom	自定义	自己写提示词	-t custom

支持的平台
平台	状态	特色功能
哔哩哔哩	✅ 完整支持	单视频、合集、多P、SESSDATA高清
YouTube	✅ 完整支持	单视频、播放列表、频道（支持代理翻墙）
抖音	✅ 支持	短视频
小红书	✅ 支持	自动解析短链接
快手	✅ 支持	短视频
TikTok	✅ 支持	国际版
Twitter/X	✅ 支持	视频推文
本地文件	✅ 支持	MP4/MP3/WAV/FLAC
其他 1800+	✅ 通过 yt-dlp	几乎所有视频网站

🚀 快速开始
1. 环境准备
1. 克隆本仓库：git clone https://github.com/CaoJiaY-05/noteking.git
2. 进入项目根目录：cd noteking
3. 安装依赖：pip install -r requirements.txt（建议使用虚拟环境，避免依赖冲突）
4. 配置API密钥：复制根目录.env.example文件，重命名为.env，填写个人LLM API密钥（支持DeepSeek、OpenAI等所有兼容OpenAI接口的大模型）
2. 两种启动方式
方式1：可视化前端（推荐，小白友好）
执行以下命令，将自动弹出浏览器可视化界面，无需输入复杂命令：
streamlit run app_ui.py
操作步骤：粘贴B站完整视频链接 → 选择生成模式（单视频/合集批量） → 点击「开始生成笔记」 → 等待10~20秒，即可在网页直接查看笔记，同时自动保存至本地目录。
方式2：命令行模式（高效快捷，适合开发者）
# 单个B站视频生成笔记
python -m noteking.cli run "https://www.bilibili.com/video/BVxxxx/"

# B站多P合集批量生成笔记
python -m noteking.cli batch "https://www.bilibili.com/video/BVxxxx/"
📂 文件路径说明
- noteking_output/：生成的Markdown笔记默认保存目录，可直接用VS Code、WPS等工具打开编辑、导出PDF
- .noteking/cache/：字幕、音频缓存目录，保留缓存可避免重复下载，节省API Token和网络流量
- core/config.py：核心配置文件（已完成优化，自动读取.env密钥，无需手动修改）
- app_ui.py：前端界面启动文件，直接执行命令即可启动可视化操作，无需额外配置
❓ 常见问题（解决我实际遇到的坑，新手必看）
- Q：启动后提示「No LLM API key configured」？
A：删除旧配置文件~/.noteking/config.json，重新运行项目，系统会自动读取.env中的密钥并重建配置，即可解决。
- Q：B站链接解析失败，提示「网页解析失败，可能是不支持的网页类型，请检查网页或稍后重试」？
A：首先确保使用完整且无多余参数的B站链接（标准格式：https://www.bilibili.com/video/BVxxxx/）；若仍失败，可在.env文件中添加B站SESSDATA，提升解析成功率。
- Q：Git提交时卡住、无法push或界面加载不动？
A：优先用命令行提交（git add . && git commit -m "提交描述" && git push origin main），绕过VS Code界面问题；若仍卡住，可终止任务管理器中的git.exe、Code.exe进程，重启VS Code后重试。
- Q：生成笔记后，如何导出PDF？
A：用VS Code（安装Markdown PDF插件）或WPS，打开noteking_output目录下的.md笔记文件，直接通过软件自带的「导出为PDF」功能操作，无需额外下载工具。
⚠️ 注意事项
- .env文件包含个人LLM API密钥，请勿上传至GitHub（仓库已配置.gitignore，会自动忽略该文件），避免密钥泄露导致额度被盗刷。
- 工具仅提取视频字幕/必要音频，不下载完整视频文件，不会占用大量硬盘空间，无需担心存储压力。
- 缓存文件无需频繁删除，保留缓存可大幅提升后续同视频的笔记生成速度，同时节省API Token消耗。
- 安装依赖时若出现报错，可尝试更新pip版本（pip install --upgrade pip）后重新安装。
📌 项目结构（核心目录）
noteking/
├── core/            # 核心配置与逻辑（含优化后的config.py，解决密钥读取问题）
├── cli/             # 命令行工具入口，支持单视频/合集批量生成
├── app_ui.py        # 前端界面启动文件，可视化操作入口
├── .env.example     # API密钥配置示例，复制重命名即可使用
├── .gitignore       # 自动忽略敏感/冗余文件，保护密钥安全
└── noteking_output/ # 笔记输出目录，生成的.md文件自动保存至此
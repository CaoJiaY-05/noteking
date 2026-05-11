from dotenv import load_dotenv
import os

# 强制加载.env文件
load_dotenv()

# 读取变量
api_key = os.getenv("NOTEKING_LLM_API_KEY")
base_url = os.getenv("NOTEKING_LLM_BASE_URL")
model = os.getenv("NOTEKING_LLM_MODEL")

print("API Key:", api_key)
print("Base URL:", base_url)
print("Model:", model)
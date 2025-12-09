from huggingface_hub import snapshot_download

# snapshot_download(
#     repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
#     local_dir="/workspace/user/Models/LLama3", # 指定路径
#     ignore_patterns=["*.msgpack", "*.h5"] # 过滤掉不需要的TensorFlow权重，省空间
# )
snapshot_download(
    repo_id="Qwen/Qwen3-4B-Thinking-2507",
    local_dir="/workspace/user/Models/Qwen/Qwen3-4B-Thinking", # 指定路径
)
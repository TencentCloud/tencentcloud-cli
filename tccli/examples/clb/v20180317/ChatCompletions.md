**Example 1: pdf输入对话测试**

pdf输入对话测试

Input: 

```
tccli clb ChatCompletions --cli-unfold-argument  \
    --ApiKey sk-3qIbn_4___xKHm6HwjTtncyCpHJD_ddDeB6ytjvpw2fq8G6x_LNO6t11Y_l7qQuKEfVH4t1s1gjUv3_vb2mqTkUv \
    --Model gpt-4o-mini-test-connection \
    --RequestPath /v1/chat/completions \
    --Attachments.0.Type pdf \
    --Attachments.0.Data data:application/pdf;base64,JVBERi0xLjQKJeLjz9MKMyAwIG9iago8PC9UeXBlIC9QYWdlCi9QYXJlbnQgMSAwIFIKL01lZGlhQm94IFswIDAgNjEyIDc5Ml0KL0NvbnRlbnRzIDQgMCBSCi9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSAyIDAgUj4+Pj4+PgplbmRvYmoKNCAwIG9iago8PC9MZW5ndGggNDQ+PgpzdHJlYW0KQlQKL0YxIDI0IFRmCjEwMCA3MDAgVGQKKHRlc3QpIFRqCkVUCmVuZHN0cmVhbQplbmRvYmoKMiAwIG9iago8PC9UeXBlIC9Gb250Ci9TdWJ0eXBlIC9UeXBlMQovQmFzZUZvbnQgL0hlbHZldGljYT4+CmVuZG9iagoxIDAgb2JqCjw8L1R5cGUgL1BhZ2VzCi9LaWRzIFszIDAgUl0KL0NvdW50IDE+PgplbmRvYmoKNSAwIG9iago8PC9UeXBlIC9DYXRhbG9nCi9QYWdlcyAxIDAgUj4+CmVuZG9iagp0cmFpbGVyCjw8L1NpemUgNgovUm9vdCA1IDAgUj4+CnN0YXJ0eHJlZgozMjQKJSVFT0Y=
```

Output: 
```
{
    "Response": {
        "ChatResponseMessage": "[Fake v2] Detected user_text=\"What's this file about?\", images=0, files=1, format=openai-chat",
        "RequestId": "cb9c6c5a-ba63-4dd1-a0ac-77f230d49989"
    }
}
```

**Example 2: 图像输入对话测试**

图像输入对话测试

Input: 

```
tccli clb ChatCompletions --cli-unfold-argument  \
    --ApiKey sk-3qIbn_4___xKHm6HwjTtncyCpHJD_ddDeB6ytjvpw2fq8G6x_LNO6t11Y_l7qQuKEfVH4t1s1gjUv3_vb2mqTkUv \
    --Model gpt-4o-mini-test-connection \
    --RequestPath /v1/chat/completions \
    --Attachments.0.Type image \
    --Attachments.0.Data data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkAAIAAAoAAv/lxKUAAAAASUVORK5CYII=
```

Output: 
```
{
    "Response": {
        "ChatResponseMessage": "[Fake v2] Detected user_text=\"What's in this image?\", images=1, files=0, format=openai-chat",
        "RequestId": "34551057-b067-41de-94e2-4604f15d9ab8"
    }
}
```

**Example 3: 基础对话测试**

基础对话测试

Input: 

```
tccli clb ChatCompletions --cli-unfold-argument  \
    --ApiKey sk-3qIbn_4___xKHm6HwjTtncyCpHJD_ddDeB6ytjvpw2fq8G6x_LNO6t11Y_l7qQuKEfVH4t1s1gjUv3_vb2mqTkUv \
    --Model gpt-4o-mini-test-connection \
    --RequestPath /v1/messages
```

Output: 
```
{
    "Response": {
        "ChatResponseMessage": "[Fake v2] Echo text-only: \"Hi, this is a connectivity test.\"",
        "RequestId": "d5b8b664-f033-4e06-af59-c3a1cae1940e"
    }
}
```


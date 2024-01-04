**Example 1: 请求成功示例**

POST / HTTP/1.1
Host: hunyuan.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: GetEmbedding
<公共请求参数>

Input: 

```
tccli hunyuan GetEmbedding --cli-unfold-argument  \
    --Input 你好
```

Output: 
```
{
    "Response": {
        "RequestId": "658a95a1f824ac766d8261b0",
        "Data": [
            {
                "Embedding": [
                    0.018218994140625,
                    0.024810791015625
                ],
                "Index": 0,
                "Object": "embedding"
            }
        ],
        "Usage": {
            "PromptTokens": 3,
            "TotalTokens": 3
        }
    }
}
```


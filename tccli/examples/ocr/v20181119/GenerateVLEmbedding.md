**Example 1: 图文混合示例**



Input: 

```
tccli ocr GenerateVLEmbedding --cli-unfold-argument  \
    --Model 0 \
    --Type 2 \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/SubmitMarkEssayAgentJob/1.jpg \
    --VideoUrl https://sls-layer-ap-guangzhou-code-1301293904.cos.ap-guangzhou.myqcloud.com/%E9%89%B4%E4%BC%AA%E6%A0%B7%E5%BC%A0/00085_54d34776.mp4 \
    --SearchMode 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Embedding": [
                    0.14095914
                ],
                "Index": 0
            }
        ],
        "InputTokens": 990,
        "TotalTokens": 990,
        "RequestId": "0c2a5d99-68bf-4809-87d3-aef51f0fbb57"
    }
}
```


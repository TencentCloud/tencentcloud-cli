**Example 1: 成功示例**



Input: 

```
tccli ocr RunRerank --cli-unfold-argument  \
    --Model 0 \
    --Query 多模态文档解析 \
    --Docs 文档解析大模型
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "Index": 0,
                "Score": 27.172710418701172
            }
        ],
        "RequestId": "55118933-250b-4d75-a70d-6c1227cb49ab"
    }
}
```


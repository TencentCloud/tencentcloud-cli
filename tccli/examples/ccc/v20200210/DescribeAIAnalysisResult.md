**Example 1: 获取 AI 会话分析结果**



Input: 

```
tccli ccc DescribeAIAnalysisResult --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId adcf61b8-dbb9-4c20-87bf-c0744c04bade \
    --StartTime 1737350008 \
    --EndTime 1737356008
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx",
        "ResultList": [
            {
                "Type": "summary",
                "Result": "会话小结"
            },
            {
                "Type": "mood",
                "Result": "中性"
            },
            {
                "Type": "intention",
                "Result": "待跟进"
            }
        ]
    }
}
```


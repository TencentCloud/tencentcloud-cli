**Example 1: 查询推荐问题**



Input: 

```
tccli csip DescribeAIAnalysisRecommendQuestions --cli-unfold-argument  \
    --SessionID 81ed4b6f-**4************0bdcb73e392e
```

Output: 
```
{
    "Response": {
        "RecommendAction": [
            {
                "Action": "问题",
                "Question": "针对172******.75挖矿木马，如何快速定位并清除恶意进程？"
            }
        ],
        "RequestId": "b1a8c0c9-f101-47fb-aec4-1e1ec9651882"
    }
}
```


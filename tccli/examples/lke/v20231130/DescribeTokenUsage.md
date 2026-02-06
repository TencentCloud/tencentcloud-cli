**Example 1: 接口调用token详情示例**

接口调用token详情示例

Input: 

```
tccli lke DescribeTokenUsage --cli-unfold-argument  \
    --ModelName cs-normal-70b \
    --StartTime 1758988800 \
    --EndTime 1759075199 \
    --AppType knowledge_qa \
    --SpaceId default_space \
    --StatStartTime 1758988800 \
    --StatEndTime 1759075199
```

Output: 
```
{
    "Response": {
        "ApiCallStats": 4909,
        "DosageTypeCurr": 0,
        "DosageTypeLimit": 0,
        "InputTokenUsage": 3178475,
        "InternetSearchUsage": 0,
        "OutputTokenUsage": 439374,
        "PageUsage": 0,
        "RagSearchUsage": 0,
        "RequestId": "a35fa69b-118b-4b25-8f1d-e5478f2b7159",
        "SearchUsage": 0,
        "SplitTokenUsage": 0,
        "TotalTokenUsage": 3617849
    }
}
```


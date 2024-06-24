**Example 1: 回答类型数据统计**



Input: 

```
tccli lke GetAnswerTypeDataCount --cli-unfold-argument  \
    --StartTime 1716368386 \
    --EndTime 1716454119 \
    --AppBizId 1747088166522585088 1780116741678956544 \
    --Type 4 \
    --LoginUin abc \
    --LoginSubAccountUin abc
```

Output: 
```
{
    "Response": {
        "ConcurrentLimitCount": 0,
        "ImageUnderstandingCount": 0,
        "KnowledgeCount": 0,
        "ModelReplyCount": 90,
        "RejectCount": 0,
        "RequestId": "452f1b7a-58ca-4b0f-9cbf-8ab400684653",
        "SearchEngineCount": 9,
        "SensitiveCount": 0,
        "TaskFlowCount": 18,
        "Total": 127,
        "UnknownIssuesCount": 10
    }
}
```


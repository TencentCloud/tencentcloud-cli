**Example 1: DescribeConcurrencyLimitDetailList**



Input: 

```
tccli adp DescribeConcurrencyLimitDetailList --cli-unfold-argument  \
    --TimeRange.EndTime 1786463999 \
    --TimeRange.StartTime 1786377600 \
    --ViewScope.ViewType 1 \
    --ViewScope.ScopeId default_space \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "ConcurrencyLimitDetailList": [
            {
                "CallSource": {
                    "SubjectId": "10023456",
                    "SubjectName": "智能客服应用",
                    "SubjectType": 1
                },
                "EventTime": "1754956800",
                "ModelName": "hunyuan-turbo",
                "RequestQuery": "请帮我分析以下合同条款中的风险点，合同内容如下：甲方...",
                "SpaceId": "space_abc123"
            }
        ],
        "TotalCount": "47",
        "RequestId": "0ce01e90-96e4-4646-914f-8565942b1492"
    }
}
```


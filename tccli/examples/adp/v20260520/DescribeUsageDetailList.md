**Example 1: DescribeUsageDetailList**



Input: 

```
tccli adp DescribeUsageDetailList --cli-unfold-argument  \
    --ResourceType 1 \
    --TimeRange.EndTime 1786463999 \
    --TimeRange.StartTime 1786377600 \
    --ViewScope.ViewType 2 \
    --ViewScope.ScopeId default_space \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCount": "12580",
        "UsageDetailList": [
            {
                "CallSource": {
                    "SubjectId": "10023456",
                    "SubjectName": "智能客服应用",
                    "SubjectType": 1
                },
                "DosageId": "dosage_9988776655",
                "EventTime": "1754956800",
                "Model": {
                    "CallType": "chat",
                    "IsDefaultKB": false,
                    "ModelName": "hunyuan-turbo",
                    "ResourceConsumptionList": [
                        {
                            "Label": "",
                            "Unit": 0,
                            "Value": 8970
                        }
                    ]
                },
                "TraceId": "trace_abc123def456",
                "UserId": "user_001"
            }
        ],
        "RequestId": "4cfbc421-7c7f-47c8-ac7e-7e3c5eb92ac1"
    }
}
```


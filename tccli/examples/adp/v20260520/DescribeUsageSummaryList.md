**Example 1: DescribeUsageSummaryList**



Input: 

```
tccli adp DescribeUsageSummaryList --cli-unfold-argument  \
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
        "TotalCount": "86",
        "UsageSummaryList": [
            {
                "Model": {
                    "CallCount": 3200,
                    "IsDefaultKB": false,
                    "ModelName": "hunyuan-turbo",
                    "ResourceConsumptionList": [
                        {
                            "Label": "",
                            "Unit": 0,
                            "Value": 25600000
                        }
                    ]
                },
                "SourceId": "space_abc123",
                "SourceName": "产品研发空间",
                "ViewType": 1
            }
        ],
        "RequestId": "b08c3f61-9655-4fa4-85bb-e35e14e289c4"
    }
}
```


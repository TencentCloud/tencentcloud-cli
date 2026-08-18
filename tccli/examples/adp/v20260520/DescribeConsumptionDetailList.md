**Example 1: DescribeConsumptionDetailList**



Input: 

```
tccli adp DescribeConsumptionDetailList --cli-unfold-argument  \
    --TimeRange.EndTime 1786550699 \
    --TimeRange.StartTime 1786550399 \
    --ViewScope.ViewType 1 \
    --ViewScope.ScopeId default_space
```

Output: 
```
{
    "Response": {
        "ConsumptionDetailList": [
            {
                "Classification": {
                    "ConsumptionScene": "chat",
                    "ConsumptionTarget": "hunyuan-turbo",
                    "ConsumptionType": "model",
                    "PackageName": "企业标准套餐包"
                },
                "EventTime": "1754956800",
                "MetricSourceType": 1,
                "Name": "智能客服应用",
                "SpaceName": "产品研发空间",
                "Usage": {
                    "ConsumptionPU": 0.00897,
                    "Usage": 8970,
                    "UsageUnit": 0
                },
                "UserName": "张三"
            }
        ],
        "TotalCount": "328",
        "RequestId": "90431410-173a-4e44-b79e-d77a399da29b"
    }
}
```


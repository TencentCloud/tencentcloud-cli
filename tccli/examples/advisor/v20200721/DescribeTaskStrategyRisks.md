**Example 1: 查询评估项风险实例列表**



Input: 

```
tccli advisor DescribeTaskStrategyRisks --cli-unfold-argument  \
    --StrategyId 1
```

Output: 
```
{
    "Response": {
        "RiskTotalCount": 1,
        "StrategyId": 1,
        "RequestId": "xx",
        "RiskFieldsDesc": [
            {
                "Field": "xx",
                "FieldName": "xx",
                "FieldType": "xx"
            },
            {
                "Field": "xx",
                "FieldName": "xx",
                "FieldType": "xx"
            },
            {
                "Field": "xx",
                "FieldName": "xx",
                "FieldType": "xx"
            },
            {
                "Field": "xx",
                "FieldName": "xx",
                "FieldType": "xx"
            },
            {
                "Field": "xx",
                "FieldName": "xx",
                "FieldType": "xx"
            },
            {
                "Field": "xx",
                "FieldName": "xx",
                "FieldType": "xx"
            },
            {
                "Field": "xx",
                "FieldName": "xx",
                "FieldType": "xx"
            }
        ]
    }
}
```


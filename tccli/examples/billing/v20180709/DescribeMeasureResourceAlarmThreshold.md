**Example 1: 包分类余量预警**



Input: 

```
tccli billing DescribeMeasureResourceAlarmThreshold --cli-unfold-argument  \
    --ProductCode p_trade_t_s \
    --ThresholdType 4 \
    --GroupId fkkTestGroup
```

Output: 
```
{
    "Response": {
        "Data": {
            "GroupId": "fkkTestGroup",
            "ProductCode": "p_trade_t_s",
            "ResourceId": "",
            "ThresholdType": 4,
            "ThresholdValueType": 0,
            "Thresholds": [
                50
            ],
            "Uin": "100007908562",
            "UserLevelConfig": true,
            "Valid": 1
        },
        "RequestId": "gabriecheng-test-20250410-1"
    }
}
```


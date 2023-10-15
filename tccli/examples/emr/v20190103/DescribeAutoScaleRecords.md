**Example 1: 获取弹性扩缩容历史示例**



Input: 

```
tccli emr DescribeAutoScaleRecords --cli-unfold-argument  \
    --InstanceId emr-3ap64zl6 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RecordList": [
            {
                "StrategyName": "abc",
                "ScaleAction": "abc",
                "ActionStatus": "abc",
                "ActionTime": "abc",
                "ScaleInfo": "abc",
                "ExpectScaleNum": 0,
                "EndTime": "abc",
                "StrategyType": 0,
                "SpecInfo": "abc",
                "CompensateFlag": 0,
                "CompensateCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```


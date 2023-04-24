**Example 1: 获取呼入实时数据统计指标实例**

获取呼入实时数据统计指标实例。

Input: 

```
tccli ccc DescribeCallInMetrics --cli-unfold-argument  \
    --EnabledNumber True \
    --EnabledSkillGroup True \
    --SdkAppId 0
```

Output: 
```
{
    "Response": {
        "Timestamp": 0,
        "TotalMetrics": {
            "IvrCount": 0,
            "QueueCount": 0,
            "RingCount": 0,
            "AcceptCount": 0,
            "TransferOuterCount": 0,
            "MaxQueueDuration": 0,
            "AvgQueueDuration": 0,
            "MaxRingDuration": 0,
            "AvgRingDuration": 0,
            "MaxAcceptDuration": 0,
            "AvgAcceptDuration": 0
        },
        "NumberMetrics": [
            {
                "Number": "abc",
                "Metrics": {
                    "IvrCount": 0,
                    "QueueCount": 0,
                    "RingCount": 0,
                    "AcceptCount": 0,
                    "TransferOuterCount": 0,
                    "MaxQueueDuration": 0,
                    "AvgQueueDuration": 0,
                    "MaxRingDuration": 0,
                    "AvgRingDuration": 0,
                    "MaxAcceptDuration": 0,
                    "AvgAcceptDuration": 0
                },
                "SkillGroupMetrics": [
                    {
                        "SkillGroupId": 0,
                        "Metrics": {
                            "IvrCount": 0,
                            "QueueCount": 0,
                            "RingCount": 0,
                            "AcceptCount": 0,
                            "TransferOuterCount": 0,
                            "MaxQueueDuration": 0,
                            "AvgQueueDuration": 0,
                            "MaxRingDuration": 0,
                            "AvgRingDuration": 0,
                            "MaxAcceptDuration": 0,
                            "AvgAcceptDuration": 0
                        },
                        "Name": "abc"
                    }
                ]
            }
        ],
        "SkillGroupMetrics": [
            {
                "SkillGroupId": 0,
                "Name": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


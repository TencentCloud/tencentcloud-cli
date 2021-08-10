**Example 1: 获取呼入实时数据统计指标实例**



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
        "SkillGroupMetrics": [
            {
                "Metrics": {
                    "AvgQueueDuration": 5,
                    "AvgAcceptDuration": 0,
                    "MaxRingDuration": 4,
                    "RingCount": 1,
                    "MaxQueueDuration": 5,
                    "TransferOuterCount": 0,
                    "AcceptCount": 0,
                    "MaxAcceptDuration": 0,
                    "QueueCount": 1,
                    "IvrCount": 0,
                    "AvgRingDuration": 4
                },
                "Name": "xx",
                "SkillGroupId": 1070
            }
        ],
        "NumberMetrics": [
            {
                "Metrics": {
                    "AvgQueueDuration": 5,
                    "AvgAcceptDuration": 0,
                    "MaxRingDuration": 4,
                    "RingCount": 1,
                    "MaxQueueDuration": 5,
                    "TransferOuterCount": 0,
                    "AcceptCount": 0,
                    "MaxAcceptDuration": 0,
                    "QueueCount": 1,
                    "IvrCount": 0,
                    "AvgRingDuration": 4
                },
                "SkillGroupMetrics": [
                    {
                        "Metrics": {
                            "AvgQueueDuration": 5,
                            "AvgAcceptDuration": 0,
                            "MaxRingDuration": 4,
                            "RingCount": 1,
                            "MaxQueueDuration": 5,
                            "TransferOuterCount": 0,
                            "AcceptCount": 0,
                            "MaxAcceptDuration": 0,
                            "QueueCount": 1,
                            "IvrCount": 0,
                            "AvgRingDuration": 4
                        },
                        "Name": "xx",
                        "SkillGroupId": 1070
                    }
                ],
                "Number": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalMetrics": {
            "AvgQueueDuration": 5,
            "AvgAcceptDuration": 0,
            "MaxRingDuration": 4,
            "RingCount": 1,
            "MaxQueueDuration": 5,
            "TransferOuterCount": 0,
            "AcceptCount": 0,
            "MaxAcceptDuration": 0,
            "QueueCount": 1,
            "IvrCount": 0,
            "AvgRingDuration": 4
        }
    }
}
```


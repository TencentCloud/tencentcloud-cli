**Example 1: 获取目标列表**

获取目标列表

Input: 

```
tccli eb ListTargets --cli-unfold-argument  \
    --EventBusId eb-l65vlc2 \
    --RuleId rule-fdltium8
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Targets": [
            {
                "Type": "abc",
                "EventBusId": "abc",
                "TargetId": "abc",
                "TargetDescription": {
                    "ResourceDescription": "abc",
                    "SCFParams": {
                        "BatchTimeout": 0,
                        "BatchEventCount": 0,
                        "EnableBatchDelivery": true
                    },
                    "CkafkaTargetParams": {
                        "TopicName": "abc",
                        "RetryPolicy": {
                            "RetryInterval": 1,
                            "MaxRetryAttempts": 1
                        }
                    },
                    "ESTargetParams": {
                        "NetMode": "abc",
                        "IndexPrefix": "abc",
                        "RotationInterval": "abc",
                        "OutputMode": "abc",
                        "IndexSuffixMode": "abc",
                        "IndexTemplateType": "abc"
                    }
                },
                "RuleId": "abc",
                "EnableBatchDelivery": true,
                "BatchTimeout": 0,
                "BatchEventCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```


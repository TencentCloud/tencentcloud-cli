**Example 1: 获取目标列表**

获取目标列表

Input: 

```
tccli eb ListTargets --cli-unfold-argument  \
    --EventBusId eb-l6***c2 \
    --RuleId rule-fd***um8
```

Output: 
```
{
    "Response": {
        "RequestId": "b9730f16-0098-45d8-a55f-fd59fd7ed050",
        "Targets": [
            {
                "BatchEventCount": 0,
                "BatchTimeout": 0,
                "EnableBatchDelivery": false,
                "EventBusId": "eb-l6***c2",
                "RuleId": "rule-fd***um8",
                "TargetDescription": {
                    "CkafkaTargetParams": {
                        "EventDeliveryFormat": "",
                        "RetryPolicy": {
                            "MaxRetryAttempts": 0,
                            "RetryInterval": 0
                        },
                        "TopicName": ""
                    },
                    "ESTargetParams": {
                        "IndexPrefix": "",
                        "IndexSuffixMode": "",
                        "IndexTemplateType": "",
                        "NetMode": "",
                        "OutputMode": "",
                        "RotationInterval": ""
                    },
                    "ResourceDescription": "qcs::eb-amp:ap-guangzhou:uin/my-uin:",
                    "SCFParams": {
                        "BatchEventCount": 0,
                        "BatchTimeout": 0,
                        "EnableBatchDelivery": false
                    }
                },
                "TargetId": "target-5q***fmx",
                "Type": "amp"
            }
        ],
        "TotalCount": 1
    }
}
```


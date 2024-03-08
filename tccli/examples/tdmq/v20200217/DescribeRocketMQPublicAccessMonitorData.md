**Example 1: 正常响应**



Input: 

```
tccli tdmq DescribeRocketMQPublicAccessMonitorData --cli-unfold-argument  \
    --InstanceId abc \
    --StartTime abc \
    --EndTime abc \
    --Period 0 \
    --MetricName abc
```

Output: 
```
{
    "Response": {
        "MetricName": "abc",
        "Period": 0,
        "StartTime": "abc",
        "EndTime": "abc",
        "DataPoints": [
            {
                "Timestamps": [
                    0
                ],
                "Values": [
                    0
                ]
            }
        ],
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```


**Example 1: 创建实例(预付费包年包月)**



Input: 

```
tccli ckafka CreateInstancePre --cli-unfold-argument  \
    --InstanceName test \
    --MsgRetentionTime 1440 \
    --InstanceType 1 \
    --ZoneId 100003 \
    --Period 1m
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "DeleteRouteTimestamp": "xx",
            "Data": {
                "FlowId": 0,
                "DealNames": [
                    "1111111111"
                ]
            }
        },
        "RequestId": "1ba4ac83-1e9e-497b-b3e1-4c10872a4068"
    }
}
```


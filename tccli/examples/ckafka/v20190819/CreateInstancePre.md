**Example 1: 创建实例(预付费包年包月)**

创建实例(预付费包年包月)

Input: 

```
tccli ckafka CreateInstancePre --cli-unfold-argument  \
    --MsgRetentionTime 1440 \
    --Period 1m \
    --InstanceName test \
    --InstanceType 1 \
    --ZoneId 100003
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "DeleteRouteTimestamp": "xxxx",
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


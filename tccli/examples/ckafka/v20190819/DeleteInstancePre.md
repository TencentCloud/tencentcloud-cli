**Example 1: 删除实例(预付费包年包月)**

删除实例(预付费包年包月)

Input: 

```
tccli ckafka DeleteInstancePre --cli-unfold-argument  \
    --InstanceId ckafka-xxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "DeleteRouteTimestamp": "xx",
            "ReturnMessage": "xx",
            "ReturnCode": "xx",
            "Data": {
                "InstanceId": "xx",
                "FlowId": 0,
                "DealNames": [
                    "1111111111"
                ]
            }
        },
        "RequestId": "xx"
    }
}
```


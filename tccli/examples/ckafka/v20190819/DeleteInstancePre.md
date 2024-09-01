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
            "DeleteRouteTimestamp": null,
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "Data": {
                "FlowId": 0,
                "DealNames": [
                    "20240624186060707999999"
                ],
                "InstanceId": "ckafka-7777xxxx",
                "DealNameInstanceIdMapping": null
            }
        },
        "RequestId": "0b56102f-b4a4-4225-8ae5-60aea1234567"
    }
}
```


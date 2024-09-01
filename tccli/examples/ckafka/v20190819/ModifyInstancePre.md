**Example 1: 修改实例(预付费包年包月)**



Input: 

```
tccli ckafka ModifyInstancePre --cli-unfold-argument  \
    --InstanceId ckafka-xxxx \
    --BandWidth 40 \
    --DiskSize 600
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "abc",
            "ReturnMessage": "abc",
            "Data": {
                "FlowId": 0,
                "DealNames": [
                    "abc"
                ],
                "InstanceId": "abc",
                "DealNameInstanceIdMapping": [
                    {
                        "DealName": "abc",
                        "InstanceIdList": [
                            "abc"
                        ]
                    }
                ]
            },
            "DeleteRouteTimestamp": "abc"
        },
        "RequestId": "abc"
    }
}
```


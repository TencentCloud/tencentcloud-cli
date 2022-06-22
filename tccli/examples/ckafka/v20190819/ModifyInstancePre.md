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
            "DeleteRouteTimestamp": "xx",
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "Data": {
                "FlowId": 0,
                "InstanceId": "ckafka-xxxx",
                "DealNames": [
                    "1111111111"
                ]
            }
        },
        "RequestId": "1ba4ac83-1e9e-497b-b3e1-4c10872a4068"
    }
}
```


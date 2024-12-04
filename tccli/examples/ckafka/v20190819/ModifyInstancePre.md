**Example 1: 修改实例(预付费包年包月)**



Input: 

```
tccli ckafka ModifyInstancePre --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --BandWidth 40 \
    --DiskSize 600
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "Data": {
                "FlowId": 0,
                "DealNames": [
                    "name"
                ],
                "InstanceId": "ckafka-test",
                "DealNameInstanceIdMapping": [
                    {
                        "DealName": "name",
                        "InstanceIdList": [
                            "name"
                        ]
                    }
                ]
            },
            "DeleteRouteTimestamp": "2024-12-02 12:21:23"
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```


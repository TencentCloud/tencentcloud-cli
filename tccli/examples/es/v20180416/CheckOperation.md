**Example 1: 检查操作**

检查操作

Input: 

```
tccli es CheckOperation --cli-unfold-argument  \
    --InstanceId es-o3164dv0 \
    --OpType scalein
```

Output: 
```
{
    "Response": {
        "AbnormalNodes": [
            {
                "NodeId": "1772608355000145932",
                "NodeRole": "warmData"
            }
        ],
        "CheckSucc": false,
        "DiskUsageInfoList": [],
        "Message": "{\"1772608355000145932\":[\"test_wcy\"],\"1772610021000155232\":[\"test_wcy\"]}",
        "NeedForceResult": false,
        "ReasonType": -23,
        "RequestId": "3cf7645f-98a4-4322-bd92-0440f746b2b6"
    }
}
```


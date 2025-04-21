**Example 1: 检查操作**

检查操作

Input: 

```
tccli es CheckOperation --cli-unfold-argument  \
    --InstanceId es-xxxxxx \
    --OpType restart
```

Output: 
```
{
    "Response": {
        "CheckSucc": true,
        "NeedForceResult": false,
        "ReasonType": 0,
        "DiskUsageInfoList": [
            {
                "DiskType": "CLOUD_DISK",
                "NodeId": 17341724100
            }
        ],
        "RequestId": "22bcf772-63da-4bc3-b409-18a662fcedd4"
    }
}
```


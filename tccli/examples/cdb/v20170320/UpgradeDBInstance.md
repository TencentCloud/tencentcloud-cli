**Example 1: 升级云数据库实例**

升级云数据库实例

Input: 

```
tccli cdb UpgradeDBInstance --cli-unfold-argument  \
    --InstanceId cdb-6si6qy6p \
    --Volume 50 \
    --Memory 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "DealIds": [
            "20171204110077"
        ],
        "AsyncRequestId": "a6040589-3b098df5-b551d9e5-81c6bfdc"
    }
}
```


**Example 1: Upgrading a TencentDB instance**



Input: 

```
tccli cdb UpgradeDBInstance --cli-unfold-argument  \
    --InstanceId cdb-6si6qy6p \
    --Memory 1000 \
    --Volume 50
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


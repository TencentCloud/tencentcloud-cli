**Example 1: 启动延迟复制**

启动延迟只读实例的延迟复制。

Input: 

```
tccli cdb StartDelayReplication --cli-unfold-argument  \
    --InstanceId cdbro-test \
    --DelayReplicationType DUE_TIME \
    --DueTime 1600400231
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "818e3462-93b8a8a8-a4911f89-2896ed4d",
        "RequestId": "28a67cf3-4589-8534-2be0-17475fa5c892"
    }
}
```


**Example 1: 修改延迟只读实例的延迟复制时间**

修改延迟只读实例的延迟复制时间

Input: 

```
tccli cdb ModifyRoReplicationDelay --cli-unfold-argument  \
    --InstanceId cdbro-test \
    --ReplicationDelay 259200
```

Output: 
```
{
    "Response": {
        "RequestId": "28a67cf3-4589-8534-2be0-17475fa5c892"
    }
}
```


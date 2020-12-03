**Example 1: 修改只读实例类型**

修改只读实例类型

Input: 

```
tccli cdb ModifyRoType --cli-unfold-argument  \
    --InstanceId cdbro-test \
    --SrcRoInstType NORMAL \
    --DstRoInstType DELAY_REPLICATION \
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


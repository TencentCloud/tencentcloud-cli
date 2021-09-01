**Example 1: 切换实例主从角色**



Input: 

```
tccli cdb SwitchDBInstanceMasterSlave --cli-unfold-argument  \
    --InstanceId cdb-xxxxxxxx \
    --DstSlave second
```

Output: 
```
{
    "Response": {
        "RequestId": "faae8d6a-38fb-44de-988e-5a0e78aba4a7",
        "AsyncRequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```


**Example 1: 更改云数据库的模式**



Input: 

```
tccli cdb ModifyDBInstanceModes --cli-unfold-argument  \
    --InstanceId cdb-xxxx \
    --Mode protectMode \
    --ProtectMode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "9ad9c2d5-88007b27-7d2c8b8c-f2598f12"
    }
}
```


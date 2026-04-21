**Example 1: 修改实例复制方式**



Input: 

```
tccli cdb ModifyDBInstanceModes --cli-unfold-argument  \
    --InstanceId cdb-5cahthon \
    --Mode protectMode \
    --ProtectMode 1
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "2a3f5881-fed4de4d-edaca28e-8d16c732",
        "RequestId": "d226dcb0-e893-4a3b-bda1-0e5af6a191e4"
    }
}
```


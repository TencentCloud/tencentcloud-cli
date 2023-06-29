**Example 1: 批量删除权限示例**



Input: 

```
tccli trro BatchDeletePolicy --cli-unfold-argument  \
    --ProjectId f3glr49ry0i0xlm7 \
    --RemoteDeviceIds test1 test2 \
    --PolicyMode black
```

Output: 
```
{
    "Response": {
        "FailedRemoteDeviceIds": [],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```


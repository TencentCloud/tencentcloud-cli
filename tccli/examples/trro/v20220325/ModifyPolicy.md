**Example 1: 修改权限示例**



Input: 

```
tccli trro ModifyPolicy --cli-unfold-argument  \
    --ProjectId f3glr49rc96pralw \
    --RemoteDeviceId test3 \
    --FieldDeviceIds dev2 dev3 \
    --PolicyMode black \
    --ModifyMode add
```

Output: 
```
{
    "Response": {
        "FailedInsertIds": [],
        "FailedDeleteIds": [],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```


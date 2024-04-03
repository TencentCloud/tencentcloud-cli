**Example 1: 实例修改为单可用区**

将实例postgres-abcd1234主节点可用区调整广州3区，备节点调整为广州3区。

Input: 

```
tccli postgres ModifyDBInstanceDeployment --cli-unfold-argument  \
    --SwitchStartTime 12:00:00 \
    --DBNodeSet.0.Role Standby \
    --DBNodeSet.0.Zone ap-guangzhou-3 \
    --DBNodeSet.1.Role Primary \
    --DBNodeSet.1.Zone ap-guangzhou-3 \
    --DBInstanceId postgres-abcd1234 \
    --SwitchTag 1 \
    --SwitchEndTime 12:30:00
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

**Example 2: 实例修改为跨可用区**

将实例postgres-abcd1234主节点可用区调整广州1区，备节点调整为广州2区。

Input: 

```
tccli postgres ModifyDBInstanceDeployment --cli-unfold-argument  \
    --SwitchStartTime 12:00:00 \
    --DBNodeSet.0.Role Standby \
    --DBNodeSet.0.Zone ap-guangzhou-2 \
    --DBNodeSet.1.Role Primary \
    --DBNodeSet.1.Zone ap-guangzhou-1 \
    --DBInstanceId postgres-abcd1234 \
    --SwitchTag 1 \
    --SwitchEndTime 12:30:00
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```


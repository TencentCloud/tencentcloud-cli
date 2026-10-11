**Example 1: 更新角色**



Input: 

```
tccli mongodb UpdateInstanceRole --cli-unfold-argument  \
    --InstanceId cmgo-******** \
    --RoleName test1 \
    --Database admin \
    --Privileges.0.Resource.Cluster False \
    --Privileges.0.Resource.Database db1 \
    --Privileges.0.Actions find
```

Output: 
```
{
    "Response": {
        "TaskId": 4356114,
        "RequestId": "548ed7f8-9b2d-46ba-8703-ac96d5773edb"
    }
}
```


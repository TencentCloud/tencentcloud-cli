**Example 1: 创建角色**



Input: 

```
tccli mongodb CreateInstanceRole --cli-unfold-argument  \
    --InstanceId cmgo-******** \
    --RoleName trole11 \
    --Database admin \
    --Privileges.0.Resource.Cluster False \
    --Privileges.0.Resource.Database test123 \
    --Privileges.0.Actions find \
    --InheritedRoles.0.RoleName read \
    --InheritedRoles.0.Database test2
```

Output: 
```
{
    "Response": {
        "TaskId": 4339802,
        "RequestId": "27516215-8d94-4c60-875d-2ba74deef405"
    }
}
```


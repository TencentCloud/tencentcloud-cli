**Example 1: 查询角色**



Input: 

```
tccli mongodb DescribeInstanceRoles --cli-unfold-argument  \
    --InstanceId cmgo-******** \
    --Database admin \
    --RoleType builtin_database \
    --RoleName test1 \
    --SearchKey t \
    --OrderBy RoleName \
    --OrderType desc \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Roles": [],
        "Total": 0,
        "RequestId": "c746232b-75d3-4c34-aeef-60af9fd02ab6"
    }
}
```


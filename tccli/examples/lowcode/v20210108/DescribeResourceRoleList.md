**Example 1: 查询资源id对应角色列表**

查询资源id对应角色列表

Input: 

```
tccli lowcode DescribeResourceRoleList --cli-unfold-argument  \
    --ResourceId abc \
    --ResourceType abc \
    --SubType abc \
    --PageNo 0 \
    --PageSize 0 \
    --EnvType abc \
    --EnvId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "RoleList": [
                {
                    "Name": "abc",
                    "RoleIdentity": "abc",
                    "Id": 0,
                    "ParentRoleId": 0,
                    "ChildRoleId": 0,
                    "EnvIdentity": "abc",
                    "IsReleased": true
                }
            ],
            "Total": 0
        },
        "RequestId": "abc"
    }
}
```


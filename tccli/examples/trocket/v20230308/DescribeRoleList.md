**Example 1: 查询角色列表**

查询角色列表成功

Input: 

```
tccli trocket DescribeRoleList --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "c5d126b6-aeeb-40ad-81c0-a94abd43f157",
        "TotalCount": 1,
        "Data": [
            {
                "RoleName": "test_role_name",
                "AccessKey": "ak0000aaaa",
                "SecretKey": "sk0000aaaa",
                "PermRead": true,
                "PermWrite": true,
                "Remark": "",
                "CreatedTime": 1729153015000,
                "ModifiedTime": 1729153015000
            }
        ]
    }
}
```


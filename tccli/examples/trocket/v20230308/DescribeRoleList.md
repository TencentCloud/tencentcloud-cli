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
                "AccessKey": "ak4ae3zkj2zea6741a2a709",
                "SecretKey": "skd68607c7dc2be6a4",
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


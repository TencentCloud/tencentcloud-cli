**Example 1: 查询角色列表**

查询角色列表

Input: 

```
tccli trocket DescribeRoleList --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "AccessKey": "eyJrZXlJZCI6InJtcS03Mm1vM2E5byIsImFsZyI6IkhTMjU2In0.eyJzdWIiOiJybXEtNzJtbzNhOW9fdGVzdFJvbGUifQ.vrdHDzzfeDsX1c5rhaFcLpJBd_dGIWQIlAPLOuOEDfM",
                "CreatedTime": 1683615280000,
                "ModifiedTime": 1683615280000,
                "PermRead": true,
                "PermWrite": true,
                "Remark": "testRemark",
                "RoleName": "testRole",
                "SecretKey": "/tuS7zTKFNmsApaUvq4l5kTnV/GSWJ2m4bGhR62kVYY="
            }
        ],
        "RequestId": "346f63a2-dd66-439e-9abc-338a56f6523c",
        "TotalCount": 2
    }
}
```


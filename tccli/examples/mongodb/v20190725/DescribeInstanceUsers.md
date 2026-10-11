**Example 1: 查询账号**



Input: 

```
tccli mongodb DescribeInstanceUsers --cli-unfold-argument  \
    --InstanceId cmgo-********
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Users": [
            {
                "ConsolePassUpdateTime": "2026-04-14 17:43:04",
                "CreateTime": "2026-04-10 15:08:23",
                "Database": "admin",
                "Description": "测试用",
                "EnablePasswordRotation": 0,
                "Roles": [
                    {
                        "Database": "admin",
                        "RoleName": "backup"
                    }
                ],
                "UpdateTime": "2026-04-14 17:43:41",
                "UserName": "mongouser"
            }
        ],
        "RequestId": "6a80448e-130a-401f-94b4-ec8a74549416"
    }
}
```


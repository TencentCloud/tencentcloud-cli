**Example 1: 查询规则组列表**



Input: 

```
tccli fwm DescribeRuleGroups --cli-unfold-argument  \
    --Product enterprise_sg \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "78be528d-83c8-4999-b8a5-432f19493579",
        "RuleGroups": [
            {
                "AppId": "1300448058",
                "GroupId": "fwmrg-sygzqi8x",
                "GroupName": "测试策略",
                "RuleCount": 47,
                "Product": "enterprise_sg",
                "CreateTime": "2026-01-08 19:17:48",
                "UpdateTime": "2026-02-27 20:01:46",
                "CreateBy": "10001161111",
                "CreateName": "测试账号",
                "UpdateBy": "10001161111",
                "UpdateName": "测试账号",
                "ReceiveAccount": [
                    {
                        "Uin": "10001161111",
                        "Nickname": "测试账号"
                    }
                ],
                "ExecAreas": [
                    "pre"
                ]
            }
        ],
        "TotalCount": 94
    }
}
```


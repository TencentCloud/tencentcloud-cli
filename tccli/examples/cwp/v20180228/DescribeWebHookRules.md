**Example 1: 获取企微机器人规则列表**

获取企微机器人规则列表

Input: 

```
tccli cwp DescribeWebHookRules --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Order  \
    --By 
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "RuleId": 55,
                "RuleName": "测试机器人",
                "HookAddr": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=abe03861-a7c6-49cf-a12c-443c34be0db5",
                "RuleRemark": "",
                "RuleItems": [
                    {
                        "Type": 24,
                        "ControlBit": "1"
                    }
                ],
                "HostLabels": [],
                "HostCount": 0,
                "IsDisabled": 1,
                "CreateTime": "2023-02-17T18:41:03+08:00",
                "UpdateTime": "2023-02-28T10:18:15+08:00"
            }
        ],
        "RequestId": "e1b258f6-746d-4eb3-b7e0-ca400e7f8d71",
        "TotalCount": 8
    }
}
```


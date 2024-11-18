**Example 1: 获取用户特征规则列表**

获取用户特征规则列表

Input: 

```
tccli waf DescribeUserSignatureRuleV2 --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Offset 0 \
    --Limit 10 \
    --By CreateTime \
    --Order desc \
    --Filters.0.Name MainClassID \
    --Filters.0.Values 010000000 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Rules": [
            {
                "CreateTime": "2024-08-28T14:38:43+08:00",
                "CveID": "",
                "Description": "这条规则用于防止黑客通过注入生成一\"onload\"消息的处理函数，攻击可出现于HTTP请求的URL或者HTTP参数中",
                "ID": "10000041",
                "MainClassID": "010000000",
                "MainClassName": "XSS攻击",
                "ModifyTime": "2024-08-28T14:56:03+08:00",
                "Reason": 0,
                "RiskLevel": 1,
                "Status": 1,
                "SubClassID": "000000000",
                "SubClassName": "000000000"
            },
            {
                "CreateTime": "2024-03-06T10:13:07+08:00",
                "CveID": "",
                "Description": "本规则用于检测XSS注入拼接行为，本规则匹配的目标是ARGUMENT",
                "ID": "10000261",
                "MainClassID": "010000000",
                "MainClassName": "XSS攻击",
                "ModifyTime": "2024-06-24T11:13:25+08:00",
                "Reason": 0,
                "RiskLevel": 1,
                "Status": 1,
                "SubClassID": "000000000",
                "SubClassName": "000000000"
            }
        ],
        "RequestId": "dcd69dd3-94ef-4d66-88fb-625b81d11e47"
    }
}
```


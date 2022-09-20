**Example 1: 查询封禁客户端信息列表**



Input: 

```
tccli teo DescribeClientRuleList --cli-unfold-argument  \
    --Domain www.baidu.com \
    --Limit 1 \
    --Offset 1 \
    --RuleId 124552 \
    --SourceClientIp 1.2.3.4 \
    --RuleType acl \
    --ZoneId zone-21xfqlh4qjee \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "RequestId": "c0ce8b7c-a48f-4eed-a0eb-c24177efc430",
        "Data": [
            {
                "RuleType": "acl",
                "Description": "sql注入攻击",
                "RuleId": 124552,
                "BlockTime": 1659595468,
                "IpStatus": "block",
                "ClientIp": "1.2.3.4",
                "Id": "1659595468-acl-1.2.3.4"
            }
        ]
    }
}
```


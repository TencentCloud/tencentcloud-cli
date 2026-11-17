**Example 1: 编辑自定义规则**



Input: 

```
tccli waf ModifyCustomRule --cli-unfold-argument  \
    --Edition sparta-waf \
    --Domain www.example.com \
    --RuleId 17958569 \
    --RuleName ProtectAdminAccess \
    --RuleAction 1 \
    --SortId 100 \
    --ExpireTime 0 \
    --Strategies.0.Field IP \
    --Strategies.0.CompareFunc ipmatch \
    --Strategies.0.Content 192.0.2.10 \
    --Strategies.0.Arg  \
    --Preview 1 \
    --ActionRatio 100
```

Output: 
```
{
    "Response": {
        "RequestId": "a713f4cf-51ef-437f-8467-d4fdec061b78",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```


**Example 1: 编辑自定义规则**



Input: 

```
tccli waf ModifyCustomRule --cli-unfold-argument  \
    --Edition clb-waf \
    --Domain hfut.qcloud.com \
    --RuleId 17958569 \
    --RuleName test \
    --RuleAction 1 \
    --Redirect / \
    --Bypass geoip,cc,owasp,ai,antileakage \
    --SortId 100 \
    --ExpireTime 0 \
    --Strategies.0.Field IP \
    --Strategies.0.CompareFunc ipmatch \
    --Strategies.0.Content 1.1.1.2 \
    --Strategies.0.Arg 
```

Output: 
```
{
    "Response": {
        "RequestId": "a713f4cf-51ef-437f-8467-d4fdec061b78"
    }
}
```


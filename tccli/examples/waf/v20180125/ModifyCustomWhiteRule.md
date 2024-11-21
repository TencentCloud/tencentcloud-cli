**Example 1: 编辑精准白名单规则**



Input: 

```
tccli waf ModifyCustomWhiteRule --cli-unfold-argument  \
    --RuleId 1100000001 \
    --Domain waf.tencentcloudapi.com \
    --RuleName rulename \
    --Bypass cc \
    --SortId 100 \
    --ExpireTime 0 \
    --Strategies.0.Field COOKIE \
    --Strategies.0.CompareFunc eq \
    --Strategies.0.Content cookie_key \
    --Strategies.0.Arg cookie_value
```

Output: 
```
{
    "Response": {
        "RequestId": "5d207f4f-0d41-4f5d-bce2-0320090c98d8",
        "Success": {
            "Message": "Success",
            "Code": "Success"
        }
    }
}
```


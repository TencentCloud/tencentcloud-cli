**Example 1: 增加精准白名单规则**



Input: 

```
tccli waf AddCustomWhiteRule --cli-unfold-argument  \
    --Name name \
    --SortId 100 \
    --ExpireTime 0 \
    --Domain waf.tencentcloudapi.com \
    --Bypass cc,bot \
    --Strategies.0.Field COOKIE \
    --Strategies.0.CompareFunc eq \
    --Strategies.0.Content cookie_value \
    --Strategies.0.Arg cookie_key
```

Output: 
```
{
    "Response": {
        "RequestId": "5d207f4f-0d41-4f5d-bce2-0320090c98d8",
        "RuleId": 7025,
        "Success": {
            "Message": "Success",
            "Code": "Success"
        }
    }
}
```


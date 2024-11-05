**Example 1: 添加访问控制（自定义策略）**

增加访问控制（自定义策略）

Input: 

```
tccli waf AddCustomRule --cli-unfold-argument  \
    --Redirect /redirect_url \
    --Domain www.test.com \
    --Name name \
    --SortId 100 \
    --ExpireTime 0 \
    --Edition clb-waf \
    --ActionType 1 \
    --Strategies.0.Content cookie_value \
    --Strategies.0.Field COOKIE \
    --Strategies.0.CompareFunc eq \
    --Strategies.0.Arg cookie_key
```

Output: 
```
{
    "Response": {
        "RequestId": "1a16a333-76ac-42f5-8066-c0ea93cc8dc7",
        "RuleId": 7025,
        "Success": {
            "Message": "Success",
            "Code": "Success"
        }
    }
}
```


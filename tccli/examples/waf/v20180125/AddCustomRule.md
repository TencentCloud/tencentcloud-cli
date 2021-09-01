**Example 1: 增加自定义规则**



Input: 

```
tccli waf AddCustomRule --cli-unfold-argument  \
    --Name test \
    --SortId 100 \
    --Redirect / \
    --ExpireTime "" \
    --Strategies.0.Field COOKIE \
    --Strategies.0.CompareFunc null \
    --Strategies.0.Content "" \
    --Strategies.0.Arg "" \
    --Domain www.test.com \
    --ActionType 1 \
    --Edition clb-waf
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


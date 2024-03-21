**Example 1: 添加信息防泄漏规则**



Input: 

```
tccli waf AddAntiInfoLeakRules --cli-unfold-argument  \
    --Domain www.test1.com \
    --Name test \
    --ActionType 1 \
    --Strategies.0.Field information \
    --Strategies.0.CompareFunc contains \
    --Strategies.0.Content idcard \
    --Uri http://www.test1.com/123.txt
```

Output: 
```
{
    "Response": {
        "RequestId": "1a16a333-76ac-42f5-8066-c0ea93cc8dc7"
    }
}
```


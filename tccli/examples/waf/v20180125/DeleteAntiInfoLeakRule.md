**Example 1: 信息防泄漏删除规则**



Input: 

```
tccli waf DeleteAntiInfoLeakRule --cli-unfold-argument  \
    --Domain www.test.com \
    --RuleId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "36809618-b248-46fc-9513-0ecf86675215"
    }
}
```


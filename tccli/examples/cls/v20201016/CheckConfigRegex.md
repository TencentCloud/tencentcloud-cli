**Example 1: 校验采集配置中的正则**

校验采集配置中的正则

Input: 

```
tccli cls CheckConfigRegex --cli-unfold-argument  \
    --Regex (.*) \
    --Content hello
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Message": "regex match successful",
        "RequestId": "sadfasf-fasfasfa-fasfasdfads-zasdfas"
    }
}
```


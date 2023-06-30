**Example 1: 搜索CLS日志**

搜索CLS日志

Input: 

```
tccli tcb SearchClsLog --cli-unfold-argument  \
    --EnvId test-12323 \
    --StartTime abc \
    --EndTime def \
    --Limit 10 \
    --QueryString x \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "RequestId": "3e22b381-93a3-44c4-85b7-456679a7b8cd",
        "LogResults": {
            "Context": "",
            "ListOver": true,
            "Results": []
        }
    }
}
```


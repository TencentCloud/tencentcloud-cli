**Example 1: 搜索CLS日志**

搜索CLS日志

Input: 

```
tccli tcb SearchClsLog --cli-unfold-argument  \
    --EnvId test-12323 \
    --StartTime '2024-12-01 00:00:00' \
    --EndTime '2024-12-01 01:00:00' \
    --Limit 10 \
    --QueryString my-function-name \
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


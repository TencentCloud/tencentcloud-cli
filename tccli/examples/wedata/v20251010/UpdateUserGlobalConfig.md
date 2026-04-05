**Example 1: demo**



Input: 

```
tccli wedata UpdateUserGlobalConfig --cli-unfold-argument  \
    --ConfigItems.0.ConfigKey language \
    --ConfigItems.0.ConfigValue zh-CN \
    --ConfigItems.0.ConfigType 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "a5bcb46e-e474-4463-b50a-a05a001f44d6"
    }
}
```


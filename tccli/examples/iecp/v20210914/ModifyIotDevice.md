**Example 1: ModifyIotDevice**



Input: 

```
tccli iecp ModifyIotDevice --cli-unfold-argument  \
    --Disabled True \
    --LogSetting 0 \
    --LogLevel 0 \
    --Description 测试 \
    --DeviceId 100049
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3"
    }
}
```


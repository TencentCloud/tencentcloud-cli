**Example 1: 修改告警策略**

修改告警策略

Input: 

```
tccli cls ModifyAlarm --cli-unfold-argument  \
    --AlarmId alarm-fb0c92e7-xxxx-xxxx-b141-74859f894481 \
    --Name bow-test-中文
```

Output: 
```
{
    "Response": {
        "RequestId": "37fe3a72-xxxx-xxxx-951a-9468fa020261"
    }
}
```


**Example 1: 启用 ValkeyBloom 模块**



Input: 

```
tccli redis ModifyValkeyModule --cli-unfold-argument  \
    --InstanceId crs-d5rb**** \
    --Name ValkeyBloom \
    --Status ON
```

Output: 
```
{
    "Response": {
        "TaskId": 2031391183,
        "RequestId": "2ccfc821-f00d-43b7-b50d-fcceaa9c96a8"
    }
}
```


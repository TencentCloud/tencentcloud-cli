**Example 1: 手机号状态查询成功示例**



Input: 

```
tccli faceid MobileStatus --cli-unfold-argument  \
    --Mobile 13800138000
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "成功",
        "StatusCode": 1,
        "RequestId": "f893bfcf-167d-45df-99aa-60a23fe5809d"
    }
}
```

**Example 2: 手机号状态查询异常示例**



Input: 

```
tccli faceid MobileStatus --cli-unfold-argument  \
    --Mobile 16137688175
```

Output: 
```
{
    "Response": {
        "Description": "手机号格式不正确",
        "RequestId": "7411a5fc-0ba6-431d-9e8a-5f6537fb8701",
        "Result": "-2",
        "StatusCode": 99
    }
}
```


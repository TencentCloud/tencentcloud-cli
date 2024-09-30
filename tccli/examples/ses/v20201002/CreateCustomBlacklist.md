**Example 1: 添加邮箱地址到黑名单**



Input: 

```
tccli ses CreateCustomBlacklist --cli-unfold-argument  \
    --ExpireDate 2024-06-19 \
    --Emails b@gmail.com a@gmail.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

**Example 2: 成功示例**

成功示例

Input: 

```
tccli ses CreateCustomBlacklist --cli-unfold-argument  \
    --Emails resrse@sdasd.com resrse@sdasd.com asdasdasdasd
```

Output: 
```
{
    "Response": {
        "InvalidCount": 1,
        "RepeatCount": 1,
        "RequestId": "1e6f3195-f832-42a4-87ca-265a80435bc0",
        "TooLongCount": 0,
        "TotalCount": 3,
        "ValidCount": 1
    }
}
```


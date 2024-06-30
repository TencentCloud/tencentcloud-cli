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


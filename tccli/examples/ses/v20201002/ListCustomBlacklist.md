**Example 1: 获取自定义黑名单列表**



Input: 

```
tccli ses ListCustomBlacklist --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Status 1 \
    --Email abc@mail.com
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreateTime": "2024-06-26 10:04:43",
                "Email": "abc@foxmail.com",
                "ExpireDate": "2024-06-27",
                "Id": 304323,
                "Status": 1
            },
            {
                "CreateTime": "2024-06-25 14:27:38",
                "Email": "abc@abc.com",
                "ExpireDate": "2024-06-26",
                "Id": 304320,
                "Status": 0
            }
        ],
        "RequestId": "3df4264a-a5c9-4a4d-abfe-770c730ca683",
        "TotalCount": 293023
    }
}
```


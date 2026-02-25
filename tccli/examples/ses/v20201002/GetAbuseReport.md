**Example 1: 获取垃圾投诉数据**

获取垃圾投诉数据

Input: 

```
tccli ses GetAbuseReport --cli-unfold-argument  \
    --StartTime 2025-08-19 \
    --EndTime 2025-08-25 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ComplainTime": "2025-09-09 08:06:54",
                "DeliverTime": "2025-08-19 08:06:39",
                "FromDomain": "example.com",
                "InsertTime": "2025-09-09 19:13:07",
                "Mta": "qq.com",
                "OriginalMailFrom": "info@example.com",
                "OriginalRcptTo": "test@qq.com",
                "SourceIp": ""
            }
        ],
        "TotalCount": 88,
        "RequestId": "f211a0fe-2b62-4fdb-a9d9-b8b420b8be24"
    }
}
```


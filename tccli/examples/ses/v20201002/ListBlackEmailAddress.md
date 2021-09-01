**Example 1: 获取黑名单邮箱地址**



Input: 

```
tccli ses ListBlackEmailAddress --cli-unfold-argument  \
    --StartDate 2020-09-22 \
    --EndDate 2020-09-22 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BlackList": [
            {
                "BounceTime": "2020-09-22 00:00:00",
                "EmailAddress": "432843@qq.com"
            },
            {
                "BounceTime": "2020-10-22 12:10:00",
                "EmailAddress": "43fdaf2843@gmail.com"
            }
        ],
        "TotalCount": 2,
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

